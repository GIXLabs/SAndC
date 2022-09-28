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
1. Draw a diagram of the setup to [read DC voltage with a multimeter](dmm.md/#measuring-voltage).
1. [Set your power supply](power_supply.md) to 4.75 V and 1 A, then verify with your multimeter. Take a picture of your setup.
1. Draw a diagram of the setup to [read DC current](dmm.md/#measuring-current) with a multimeter.
1. Measure the DC current through a 1k ohm resistor, with your power supply set to 4.75 V and 1 A. Use the A plug on the multimeter, which is the one on the far left side. Take a picture of your results.
  1. If the result is less than 400 mA, reconnect your probe to the mA/uA port and record again. Compare this result with the previous one.

## Oscilloscope and Signal Generator
1. [Attach two 10X probes](oscope.md/#connecting-probes) to your oscilloscope and [calibrate them](oscope.md/#calibrating-oscilloscope-probes). [Adjust the vertical position](oscope.md/#adjusting-the-display) of each signal so that they overlap.
    1. Take a picture of the waveform with your uncalibrated probes on the oscilloscope, then another once you have calibrated them. Note: you may want to leave labels in your pictures so you can reference them later in your write-up.
1. [Set your signal generator and oscilloscope up with a 47 Ohm resistor.](oscope.md/#investigating-a-circuit) On the signal generator, [set the load to "High Z,"](signal_gen.md/#changing-mode) and [generate a ramp waveform (50/50)](signal_gen.md/#changing-the-waveform), with [peak-to-peak amplitude of 2.5 V, minimum voltage at 0.0V](signal_gen.md/#adjusting-amplitude), and [frequency set to 100kHz](signal_gen.md/#adjusting-frequency). Remember to turn the signal on. On the oscilloscope set the horizontal scale to 4 micro-sec per capture. Take a screenshot of the wave on your oscilloscope.
    1. Count the number of positive peaks on the screen and explain why you get the number you get.
    1. [Read and record the peak-to-peak amplitude and minimum voltage.](oscope.md/#measuring-voltage)
    1. Set the horizontal scale to 1 micro-sec per division and repeat the previous two steps.
1. Repeat the previous exercise for each setting in the table below. Note: you just did W0 in the previous steps.

| Test Case | Waveform | Frequency | Peak to Peak Voltage | Vmin |
| --- | --- | --- | --- | --- |
| W0 | Ramp (50/50)| 100 kHz | 2.5 V | 0.0 V |
| W1 | Square | 1.0 MHz | 0.5 V | -.25 V |
| W2 | Sine | 1000 Hz | 1.5 V | 0.0V |
| W3 | Ramp (50/50) | 200 kHz | 3.0 V | -1.5V |
| W4 | Pulse: 5% on 95% off (duty) | 1 MHz | 3.0 V | 0.0 V |

# Write-Up
The write-up for this lab should use the following outline:

1. **Title page** (see template in the folder ‘Requirement of Lab Reports’)
1. **Introduction:** ⅓ of a page describing the purpose and goals of this lab in your own words. Do not reproduce any material from this assignment document in any section of your write-up.
1. **Results:** Each line in the Assignment section indicates some data which must appear in your report. Separate each result or related set of results with a section header indicating what it is. For any numerical data or graph describe the meaning of the data.
1. **Discussion and Conclusions:** In ½ to 1 page, summarize the key learning points from the Results above.

# Frequently Asked Questions
**Q: I have set up the signal generator and connected it to the oscilloscope, but the signal seems flat.**

A: Please check if the output of the signal generator is ‘On’. There is a yellow button ‘On/Off’ on the signal generator. It will light up if the output is ‘On’.


**Q: I have signal wave(s) shown on the oscilloscope, but how to I measure the voltage?**

A: You need to add measurement on the screen of oscilloscope. See the [oscilloscope article.](oscope.md/#measuring-voltage)

**Q: The waveform on the oscilloscope looks correct, but the amplitude (voltage) is 2 times larger / half than the expectation.**

A: This is usually caused by the ‘load’ setting on your signal generator does not match your actual circuit setting. You may need to switch the ‘load’ mode on the signal generator. See the [signal generator article](signal_gen.md/#changing-mode-(high-z))  for how to change the load.

**Q: I changed the ‘load’ setting on the signal generator, but the output does not change.**

A: This is a counter-intuitive performance of the signal generator. Once you change the ‘load’ mode, the signal generator will double or half the voltage value. Please double-check the voltage setting every time you change the ‘load’ mode.
