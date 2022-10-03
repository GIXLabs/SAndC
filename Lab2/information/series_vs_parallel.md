# Series vs. Parallel

There are 2 basic ways to connect more than two components in an electric circuit: in series or parallel.

## Series

In a series circuit, components are connected end to end to form a single chain where there is one path for electrons to flow. If we were to connect 3 resistors (R1, R2, and R3) in series to a power supply, we would get the following schematic and breadboard:
![Series schematic](/assets/general_knowledge/series_schematic.png)
![Series breadboard](/assets/general_knowledge/series_breadboard.jpg)

## Parallel

In a parallel circuit, components are connected so that each one is joined to a common node on each side. Instead of the electrons flowing through a single path, they now have 3 distinct paths in which current may flow.
![Parallel schematic](/assets/general_knowledge/parallel_schematic.png)
![Parallel breadboard](/assets/general_knowledge/parallel_breadboard.jpg)

## Series-Parallel

In the real world, circuits are often a mix of series and parallel components. In this example, R2 and R3 are connected in parallel to each other and the two of them are connected in series to R1.
![Series-parallel schematic](/assets/general_knowledge/series_parallel_schematic.png)
![Series-parallel breadboard](/assets/general_knowledge/series_parallel_breadboard.jpg)

## Series vs. Parallel Effect on Resistance

Let's assign some resistor values to the schematics shown above in order to more easily understand how the different methods affect voltage and current. For the explanations below, R<sub>1</sub>=100Ω, R<sub>2</sub>=200Ω, and R<sub>3</sub>=300Ω. The power supply has a voltage of 5V.

### Series

In a series circuit, the current throughout each resistor is the same and the voltage drop across each resistor is proportional to its value compared to the total equivalent resistance. The total equivalent resistance is equal to the sum of the resistors. R<sub>equivalent</sub> = R<sub>1</sub> + R<sub>2</sub> + R<sub>3</sub> = 100 + 200 + 300 = 600Ω.

The current across each resistor is constant and follows Ohm's law. I = V/R<sub>equivalent</sub> = 5/600 = .00833A or 8.33mA.

The voltage drop across each resistor is proportional to its value compared to the total equivalent resistance.
V<sub>resistor</sub> = V<sub>total</sub> _ (R<sub>resistor</sub>/R<sub>equivalent</sub>)
Voltage drop across R<sub>1</sub> = 5 _ (100 / 600) = 0.83V.
Voltage drop across R<sub>2</sub> = 5 _ (200 / 600) = 1.67V.
Voltage drop across R<sub>3</sub> = 5 _ (300 / 600) = 2.5V.

If we sum these voltages up we see that we get our total voltage drop. 0.83 + 1.67 + 2.5 = 5V

We could also use Ohm's to figure out the voltage drop across any given resistor once we calculate the current throughout the circuit. For example:
Voltage drop acros R<sub>2</sub> = V<sub>R2</sub> = IR<sub>2</sub> = 0.00833 \* 200 = 1.67V.

### Parallel

In a parallel circuit, the voltage drop across each resistor is the same and the current throughout each one differs. The inverse of the total equivalent resistance of two or more resistors connected in parallel is the algebraic sum of the inverses of the individual resistances.
1/R<sub>equivalent</sub> = 1/R<sub>1</sub> + 1/R<sub>2</sub> + 1/R<sub>3</sub> = 1/100 + 1/200 + 1/300 = 0.0183
R<sub>equivalent = 1 / 0.0183 = 54.54Ω.

The total current I<sub>Total</sub> entering into the parallel resistor circuit follows Ohm's law. I<sub>Total</sub> = V/R<sub>equivalent</equivalent> = 5/54.54 = .0917A or 91.7mA.

The current flowing through each resistor is not constant but again we can use Ohm's law to find I<sub>R1</sub>, I<sub>R2</sub>, and I<sub>R3</sub>.
I<sub>R1</sub> = V/R<sub>1</sub> = 5/100 = .05A
I<sub>R2</sub> = V/R<sub>2</sub> = 5/200 = .025A
I<sub>R3</sub> = V/R<sub>3</sub> = 5/300 = .0167A

We could have also gotten to I<sub>Total</sub> by summing I<sub>R1</sub>, I<sub>R2</sub>, and I<sub>R3</sub>. .05+.025+.0167 = .0917A.

### Series-Parallel

When working with a mix of series and parallel resistors, we find the equivalent resistance of each subsection of the circuit in order to create a simplified abstraction of it. In the example above, R2 and R3 are in parallel. They are connected in series with R1. We will find the equivalent resistance of R2 and R3 and then imagine that that new resistor value is a single resistor in series with R1.

1/R<sub>equiv</sub> = 1/R2 + 1/R3 = 1/200 + 1/300 = .00833
R<sub>equiv</sub> = 1/.00833 = 120Ω.

So now we have R<sub>1</sub> and R<sub>equiv</sub> in series. R<sub>Total</sub> = R<sub>1</sub> + R<sub>equiv</sub> = 100 + 120 = 220Ω.

The current through R1 and into the parallel resistors is I = V/R<sub>Total</sub> = 5/220 = .0227A or 22.7mA.
We can calculate the voltage drop across R1 using Ohm's law: V<sub>R1</sub> = I*R<sub>1</sub> = .0227 * 100 = 2.27V.
We could also calculate it as a proportion of total resistance: V<sub>R1</sub> = V<sub>Total</sub> _ R<sub>1</sub>/R<sub>Total</sub> = 5 _ 100/220 = 2.27V.

The voltage drop will be the same across R2 and R3. V<sub>equiv</sub> = V<sub>Total</sub> _ R<sub>equiv</sub>/R<sub>Total</sub> = 5 _ 120/220 = 2.73V.
The current through each resistor can be calculated via Ohm's law.
I<sub>R2</sub> = V<sub>equiv</sub> / R<sub>2</sub> = 2.73/200 = .0136A.
I<sub>R3</sub> = V<sub>equiv</sub> / R<sub>2</sub> = 2.73/300 = .0091A.

Just for posterity's sake we can double check that .0136 + .0091 = .0227A which was the current flowing into the node.
