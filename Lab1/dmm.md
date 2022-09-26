# Using the Fluke Digital Multimeter (Yellow)
## Reading Voltage
First prop the multimeter up so it is a little easier to read. Plug in probes (see below) to the two sockets on the bottom right of the multimeter. The red one should go in the far right, which is marked with a few symbols (temperature, voltage, current, and transistor). The black one should go in the port marked COM (short for common).

![Plugging in Cables](assets/DMMVoltWiring.gif)

**Best Practice Note:** Although the probes are the same, it is a good practice to use black for ground or common lines and red for lines at a positive voltage.

Rotate the knob on the front of the multimeter twice clockwise from the OFF position. It should be on the V with a couple of lines above it, which indicates you want to measure DC voltage.

![Switching to DC Voltage](assets/DMMVolt.gif)

Apply the probes in parallel with your circuit and read the voltage from the display on the multimeter. In the above clip, we are reading the voltage from a benchtop power supply, but the probes can be applied to other test points in your circuits.

**Note:** If you apply the black probe to the positive voltage in your circuit, the voltage displayed on the multimeter may be negative. Switch the position of your probes to get a correct reading.

**Safety Note:** Be careful with the placement of your probes. The tips of your probes conduct electricity, which is obvious, but the implications are not. If your tip connects two parts of your circuit that should not be connected, you can end up frying components. This is especially tricky when working with small components.

## Reading Current
To measure current, the multimeter must be placed in series with the circuit you hope to measure. This means that the current will flow through the multimeter. As a result, you can damage your multimeter if you allow too much current to flow through it.

First, the red probe to the socket on the bottom left of the multimeter marked A. This can measure currents up to 10 Amps and is the one you should use most often.

![Wire for Current](assets/DMMCurrent.gif)

Then you should rotate the knob until it points to the option mA and press the yellow button in the top left to switch to DC. These two steps are shown in the clip above.

Here is an example where the power supply is set to 10V and passed through a 1k Ohm resistor using the A setting.

![A Setting](assets/DMMCurrentExA.gif)

Since the current was below 400 mA, we can get finer resolution by switching to the mA port.
![mA Setting](assets/DMMCurrentExmA.gif)
