# Introduction
In this lab, you will learn and practice using common test equipment used when making circuits. Many of the terms may not be fully defined and their relationship may not be clear yet, such as voltage, current, and resistance, but those will be covered in more detail in a future lab.

Most of the test equipment is either on your desk or in the locked drawer on the north side of the desk (the one facing the Prototyping Labs). Talk to a TA or member of the Prototyping Labs staff to get a key. You will be asked for an ID in exchange for the key to make sure we get the key back when you are done.

# Skills to Learn
- [Using a Power Supply](power_supply.md)
- [Using a Multimeter (DMM)](dmm.md)
- [Using a Signal Generator](signal_gen.md)
- [Using an Oscilloscope](oscope.md)

# Assignment
## Power Supply and Multimeter
1. Draw a diagram of the setup to read DC voltage with a multimeter.
1. Set your power supply to 4.75 V and 1 A, then verify with your multimeter. Take a picture of your setup.
1. Draw a diagram of the setup to read DC current with a multimeter.
1. Measure the DC current through a 1k ohm resistor, with your power supply set to 4.75 V and 1 A. Use the A plug on the multimeter, which is the one on the far left side. Take a picture of your results.
  1. If the result is less than 400 mA, reconnect your probe to the mA/uA port and record again. Compare this result with the previous one.

## Oscilloscope and Function Generator
1. Attach two 10X probes to your oscilloscope and calibrate them. Take a picture of your uncalibrated probes on the oscilloscope, then another once you have calibrated them.
1. With the load set to "High Z," generate a ramp wave shape, with peak-to-peak amplitude of 2.5 V, minimum voltage at 0.0V, and frequency set to 100kHz. On the oscilloscope set the horizontal scale to 4 micro-sec per capture. Take a screenshot of the wave on your oscilloscope.
    1. Count the number of positive peaks on the screen and explain why you get the number you get.
    1. Read and record the peak-to-peak amplitude and minimum voltage.
    1. Set the horizontal scale to 1 micro-sec per division and repeat the previous two steps.
1. Repeat the previous step with the following settings:

| Test Case | Waveform | Frequency | Peak to Peak Voltage | Vmin |
| --- | --- | --- | --- | --- |
| W1 | Square | 1.0 MHz | 0.5 V | -.25 V |
| W2 | Sine | 1000 Hz | 1.5 V | 0.0V |
| W3 | Ramp (50/50) | 200 kHz | 3.0 V | -1.5V |
| W4 | Pulse: 5% on 95% off (duty) | 1 MHz | 3.0 V | 0.0 V |

# Frequently Asked Questions
**Q: I have set up the signal generator and connected it to the oscilloscope, but the signal seems flat.**

A: Please check if the output of the signal generator is ‘On’. There is a yellow button ‘On/Off’ on the signal generator. It will light up if the output is ‘On’.


**Q: I have signal wave(s) shown on the oscilloscope, but how to I measure the voltage?**

A: You need to add measurement on the screen of oscilloscope. See the [oscilloscope article.](oscope.md)

**Q: The waveform on the oscilloscope looks correct, but the amplitude (voltage) is 2 times larger / half than the expectation.**

A: This is usually caused by the ‘load’ setting on your signal generator does not match your actual circuit setting. You may need to switch the ‘load’ mode on the signal generator. See the [signal generator article for how to change the load.](signal_gen.md)

**Q: I changed the ‘load’ setting on the signal generator, but the output does not change.**

A: This is a counter-intuitive performance of the signal generator. Once you change the ‘load’ mode, the signal generator will double or half the voltage value. Please double-check the voltage setting every time you change the ‘load’ mode.
