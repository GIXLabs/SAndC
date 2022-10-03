# Flashing Code to an Arduino

When working with microcontrollers, flashing code is the process of transferring the code you've written in the IDE on your computer to the microcontroller you're writing it for. For this tutorial you will need:

- An Arduino Uno
- A USB A-to-B cable
- [The Arduino IDE](https://www.arduino.cc/en/software)

## 

1. Download and install the Arduino IDE from the link above. Open the software and you should see something like the following:
![Arduino IDE](/assets/general_knowledge/arduino_ide.png)

2. Connect your Arduino to your laptop.
![Connect board](/assets/general_knowledge/arduino_connect.jpg)

3. Select which type of Arduino board you have connected. My dropdown menu will have a few more options than the default as I've installed a few 3rd party boards. Go ahead and select Arduino Uno.
![Select board](/assets/general_knowledge/arduino_select_board.png)

4. Select the COM port that the Arduino is connected to. The software should do a pretty good job of prompting you as to which one it is. 
![Select port](/assets/general_knowledge/arduino_select_com_port.png)

5. Programs in Arduino are referred to as sketches. Either open a pre-written or write your own sketch. Click the verify button in the top left of the UI. It should take a few moments to compile and then produce an output at the bottom of the UI. If it says, "Done compiling" then you're ready to load the sketch onto the board. If it spits out an error, it should give you a hint as to where the error is via some orange text at the bottom of the window. 
![Verify sketch](/assets/general_knowledge/arduino_verify.png)

6. Click the upload button to the right of the verify button. If it says "Done uploading" then you're good to go. If you get an error but the program compiled correctly on the previous step, you likely have the incorrect board or port selected.
![Upload sketch](/assets/general_knowledge/arduino_upload.png)