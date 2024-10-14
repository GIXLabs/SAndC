from machine import Pin, ADC
import time

# Variables
PulseSensorSignalPin = 0  # Pulse Sensor Signal Pin connected to ADC Pin 0 (GPIO 36)
LED = Pin(2, Pin.OUT)    # On-board LED (or external LED if needed)
Threshold = 550           # Threshold to detect a beat

# Set up ADC for PulseSensor
adc = ADC(Pin(4, Pin.IN))        # ADC Pin for Pulse Sensor (GPIO 4)
adc.atten(ADC.ATTN_11DB)  # Configure the ADC range (11dB attenuation gives full 3.3V range)
adc.width(ADC.WIDTH_10BIT)  # 10-bit resolution (0-1023 values, similar to Arduino)

# Main loop
while True:
    Signal = adc.read()   # Read the PulseSensor's value

    print(Signal)         # Send the Signal value to the REPL or a serial monitor

    if Signal > Threshold:  # If the signal is above 550, turn on the LED
        LED.value(1)
    else:                  # Else, turn off the LED
        LED.value(0)

    time.sleep(0.005)     # Small delay (5 milliseconds)

