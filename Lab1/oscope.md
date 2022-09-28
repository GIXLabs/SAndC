# Using an Oscilloscope
Oscilloscopes (often called just 'scopes) can also help you debug your circuit. They can be used to make sure one of your peripheral devices is talking to the main microcontroller like you expect, check that your PWM signals are correct, check for fluctuations in your power supply, and much more.

The way it does all of these things is by plotting voltage over time, which turns out to be surprisingly helpful.

## Turning on the Oscilloscope
There is a power socket on the back for a power cable, much like that on the benchtop power supply. Once you have plugged that in, press the power button in the bottom left corner of the oscilloscope. The oscilloscope takes a minute or two to boot up.

## Connecting Probes
Once the oscilloscope is on, you should connect your probe(s) to the BNC connectors along the bottom. When positioned right, they slide in without effort and twist to lock in place. **Please be gentle with your probes.** They are precision instruments and should be treated that way.

![Attaching BNC](/assets/OscBNC.gif)

Many probes come with an option to reduce the voltage of the incoming signal to reduce the chance of damaging the oscilloscope. To activate that feature, slide the switch on the probe to "10X."

![Sliding 10X](/assets/Osc10XProbe.gif)

You will also need to tell the oscilloscope that you are using a 10x probe by pressing the colored button for the probe and then following the buttons on screen.

![Configuring 10X](/assets/Osc10XOsc.gif)

## Calibrating Oscilloscope Probes
Clip the probe and ground to their appropriate hooks on the bottom right side of the oscilloscope.

![Hooking to Calibration](/assets/OscCalConn.gif)

Using a flat-head screwdriver, adjust the screw until the wave has a square top. You may need to press the Autoset button if you do not see the signal and you may need to scale the display so you can see the wave better (see Adjusting the Display section for more details).

![Adjusting Calibration](/assets/OscCalScrew.gif)

## Adjusting the Display
### Horizontal Position and Scaling
The horizontal axis is the time axis and is shared by all of your signals (probes). The time between lines is indicated on the screen. You can change this by adjusting the scaling knob. You can also change what part of the signal you are looking at by rotating the position knob.

![Horizontal](/assets/OscHori.gif)

### Vertical Position and Scaling
The vertical axis shows voltage and can be adjusted independently for each signal (probe). Like the horizontal axis, you can adjust the scaling and the position of the signal on the display.

![Vertical](/assets/OscVert.gif)

## Investigating a Circuit
In this example, we have a signal generator set with a 100kHz ramp waveform, 2.5V maximum, and 0.0V minimum. Using BNC to clip connector to send the signal through a 47 Ohm resistor.

Please note that the black ground clip on the probe is connected to one side of the resistor and the main probe is connected to the other side. The black clip should always be connected to a ground in your circuit (such as the negative side of the battery).

![Investigating Circuit](/assets/OscInCircuit.gif)


## Measuring Voltage
Frequently, you will want to know how to measure voltages on your oscilloscope. Although you might be able to count tick marks to measure voltage, there is an easier way.

To measure voltage, you will need to add measurements through the "Measure" button. After pressing the button, you should start by removing all of the current measurements. After that, scroll through the measurement options and add Max and Min. See the gif below for more details.

![Measuring Voltage](/assets/OscMeasure.gif)

## Going Further
Sparkfun has an excellent tutorial on getting started with oscilloscopes [here.](https://learn.sparkfun.com/tutorials/how-to-use-an-oscilloscope/all)
