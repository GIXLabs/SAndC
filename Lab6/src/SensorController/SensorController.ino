#include <Adafruit_BMP280.h>
#include <Adafruit_LSM6DS33.h>
#include <Adafruit_SHT31.h>
#include <Adafruit_APDS9960.h>
#include <Adafruit_Sensor.h>
#include <PDM.h>

Adafruit_BMP280 bmp280;      // temperautre, barometric pressure
Adafruit_LSM6DS33 lsm6ds33;  // accelerometer, gyroscope
Adafruit_SHT31 sht30;        // humidity
Adafruit_APDS9960 apds9960;  // light, color

float temperature, pressure, altitude;
float accel_x, accel_y, accel_z;
float gyro_x, gyro_y, gyro_z;
float humidity;
uint8_t proximity;
uint16_t r, g, b, a;
int32_t mic;

extern PDMClass PDM;
short sampleBuffer[256];  // buffer to read samples into, each sample is 16-bits
volatile int samplesRead; // number of samples read

void setup(void) {
  Serial.begin(115200);
  //  while (!Serial) delay(10);

  // initialize the sensors
  apds9960.begin();
  apds9960.enableProximity(true);
  apds9960.enableColor(true);
  bmp280.begin();
  lsm6ds33.begin_I2C();
  sht30.begin();
  PDM.onReceive(onPDMdata);
  PDM.begin(1, 16000);
}

void loop(void) {
  proximity = apds9960.readProximity();
  while (!apds9960.colorDataReady()) {
    delay(5);
  }

  apds9960.getColorData(&r, &g, &b, &a);
  temperature = bmp280.readTemperature();
  pressure = bmp280.readPressure();
  altitude = bmp280.readAltitude(1013.25);

  sensors_event_t accel;
  sensors_event_t gyro;
  sensors_event_t temp;
  lsm6ds33.getEvent(&accel, &gyro, &temp);
  accel_x = accel.acceleration.x;
  accel_y = accel.acceleration.y;
  accel_z = accel.acceleration.z;
  gyro_x = gyro.gyro.x;
  gyro_y = gyro.gyro.y;
  gyro_z = gyro.gyro.z;

  humidity = sht30.readHumidity();

  samplesRead = 0;
  mic = getPDMwave(4000);

  Serial.print(temperature);
  Serial.print(",");
  Serial.print(pressure);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.print(altitude);
  Serial.print(",");
  Serial.print(accel_x);
  Serial.print(",");
  Serial.print(accel_y);
  Serial.print(",");
  Serial.print(accel_z);
  Serial.print(",");
  Serial.print(gyro_x);
  Serial.print(",");
  Serial.print(gyro_y);
  Serial.print(",");
  Serial.print(gyro_z);
  Serial.print(",");
  Serial.print(mic);
  Serial.print(",");
  Serial.print(r);
  Serial.print(",");
  Serial.print(g);
  Serial.print(",");
  Serial.print(b);
  Serial.print(",");
  Serial.print(a);
  Serial.println();

  delay(200);
}

/*****************************************************************/
int32_t getPDMwave(int32_t samples) {
  short minwave = 30000;
  short maxwave = -30000;

  while (samples > 0) {
    if (!samplesRead) {
      yield();
      continue;
    }
    for (int i = 0; i < samplesRead; i++) {
      minwave = min(sampleBuffer[i], minwave);
      maxwave = max(sampleBuffer[i], maxwave);
      samples--;
    }
    // clear the read count
    samplesRead = 0;
  }
  return maxwave - minwave;
}

void onPDMdata() {
  // query the number of bytes available
  int bytesAvailable = PDM.available();

  // read into the sample buffer
  PDM.read(sampleBuffer, bytesAvailable);

  // 16-bit, 2 bytes per sample
  samplesRead = bytesAvailable / 2;
}
