# Solderless Breadboards

![breadboard](/assets/general_knowledge/breadboard.jpg)

Solderless breadboards, normally just referred to as breadboards, are tools to quickly prototype electronic circuits. They allow you to make electrical connections by inserting your components into a grid of holes which are electrically connected to one another. 

## How is a Breadboard Connected?

Behind the plastic exterior of the breadboard, there are a series of metallic strips that connect the various holes to each other. Breadboards are connected along their rows, usually with a split in the middle to accomodate integrated circuits (more on that later). Medium and larger sized breadboards will also have a connection down their columns at the edges to be used as a power rail. The picture below illustrates what holes are connected to each other in a medium sized breadboard. 

![breadboard](/assets/general_knowledge/breadboard_connections.jpg)

## Making Connections

To make a connection, insert the lead of your component into a hole and press down until you feel it make solid contact with the bottom of the breadboard. There should be a slight amount of resistance as you first insert the lead to let you know that the connection is solid.

![first connection](/assets/general_knowledge/breadboard_first_connection.gif)

Continue with this process until you've completed your circuit.

![simple circuit](/assets/general_knowledge/simple_circuit_connection.gif)

### Jumper Wires

When working with breadboards you'll quickly find that it would be helpful to connect components on different rows together. This is accomplished via jumper cables. These simply provide a direct connection between any two points. You'll use "male-to-male" connectors to make connections between holes on the boards but there are also "male-to-female" and "female-to-female" connectors where one or both sides of the wires are receptacles.

![jumper wire](/assets/general_knowledge/breadboard_jumper_wire.gif)

### Integrated Circuits

Integrated circuits should be placed so that they span the channel that divides the breadboard this is done in order to not short the pins across a row.

![breadboard with ic](/assets/general_knowledge/breadboard_ic.jpg)

### Connecting Components With Narrow Leads

There are various components that do not directly plug in to breadboards. You might have a surface mount integrated circuit and use an [SOIC to DIP adapter](https://www.adafruit.com/product/1283) or use a [screw terminal](https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/691137710002/6644051) to ensure that the connection to some narrow leads are secure. For the purposes of Sensors and Circuits, you'll be able to get by through a combination of jumper wires and alligator clips.

![narrow leads](/assets/general_knowledge/breadboard_narrow_leads.gif)

