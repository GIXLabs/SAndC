# Introduction

The purpose of this lab is to learn about several of the ways to sense temperature.

# Background

- [Thermocouple](https://en.wikipedia.org/wiki/Thermocouple)

- [What is the effect of temperature on semiconductor diode](https://www.quora.com/What-is-the-effect-of-temperature-on-semiconductor-diode)

- [Thermistor](https://en.wikipedia.org/wiki/Thermistor)

- [Adafruit Feather nRF52840 Sense](https://www.adafruit.com/product/4516)

- [Overview of Adafruit Feather Sense\*\*](https://learn.adafruit.com/adafruit-feather-sense)

# Resources:

# One-Wire

- [**One-Wire to Arduino Interfacing**](https://www.tweaking4all.com/hardware/arduino/arduino-ds18b20-temperature-sensor/)
- [**One-Wire Arduino Library**](https://www.pjrc.com/teensy/td_libs_OneWire.html)
- [**1-Wire Tutorial**](https://www.hacktronics.com/tutorials/arduino-1-wire-tutorial.html)

# Write-Up

The writeup for this lab should contain the following outline:

1. Title page (see template in the folder ‘Requirement of Lab Reports’)
2. Introduction
   ⅓ of a page describing the purpose and goals of this lab in your own words. Do not reproduce any material from this assignment document in any section of your writeup.
3. Results
   Each location in the instructions below marked with “✏️” indicates some data which must appear in your report.

# Pre-lab computations:

## Compute all resistor values for step 2 below.

## Parts, tools, supplies required:

- Dallas Semi "One-Wire" temperature Sensor
- Type K thermocouple with Max6675 thermocouple amplifier/SPI interface breakout
- MF52 10KOhm thermistor
- Diode
- Ice-water
- Boiling water
- Heat gun

# Procedure:

1. A lab station will be set up with the water baths. Please coordinate with other groups for their use.
2. Referring to the Resources and your pre-lab calculations above, interface each device to the either an Arduino or DMM as follows:

## One-wire sensor:

1. We have two types of one-wire sensors: Stainless Steel cylinder, or BJT package. Use appropriate hookup as shown:
1. Hook up to Arduino, install and run driver software (see Resources above).
1. Download the [one-wire-512.ino](one-wire-512/one-wire-512.ino) to the arduino, print values to your PC
1. As you get each sensor working, take each one to the ice-water and boiling-water baths.
1. ✏️ Record reading of the sensor in ice water & boiled water.
1. ✏️ Using the fact that ice-water is very close to 0 deg C and boiling water is very close to 100C, derive 2nd order polynomial calibration factors for thermistor. (If you find your type-K sensor or one-wire sensor is also not very accurate, you can also perform calibration. In this case, a linear calibration is often good enough)

## Thermistor:

1.  Attach Fluke DMM to thermistor with alligator clips
1.  ✏️ Record resistance at \> room temperature \> 0&deg;C \> 100&deg;C (using water baths)
1.  The Arduino analog input can handle input voltages from 0-5V. Design a DC circuit making a voltage divider with
    1.  5V input (from Vcc pin on arduino)
    1.  A resistor R
    1.  The Thermistor
    1.  So that the voltage across the 10K-thermistor voltage will range from 0-5V for any temperature from -10&deg;C to + 110&deg;C.
1.  You should **NOT** expect a straight line relationship. \> Try to fit a 2nd order polynomial (y = ax^2 + bx + c) to three data points: 0&deg;C, Room Temp, 100&deg;C (where y is resistance and x is temperature).
1.  Write an Arduino sketch which reads the analog port and prints the reading.
    1.  ✏️ demonstrate that it works using the water baths.

For two points extra credit:
✏️ Implement the polynomial equation (iv) on the Arduino
✏️ Demo correct temperature readout

✏️ Record reading of the sensor in ice water & boiled water.

## Adafruit Feather nRF52840 Sense:

Now you have some familiarity with temperature sensors. Let's use a hardware board to get large data sets and do analysis

1. Set up environment:

- Arduino: [install](https://www.arduino.cc/en/software)
  - Please install all libraries in **libs** folder

(Sketch -\> Include Library -\> Add .ZIP Library)

- Install nRF52840 board manger: [install](https://learn.adafruit.com/adafruit-feather-sense/arduino-support-setup)

- Python 3 (3.7 or higher): [install python3](https://www.python.org/downloads/)
- Install Python Serial Port Extension: `pip3 install pyserial`
- Google Colab [open](https://colab.research.google.com/)

1. Once you're done with the installation
1. Upload the [SensorController](adafruit_nRF52840_Sense/SensorController/../Tech512-Lab6Part3-52840/SensorController/SensorController.ino) to **nRF52840**, you will see reading of the temperature sensor on the board, the data will be printed around every 0.5 seconds.
1. Uncomment **Serial.print** command from line 68-95. Take a screenshot of reading from all sensors on the board.

1. **Close the Serial Monitor in Arduino studio** and run [logging.py](adafruit_nRF52840_Sense/Tech512-Lab6Part3-52840/logging.py). The software will create a csv file to logs/{currentTime}.csv and you can stop it by CTRL+C

### Other options

1. Create a Colab or run [lab6.ipynb](adafruit_nRF52840_Sense/Tech512-Lab6Part3-52840/lab6.ipynb) with Jupyter. You can upload the csv file by drag and drop to the file menu.

1. ✏️ Plot the temperature data with time
1. ✏️ Open-ended question: Capture the data for more than 1 minute. Choose the data you are interested in, plot the graph, do analyze: what do you get from the data?

### Hint:

1.  You can collect accelerator data and measure the number of steps the user takes within one minute
1.  You can breathe towards the nRF52840 board and get your breathing temperature, breathing humidity, changing in air pressure. (An example for cohort 4: [adds Calypso Mask M3.ppt])
1.  Analyze the levels of sound in different room or different machine (the sound of 3D printer VS the sound of laser cutter)
