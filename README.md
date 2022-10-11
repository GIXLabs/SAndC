# TECHIN 512: Sensors and Circuits
This repository contains class content for TECHIN 512, the Sensors and Circuits class for students at GIX at the University of Washington getting their Masters of Science in Technology Innovation.

In addition to assignments, it hosts some how to content on using electronics test equipment, like benchtop power supplies, oscilloscopes, digital multimeters (DMM), and more.

## Table of Contents
 - Lab 1: [Instrument Familiarization](Lab1/README.md)
 - Lab 2: [DC Circuits and Voltage Dividers Lab](Lab2/README.md)
 - Lab 3: [BJT Timer Circuit](Lab3/README.md)

## General Tips
 1. Make sure to read the safety manual carefully. Safety is always the No.1 Priority.
2. **Always check the resistance of each resistor before use.** You probably do not want to debug for a long time about wiring only to find there is a wrong resistor. Although there are labels on the boxes, the resistors inside may be returned by mistake. **If you are unsure about the resistors when you finish labs, please discard and do not return them.**
3. Be careful when measuring current. Mistakes in measuring current can burn the fuse of the DMM. **When you are going to measure current but make no change to the circuit, it is wrong.** Measuring current always requires disconnecting somewhere in your circuit and ‘inserting’ the DMM in between. And always change the mode of DMM back to ‘voltage’ after you measure current. This can efficiently prevent forgetting the mode of DMM and measure voltage in the current mode in your next use, and thus burn the fuse.
4. **All the GNDs of your circuit, DMM, Arduino and oscilloscope probes should be connected together.** This is called common ground.

5. Pay attention to the ‘1X’ and ‘10X’ mode of your oscilloscope setting and the probes. If the measurement your get is around 10 times larger or smaller then you expect, it is probably that the scale of your oscilloscope and probes do not match.
