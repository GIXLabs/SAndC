# Final Project Take-Home Assignment 2

## Goals
The objectives of this assignment are:
- Learn how to setup Circuitpython on your microcontroller
- Installing Circuitpython libraries
- Interfacing with SSD1306 OLED Screen
- Interfacing with the Rotary encoder
- Interfacing with ADXL345 Accelerometer

## Setting up Circuitpython

To install Circuitpython on your microcontroller go to this [website](https://circuitpython.org/downloads). In the search bar type in the microcontroller you are using, in this case it is Xiao ESP32C3. 

![Circuitpython Xiao](assets/CircuitpythonXiao.svg)

Connect your Xiao ESP32C3 to your computer and click on OPEN INSTALLER. Follow the directions until you have successfully installed Circuitpython on your ESP32. If you are having difficulties installing Circuitpython using the web installer, download the .BIN file and follow the instructions [here.](https://learn.adafruit.com/circuitpython-with-esp32-quick-start/web-serial-esptool)

Verify that you have successfully installed Circuitpython by opening Thonny and checking if it recognizes your board. Be sure to check if your Thonny interpreter is set to Circuitpython and you have selected your board's COM port. You'll know if Thonny recognizes your board if in the bottom right corner it has the COM port associated with your ESP32 and if in the shell you see >>> in blue text like the image below. You might have to click the Red Stop button at the top to get Thonny to successfully connect to your board.

![Thonny Successful Connection](assets/ThonnyConnect.svg)

## Installing Circuitpython Libraries

Adafruit maintains a majority of the libraries for Circuitpython that can be downloaded [here.](https://circuitpython.org/libraries) On the library download page be sure to select the bundle pack that matches the version of Circuitpython that you installed.

![Circuitpython Libraries](assets/CircuitpythonLibraries.svg)

Once you have downloaded the zip file for the library bundle, extract the contents to somewhere you will remember on your computer.

