# Final Project Take-Home Assignment 3

## Goals
- Learn Filtering/Calibration Techniques for the accelerometer 
- Detect directional movement with the accelerometer
- Interfacing with NeoPixels 
- Interfacing with Push Buttons
- Creating Helper Functions

## Deliverables

Anything marked with a ✏️ must be included in your deliverable. Your final deliverable will be a pdf containing any pictures and code (screenshot or copy/pase are both acceptable) asked for. Please make sure your responses are ordered in the same way as they are given. Title each section of your responses so that they correspond to the section you are giving your answers to.

## Useful Resources

- [Guide to Helper Functions](https://www.geeksforgeeks.org/javascript/what-are-the-helper-functions/#)
- [Push Buttons](https://learn.adafruit.com/multi-tasking-with-circuitpython/buttons)
- [Debouncing in Circuitpython](https://learn.adafruit.com/debouncer-library-python-circuitpython-buttons-sensors/basic-debouncing)
- [Neopixels in Circuitpython](https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel)
- [Infromative article about Accelerometer Calibration](https://thecavepearlproject.org/2015/05/22/calibrating-any-compass-or-accelerometer-for-arduino/)


## Filering/Calibrating Accelerometers

There are many filters and techniques available to help increase the accuracy and reduces the noise for accelerometers. Generally, you would perform a Fourier Transform on the signals output from your accelerometer to get a better idea of what filters would work for you. However, since you have not taken TECHIN 513 yet we will not go into that process. We will instead look into and implement some common filters that are used with accelerometers.

### Zero Offset Calibration

Before we get into filters we will perfrom a simple calibration process for the accelerometer. If we have the accelerometer sitting flat on a table we would expect that acceleration in the X and Y axis to be zero and 9.81 m/s in the Z axis. This is almost never the case, if you were to take readings with your accelerometer laid flat and not moving you would get some small readings for X and Y and readings around but precisely 9.81 m/s for Z. Zero Offset Calibration helps compensate for this. There are multiple ways to implement this type of calibration, but we will focus on a more novel way to accomplish it.

The way we will implement Zero Offset Calibration is to take some amount of sample readings for each axis and then take the average of those readings and store those values into variables. Those variables are usually referred to as the baseline. To complete the calibration, everytime we take a reading we will subtract the baseline from the raw reading of the accelerometer.

✏️ Implement Zero Offset Calibration using the method described above. Here is an itemized list of what the process should be:

- Take at least 20 readings for each axis and get the average
- store the average for each axis into their own variable. These variables are storing the baseline
- Take a reading from the accelerometer and substract the baselines from them.

**Be warned that if you do this process with the Z-axis then it would also give calibrated values close to zero. This is fine depending on your application.**

Here is some starter code to help you:
```
import board
import time
import adafruit_adxl34x

i2c = board.I2C() 

accelerometer = adafruit_adxl34x.ADXL345(i2c)

x, y, z = accelerometer.acceleration # This is how you save accelerometer readings into variables
```
There are multiple ways you can get the average of the readings. Two examples are saving the readings in lists, use the sum built-in function and divide by the length of the list or you can instantiate variables that hold the sums and add to these variables everytime you take a reading and then divide by the number of readings. Both examples require you to code a loop to take the readings.

✏️ Once you have accomplished the calibration print out raw and calibrated readings for each axis to your shell and take a screenshot. Be sure to add your code to your deliverable as well.

### Filtering

There are many filters that are commonly used for accelerometers but this assignment will introduce the following: Lowpass Filter, Highpass Filter, and Magnitude Filter.

One of the most popular lowpass filters used for sensors is the [Exponential Moving Average](https://en.wikipedia.org/wiki/Exponential_smoothing) filter. This filter is very good at smoothing out the readings and eliminates high frequency noise caused by jitter, vibration, EMI, etc. One of the big reasons this filter is popular in microcontroller applications is how easy it is to implement.

Here is the equation to implement this filter: **signalFiltered = alpha * rawSignal + (1 - alpha) * signalFiltered**

Where alpha is known as the smoothing factor. The lower alpha is the more your signal smoothed. Typical alpha values range from 0.1 - 0.6. The higher alpha is the less effect the filter will have on your signal.

To get a better idea on how this filter effects your signal here is an image where the blue line represents the y-axis reading of the accelerometer and the orange line shows the filtered y-axis reading.

