# Introduction

The purpose of this lab is to learn about several of the ways to sense temperature.

# Background

- [Thermocouple](https://en.wikipedia.org/wiki/Thermocouple)

- [What is the effect of temperature on semiconductor diode](https://www.quora.com/What-is-the-effect-of-temperature-on-semiconductor-diode)

- [Thermistor](https://en.wikipedia.org/wiki/Thermistor)

- [Adafruit Feather nRF52840 Sense](https://www.adafruit.com/product/4516)

- [Overview of Adafruit Feather Sense\*\*](https://learn.adafruit.com/adafruit-feather-sense)

# Resources

## One-Wire
- [Circuitpython OneWire Documentation](https://docs.circuitpython.org/projects/onewire/en/latest/index.html)
- [**1-Wire Tutorial**](https://www.hacktronics.com/tutorials/arduino-1-wire-tutorial.html)

# Write-Up

The writeup for this lab should contain the following outline:

1. Title page (see template in the folder ‘Requirement of Lab Reports’)
1. Introduction
   ⅓ of a page describing the purpose and goals of this lab in your own words. Do not reproduce any material from this assignment document in any section of your writeup.
1. Results
   Each location in the instructions below marked with “✏️” indicates some data which must appear in your report.

# Pre-lab computations:

None.

## Parts, tools, supplies required

- Dallas Semi "One-Wire" temperature sensor
- Type K thermocouple with Max6675 thermocouple amplifier/SPI interface breakout
- MF52 10KOhm thermistor
- Ice-water
- Boiling water

# Procedure
```diff
- Be careful with water, please keep (hot) water away from yourself and intruments.
```
1. A lab station will be set up with the water baths. Please coordinate with other groups for their use.
1. Referring to the Resources and your pre-lab calculations above, interface each device to the either an Arduino or DMM as follows:

## One-Wire Sensor



1. We have two types of one-wire sensors: stainless steel cylinder, or BJT package. Connect the sensor to your ESP32, GND to GND, Vcc to 3V3, and Data to any digital pin on the ESP32.
1. Open Thonny and run the script below make sure that the data pin you connected to your ESP32 is consistent with the one used in the code or vise versa.
```
import time
import board
from adafruit_onewire.bus import OneWireBus

from adafruit_ds18x20 import DS18X20

ow_bus = OneWireBus(board.D5)
ds18 = DS18X20(ow_bus, ow_bus.scan()[0])

while True:
    print(f"Temperature: {ds18.temperature:0.3f}C")
    time.sleep(0.5)
```

5. As you get each sensor working, take each one to the ice-water and boiling-water baths.
6. ✏️ Record reading of the sensor in ice water & boiled water. Get at least 10 readings of both boiling and ice water

## Thermistor:

<img src="assets/thermistor_2.png" alt="Thermistor" width="250"/>

1. Attach Fluke DMM to thermistor with alligator clips
2. ✏️ Using water baths, record resistance at
   - ✏️ Room temperature
   - ✏️ 0&deg;C
   - ✏️ 100&deg;C
3. The ESP32 analog input can handle input voltages from 0-3.3V. Design a DC circuit making a voltage divider with:
   - 3.3V input (from 3V3 pin on ESP32)
   - Resistor (R) around 10K Ohm
   - Thermistor
   - The voltage across the 10K-thermistor voltage should range from 0-3.3V for any temperature from -10&deg;C to + 110&deg;C.
4. You should **NOT** expect a straight line relationship.
   - Recall the voltage dividers' equation, use the voltage divider you designed and the voltage measured (V) to calculate the thermometer's resistance(R), and record the relationship between R and T.
   - ✏️ Try to fit a logarithmic function T = a\*log(R)+b or 2nd order polynomial (R = aT^2 + bT + c) to three data points: 0&deg;C, Room Temp, 100&deg;C (where y is resistance and x is temperature).
6. Write an Circuitpython script that reads the analog port and prints the reading.
   - Your analog input should be the voltage that you measured earlier. You can refer to [this page](https://learn.adafruit.com/circuitpython-essentials/circuitpython-analog-in?gad_source=1&gad_campaignid=21079267614&gbraid=0AAAAADx9JvRd5jGftl1VVKVzLqWUmFp5e&gclid=Cj0KCQiA5abIBhCaARIsAM3-zFUWpUP0xXIMxv00rPqMOSnX_utmNfTAWRiLHmxl7k-Yw6MwOJ-OOucaAvgdEALw_wcB) for Circuitpython Analog Input.
   - ✏️ Demonstrate that it works using the water baths.
8. ✏️ Record reading of the sensor in ice water & boiled water.
9. Code Implementation:
   - ✏️ Implement the logarithmic or polynomial equation on the Arduino.
   - ✏️ Take a screenshot of the correct temperature readout.


