/*
 Setup your scale and start the sketch WITHOUT a weight on the scale
 Once readings are displayed place the weight on the scale
 Press +/- or a/z to adjust the calibration_factor until the output readings match the known weight
 Arduino pin 6 -> HX711 CLK
 Arduino pin 5 -> HX711 DOUT
 Arduino pin 5V -> HX711 VCC
 Arduino pin GND -> HX711 GND 
*/

#include "HX711.h"

HX711 scale(5, 6);

float calibration_factor = 100; // this calibration factor is adjusted according to my load cell
 

void setup() {
  Serial.begin(9600);
  Serial.println("GIX Techin512 HX711 calibration sketch");
  Serial.println("Remove all weight from scale");
  Serial.println("After readings begin, place known weight on scale"); 

  scale.set_scale();
  scale.tare();  //Reset the scale to 0

  long zero_factor = scale.read(); //Get a baseline reading 
}

void loop() {
  long reading;
  delay(200);
  Serial.print("Reading: ");
  reading = scale.read();
 // if (units < 0)
 // {
 //  units = 0.00;
 //  }
  Serial.print(reading);
  Serial.print(" raw");  
  Serial.println();
 
}
