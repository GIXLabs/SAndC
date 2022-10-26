Strain Gage / Load Cell

Introduction
The purpose of this lab is to learn about measurement of Force and Strain. We will learn about ideal and non-ideal behavior of practical force sensors. Measuring force is most often used to measure weight (the force of gravity developed by a Mass).

Background
Key terms:

Strain size deformation of a material. Often expressed:
Strain = 𝜺 (epsilon) = ΔL / L
(note the units (mm, inch etc) cancel out! Strain has no units (it’s “dimensionless”)
For strong materials like metal, strain is very small, like 10-5

Stress force per unit area.
Stress = σ= F/A (sigma)
(units of stress are Pascals or pounds-per-square-inch, PSI)

Under some conditions, strain is proportional to stress by the simple equation:
ϵ= E σ
(Hooke’s Law). E is Young’s modulus. Most Force/Weight sensors exploit this by measuring strain and calibrating it to stress -✏️ Force. If the stress or strain is too big, the material might crack or deform, breaking this relationship (so be gentle with strain gages and load cells!).

We will learn about two sensors:

Strain gage: a sensor which can measure very small strains on a surface. As the gage is stretched, its resistance will change.
Load Cell: a metal structure which has a linear relationship between stress and strain so that it follows Hooke’s Law. A strain gage is applied to the surface of a load cell.

Resistive Heating
We have from Ohm’s Law: V=IR. We also know that power is: P =IV. From this we can easily get P= I2R. Power in a resistor converts directly to heat and heat converts to temperature. Thus any resistor will heat up more and more as power is increased. Strain gages are resistors. One thing we will study in this lab is how strain gages respond to changes in temperature.

[StrainGaugeLoadCellBackground.pdf] This material (From Prof. Hannaford’s EE543 course notes) goes into more depth and detail on load cell design.
[ Sparkfun Tutorial ] Detailed info on hooking up a bridge-based load cell to Arduino
[instructables] Similar tutorial.

Preparation:
Pre-lab computations:
None but see Computer Preparation below

Computer Preparation
Make sure your laptop can do Arduino development (one such laptop per lab bench team).
Install the HX711 chip library [HX711_Library.zip] ( Library installation help ) or go to https://www.arduino.cc/reference/en/libraries/hx711-arduino-library/

Parts, tools, supplies required:
Strain gage [Ebay Part]
Simplistic “Diving Board” load cell
5Kg load cell [Ebay Link]
Load Cell A to D-SPI interface (HX711) chip:
Load Cell mounting base (supplied by GIX).
Test Weight Set
DMM with Type K thermocouple plug
Power Supply
Cup of ice cubes, Heat gun, Soldering iron
Arduino, USB cable
[HX711_driver_TECHIN512_GIX_rev01.ino ] Prepare Arduino code
HX711 chip Arduino driver (software, see below)

Procedure:

Strain Gage Measurements
In this section you will study the resistance of the individual strain gage and its sensitivity to temperature.

Resistance temperature sensitivity. We will use the resistance of the strain gage to heat it up a little bit and then see how much the resistance changes.
Set power supply to 2.0V. (set current limit to about 200mA)
Set up the Bench-Top DMM (not the Fluke yellow hand held DMMs) to measure current. Using “LO” and “mA” inputs, connect it in series with the strain gage and the power supply.
Using the button labeled “Rate”, set the Bench-DMM to “slow” -- this means it will average several readings to get more accuracy (5 ½ digits!!!). Record all 5 digits from the DMM in “slow” mode. If the last digit is flickering between two values, split the difference .. example: 1.4297{3 / 4} ---✏️ 1.429735
Read current from the DMM.
✏️ What is the voltage, V (assume the power supply is accurate), and current, I? ✏️Compute the resistance? (R=V/I). ✏️ What is the power dissipated in the strain gage? (P = I*V or P=I2R).
Change power supply voltage to +5V Wait for 3 minutes.
✏️ Measure/compute R = V/I. ✏️What is resistance? ✏️ Did it change?
✏️ Compute the power dissipated in the strain gage resistance
Reduce voltage to 1.0V. Wait 3 minutes. During this time, predict the current using both values of resistance.
✏️ record current and compute resistance after 3 min of cooling.
Delta-R vs cold (ice cube)
In this section, we will study how resistance of the gage ( ) changes with temperature.
Place the strain gage (not the diving board) on several sheets of paper or a notebook (thermal insulation from the desk).
Set power supply to 1.0 V, ✏️ measure current / compute resistance.
Apply an ice cube to the gage. Use a plastic bag or some other methods to apply ice, in order to prevent direct contact. Water may affect measurement. ✏️ What is change in resistance?
Use temperature attachment (type “K” thermocouple) with yellow Fluke DMM to ✏️ measure room temperature. Then, ✏️ press your finger on the tip of the thermocouple and record temperature.
Assume the ice is approximately 0 deg C ✏️ Cycle the gage 5 times between 0C and room temperature. Record resistance at each temperature for each cycle. Average your results at each temperature.
✏️ Compute coefficient of thermal resistivity:
 G = ΔR/ΔT

Strain Gage “Diving Board”


The diving board is a simplistic load cell with a single strain gage. We’ll measure its sensitivity to strain and temperature. The strain gage is the same type (nominal resistance 350 Ohm) but it is glued to a beam of acrylic material.
Hook up the diving board leads to the bench-top DMM the same way as in part 1. Set the DMM to “slow” for maximum accuracy. Using 2.0V from the power supply, ✏️ compute and record the resistance.
Stretch the gage by gently pressing down on the end of the diving board until it touches the base. ✏️ compute and record resistance when gage is deflected.
Release the “diving board”
Set heat gun switch to “Low” and verify that it is blowing room temperature air.
Blow room temperature air on the “diving board” strain gage for 1 min. ✏️ compute and record resistance without touching the gage.
Tape Type K thermocouple onto diving board near the strain gage (leave tip out in open air just above strain gage).
Set the heat-gun to high. From a distance of 12” (50cm), heat the strain gage with the heat gun for 15 seconds (DO NOT APPLY HEAT CLOSER THAN 12” / 50cm!! or you WILL damage the strain gage.) ✏️ Record hot air temperature from DMM.
✏️ compute and record resistance when gage is heated (but not pushed or deformed).



	Load Cell Measurements
Finally we will study a weight measurement system consisting of a load cell mounted between two platforms.
	Plug an Arduino into your prepared laptop.
	Using male-to-female proto-board hookup wires, connect Arduino with load cell HX711 chip via SPi according to

	Download and run pre-written sketch [HX711_driver_TECHIN512_GIX_rev01.ino] which can:
	Read load cell , type sensor reading on Laptop Screen (terminal)
	Repeat
	Calibrate the load cell (shown at right with top platform removed for clarity) with weight set:
	Apply 1 g, 10g, 100g to the center target on the TOP platform.
	✏️ record load cell reading at each weight. Use each weight 3 times and average the results.
	✏️ Using a spreadsheet, or graph paper, fit a linear equation to your calibration data and add it to the Arduino sketch so that the Arduino prints grams on your laptop.
	✏️ record calibrated reading for each weight. Verify your calibration.
	Apply the 100g weight to each target on the top platform in turn. What is the variation in weight measured due to location??
	Temperature Sensitivity
	Place a weight between 100-500 grams on your platform. Record the weight reading at room temperature.
	Place the type K thermocouple tip inside the two holes in the load cell beam.
	Set the heat-gun to high. From a distance of 12” (50cm), heat the strain gage with the heat gun for 15 seconds (DO NOT APPLY HEAT CLOSER THAN 12” / 50cm!! or you WILL damage the strain gage.) ✏️ Record hot air temperature from DMM.
	✏️ Record the weight reading and air temperature.
	✏️ Remove heat gun. How long does for weight reading to return to within 1% of the value read in step “a.” above? (Some of the strain gauges’ reading may not return to 1%. In this case, wait until the reading is stable and record the stable value)



Write-Up
 [ same instructions as previous TECHIN 512 labs ]
