# Introduction

In this lab we will be exploring [Ohm's Law](https://youtu.be/8jB6hDUqN0Y?t=162), which specifies the relationship between voltage (V), current (I), and resistance (R).
V = IR

# Skills to learn

1. How to understand Ohm's law
2. How to distinguish between series and parallel
3. How to get started with ESP32

# Pre-Lab Calculations

1. ✏️ A 1000 Ohm resistor is connected to 20 V. Find the current through the resistor:
2. ✏️ Two 2K Ohm resistors are connected in series. The current through them is 1.5mA. Find the voltage across the two and also across each one separately.
3. ✏️ A 2K and a 500 Ohm resistor are connected in parallel across a 1.5V battery. Find the current draw from the battery and also the current in each resistor.
4. ✏️ A 100 Ohm and 900 Ohm resistor are connected in series across a 9V battery. Find the voltage across the 100 Ohm resistor.

## Supplies

- Resistors: 2x 1000 Ohm and 1x 500 Ohm (two 1000 Ohm resistors in parallel can work as a 500 Ohm resistor if you cannot find a 500 Ohm resistor)
- Alligator clip leads
- Breadboard
- Handheld multimeter (yellow)

## Write-Up

The writeup for this lab should contain the following outline:

(you can download the writeup template [here](/Lab2/Lab2_WriteUp.docx))

1. Title page (see template in the folder ‘Requirement of Lab Reports’ on Canvas)
2. Introduction
   - ⅓ of a page describing the purpose and goals of this lab in your own words. Do not reproduce any material from this assignment document in any section of your writeup.
3. Results
   - First include the Pre-lab computations.
   - Then, each location in the instructions below marked with ✏️ indicates some data which must appear in your report. Separate each result or related set of results with a section header indicating what it is. For any numerical data or graph describe the meaning of the data.
4. Discussion and Conclusions:
   - In ½ to 1 page, summarize the key learning points from the Results above.

# Assignment

## 1. [Ohm’s Law](https://youtu.be/8jB6hDUqN0Y?t=162)

1. Set the DMM to measure resistance and measure the resistance of your 1000 Ohm resistor (may show up as 1k on multimeter).
2. ✏️ Compare measured resistance with “1000 Ohms”.
   - ✏️ What is the percentage of error? (Tip: it is better to always check the resistance of a resistor before using it.)
3. Set up the [power supply](/Lab1/power_supply.md) for +10 V, connect 1000 Ohm resistor across power supply.
4. [Set DMM to Voltage mode](/Lab1/dmm.md#measuring-voltage), and verify +10V DC across 1K Ohm resistor.

   ![VerifyVoltage](/assets/Lab2-16.jpg)

5. Switch your [DMM to current mode](/Lab1/dmm.md#measuring-current) (change Red lead to A)
6. [Connect your DMM](/Lab1/dmm.md#measuring-current) between resistor and power supply ground as follows:

   - Disconnect the resistor from power supply GND
   - Connect the red lead (A) of DMM to the resistor
   - Connect the black lead (COM) of DMM to power supply GND

   ![VerifyCurrent](/assets/Lab2-15.jpg)

   ![DivLoad3](/assets/Lab2-24.png)

   - ✏️ Diagram your circuit (without the DMM)
   - ✏️ Record the current reading and indicate your measured current with a directional arrow on the circuit.
   - ✏️ Compare the reading to expected current from [Ohm’s Law]. What is the current error if you use the measured vs specified (1000 Ohm) resistance?

7. [Change the voltage](/Lab1/power_supply.md#voltage) to {5.0V, 2.5V, 0.2V}
8. ✏️ Record the current in each case and graph voltage (Y axis) vs. Current (X axis). Label your graph with units.
9. ✏️ Fit a line to your data and compute its slope. Compare with 1000 Ohms.

## 2. [Parallel](/Lab2/information/series_vs_parallel.md) Resistors

1. Connect two 1000 Ohm resistors in parallel (connect the two resistors at both ends) with alligator clips or simply twist them together, [connect them between +10V DC and GND](/Lab1/dmm.md#power_supply).

   - ✏️ What is power supply current readout?

   ![ParCurrent3](/assets/Lab2-23.png)

   ![ParCurrent1](/assets/Lab2-14.png)

2. [Set up your DMM for current measurement](/Lab1/dmm.md#measuring-current). Plug red lead into “A” (see instructions/diagram, 1.5/1.6, above)
3. ✏️ Measure the current between the power supply ground and the pair of resistors (i.e. total current of both resistors).

   ![ParCurrent2](/assets/Lab2-13.png)

4. Reconnect resistors and DMM as necessary to measure voltage across the two resistors, and the current in each resistor separately.
   - ✏️ Record your measurements.
   - ✏️ Compare your measurement with sum of the two resistor currents.

   ![ParVot](/assets/Lab2-12.jpg)

5. ✏️ Use Ohm’s law to find the equivalent resistance of the two resistors in parallel (based on ideal value shown in the figure).
6. Disconnect the resistors from the power supply and use the DMM in Resistance mode to measure the resistance of the two resistors in parallel.
   - ✏️ Compare measured resistance with result from part 2.5

   ![ParRes](/assets/Lab2-11.png)

7. ✏️ Diagram the circuit and label all voltages and currents.
8. ✏️ Verify that each resistor follows [Ohm’s Law](https://youtu.be/8jB6hDUqN0Y?t=162). i.e. For each resistor, measure the voltage between the two ends and the current goes through it, then plug it into the formula.

## 3. [Series](/Lab2/information/series_vs_parallel.md) Resistors

1. Connect the 1000 Ohm and 500 Ohm resistors in series (connect only one end)

   ![SerConnect](/assets/Lab2-19.png)

2. [Set your DMM to current mode](/Lab1/dmm.md#measuring-current) and plug the red lead to A accordingly. Remember, you should start with the A port on the multimeter and switch to the mA/uA port for higher resolution **IF** the current measured with the A port is less than 400 milliamps.
3. ✏️ Open the circuit at three points and measure the current at each gap:

   - ✏️ Power supply ground connection

   ![SerCurrent1](/assets/Lab2-9.jpg)

   - ✏️ Connection between the two resistors

   ![SerCurrent2](/assets/Lab2-8.jpg)

   - ✏️ [Power supply positive connection](/Lab1/power_supply.md)

   ![SerCurrent3](/assets/Lab2-7.jpg)

4. ✏️ Use your DMM in Resistance mode to measure the resistance of the two series connected resistors.

   ![SerRes](/assets/Lab2-6.jpg)

   - ✏️ Diagram the circuit and label all (measured) voltages and currents.
   - ✏️ Verify that each resistor follows [Ohm's Law](https://youtu.be/8jB6hDUqN0Y?t=162).

## 4. Voltage Dividers

Voltage dividers are an important and useful circuit to scale a voltage (signal) by a factor between 0 and 1.0. The most famous application of voltage dividers is an audio volume control.

![DivLoad5](/assets/Lab2-22.png)

1. Connect 1000 Ohm and 500 Ohm resistors in series.
2. The 1000 Ohm resistor should [connect to +5V](/Lab1/power_supply.md), the 500 Ohm resistor should connect to GND
3. [✏️ Measure and record the voltage](/Lab1/dmm.md#measuring-voltage) between ground and:

   - ✏️ Ground (should be 0.0!!)

   ![DivVol1](/assets/Lab2-5.jpg)

   - ✏️ Junction between the two resistors

   ![DivVol2](/assets/Lab2-4.jpg)

   - ✏️ Compare voltage measured in 4.3.2 to prediction of voltage divider equation.
   - Power (should be 5.0V!!)

   ![DivVol3](/assets/Lab2-3.jpg)

4. Connect a second 1000 Ohm, “load” resistor between your voltage divider output (junction between 1000 + 500 Ohm resistors) and ground. Since the circuit is getting more complex, you should consider using a breadboard for this part. The [introduction to breadboarding article](information/breadboard.md) can get you started and the [series vs parallel article](series_vs_parallel.md) has examples.

   ![DivLoad4](/assets/Lab2-21.png)

   ![DivLoad1](/assets/Lab2-1.jpg)

5. [Measure current](/Lab1/dmm.md#measuring-current) in the load resistor and [voltage](/Lab1/dmm.md#measuring-voltage) across the load resistor. Remember, you should start with the A port on the multimeter and switch to the mA/uA port for higher resolution **IF** the current measured with the A port is less than 400 milliamps.

   - ✏️ Measure the current

   ![DivLoad2](/assets/Lab2-2.jpg)

   - ✏️ Measure the voltage

   ![DivLoad3](/assets/Lab2-18.jpg)

6. Explain why this voltage divider does not follow the 4.3.2 voltage prediction now that a load resistor has been added.

## 5. ESP32 - Blink a LED

1. Setup ESP32 with MicroPython

Before proceed with the steps below, make sure you have Thonny IDE and USB to UART bridge driver successfully installed, as well as MicroPython configured to ESP32 downloaded. 
- Thonny IDE download [link](https://thonny.org/)
- Check the dev board model, and download the USB to UART bridge driver. The link for CP210X is [here](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers). Install the driver on your laptop. You may have to change the laptop security setting to unblock extensions to successfully install it. The release note included in the installation package is a good resource for FAQ.
- Download latest and stable release of MicroPython firmware for ESP32. The link is here: https://micropython.org/download/ESP32_GENERIC/ We will use the downloaded file later, please make sure you can locate it later.

Let's now put things together.

- Connect ESP32 dev board with your laptop.
- Open Thonny IDE. Click on “Tools” → “Manage Plug-Ins”. Type in esptool in the search field as shown below. Depending on the operating system on your laptop, the figure may look different. Install esptool by clicking on it (in the red box).
![IntermediateStep-1](/assets/Lab2-25.png)
- Click on “Tools” → “Options” → “Interpreter”. Select MicroPython (ESP32) as the interpreter of Thonny. Select the option with USB to UART as the port. 
![IntermediateStep-2](/assets/Lab2-26.png)
- Click on “Install or update MicroPython (esptool)”. Click on the icon ≡. Choose the “Select local MicroPython image” option. Browse through your local files and find the MicroPython file downloaded before. 
- Click on button “Install”. You may have to push the boot button on the board to write to it.
- Copy and paste the following code line by line to the Shell window in Thonny.

```
>>> Import machine
>>> led = machine.Pin(2, machine.Pin.OUT)
>>> led.on()
```
What did you observe after entering the 3rd and 4th line? Add comments to the code based on your observation. Feel free to read the documentation or utilize other resources to understand this code implementation.

For Windows users, feel free to refer to this [tutorial](https://www.youtube.com/watch?si=JNdeSa-IPverrW2t&v=elBtWZ_fOZU&feature=youtu.be)




## 5. Arduino – [Blink a LED](/Lab2/information/flashing_code.md)

1. Open the ‘SIK Guide‘ book of your Arduino Starter Kit. Go to page 21 and finish Circuit 1 – ‘Blinking a LED’

   ![LED1](/assets/Lab2-20.png)

   - Note: if you do not have the book, you can use this [Arduino tutorial](https://www.arduino.cc/en/Tutorial/BuiltInExamples/Blink). This tutorial uses a different resistor value, but will work just as well.

2. ✏️ After you finish the circuit. **Ask a TA to check it.**

# Frequently Asked Questions

**Q: I hear the yellow DMM start beeping when I try to measure voltage or current.**

A: The beeping is a warning from DMM that your DMM setting does not match with the lead connected. For example, the pointer is on ‘V’ but the red lead is connected to ‘A’. Once you hear the beeping, please do not perform any measurement until you figure out the issue. Otherwise, the DMM may be damaged.

**Q: How can I use breadboards?**

A: Please refer to [this tutorial](https://www.sciencebuddies.org/science-fair-projects/references/how-to-use-a-breadboard) on using breadboards. [Here is another one](information/breadboard.md).

**Q: In 4.4, how can I add the load resistor and measure the current and voltage?**

A: The load resistor should be added in parallel with the 500 Ohm resistor, then you could measure the current and voltage as normal.
