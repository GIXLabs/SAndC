# Introduction

The purpose of this lab is to learn about measurement of photoplethysmogram (PPG) using pulse oximeter. We will learn about driving a pulse oximeter using Arduino, and using Python serial reader to receive the signal at PC. We will also use filters to reduce the noise and study the affect of the filters on the signal.

# Background

1. A photoplethysmogram (PPG) is an optically obtained plethysmogram that can be used to detect blood volume changes in the microvascular bed of tissue. A PPG is often obtained by using a pulse oximeter which illuminates the skin and measures changes in light absorption. A conventional pulse oximeter monitors the perfusion of blood to the dermis and subcutaneous tissue of the skin

   For more details, please see [Wikipedia – Photoplethysmogram](<https://en.wikipedia.org/wiki/Photoplethysmogram#:~:text=A%20photoplethysmogram%20(PPG)%20is%20an,measures%20changes%20in%20light%20absorption.>).

![UW pulse oximeter](assets/UW_pulse_oximeter.png)

2. Low pass filters can help with reducing the noise in the signals of sensors. Low pass filters exist in many different forms. For hardware side, as introduced in Lab 3, an RC circuit can be used as a low pass filter when output is connected to the capacitor. In this lab, we will look at the software side where filters are applied by code and algorithms.

3. Moving average filter is applied by the average of several previous data points. As Fig.3 shows, each point of the filtered signal is the average of k previous near points in the original signal.

   For more details, please see [Wikipedia- Moving average](https://en.wikipedia.org/wiki/Moving_average#Other_weightings).

![Moving Average Example](assets/moving_average_ex.png)

4. Exponential decay filter (also called exponential smoothing) is a rule of thumb method to filter out noise in time series signals. It can be implemented by the following equation:

   S*k=αx_k+(1-α)S*(k-1)

   where S is the filtered signal, x is the original signal and is the exponential factor. For more details, please see [Wikipedia - Exponential smoothing](https://en.wikipedia.org/wiki/Exponential_smoothing).

# Preparation:

Pre-lab computations:

- None but see Computer Preparation below

# Computer Preparation

We will use Python for signal process in this Lab. If you are not familiar with Python, please follow the steps to prepare Python workspace. Detailed instruction on Python is beyond the scope of this lab, but it is recommended to explore more on Python, as it can be very useful in your future courses.

For more information on setting up Anaconda and Spyder click [here](/Lab6/anaconda.md).

## Parts, tools, supplies required:

- Arduino
- Pulse Oximeter sensor

![PPG Sensor](assets/ppg_sensor.png)

- Source code (src) folder

# Procedure:

All the code in this Lab is provided in the 'src' folder, but you are welcome to write you own code for any part of this lab.

1. **Setup hardware**

   1. Connect Arduino to your PC.
   2. Connect the pulse oximeter sensor to Arduino, red pin to 3.3V, black pin to GND and purple pin to Analog input **A0** by default.
      ![Arduino Connections](assets/arduino_conn.svg)

2. **Install and Upload Arduino Script**

   - [Install Library PulseSensor](https://pulsesensor.com/pages/installing-our-playground-for-pulsesensor-arduino)

   - [Pulse Sensor Code and Guide](https://pulsesensor.com/pages/code-and-guide)

## Test the sensor

1.  Use two fingers to hold the sensor or use tape to fix the sensor on one of your fingers or on your ear. Make sure the front side of the sensor is touching your skin.
2.  In Arduino IDE, go to 'Tools-Serial Plotter', if everything is set correctly, you should see similar plots as the following figure and a yellow LED on your Arduino blinking on your heartbeat. Make sure the baud rate is **57600**. If you see that signal reaches the upper limit 1000 or the peak is not obvious, you may need to adjust the pressure applied on the sensor.

![Serial Plotter Example](assets/serial_plotter_ex.png)

3. ✏️ Take a photo of your sensor setup and a screenshot of the serial plotter.

## Record data on your PC

- Open Spyder, make sure the virtual environment is correct.

![Spyder Enviroment Check](assets/spyder_env_check.png)

- In Spyder, open the file [serial_reader_PPG.py](src/serial_reader_PPG.py). You may need to change the serial setting, as shown in the following figure.

![Spyder Com Port Check](assets/change_com.png)

- Run the Python script, make sure the sensor is correctly placed on your skin. It will record the raw PPG sensor reading for 10s. The data will be saved as a '.txt' file in the same folder of '**serial_reader_PPG.py**'.

![Text Output File](assets/text_output_file.png)

- If the recording is successful, you can see a plot pop up as the following figure shows.

![PPG Data](assets/filtered_data.png)

- ✏️ Take a screenshot of this figure.
- Repeat this step to record 1 trail for each member in your group. Make sure to change the file name in the script. Otherwise, it will overwrite existed files.

![Change filename](assets/change_filename.png)

- If you find any of the following error, just close the current Console and run again.

![Python error 1](assets/python_error1.png)

![Python error 2](assets/python_error2.png)

![Python error 3](assets/python_error3.png)

- In medical practice, data such as PPG or ECG are usually considered as the private of patients. So you are also welcome to use anonymous recording in this lab, for example, by writing '**member 1**' instead of your name.

## Filter the noise using moving average
1. In Spyder, open [moving_average_filter.py](src/moving_average_filter.py), enter the file name of your recorded data.

   ![Moving Average Filter](assets/moving_average_filter.png)

  1. Run this script, a figure should pop up.
  1. ✏️ Take a screenshot of the figure and describe what you find when applying moving average and with different window size k. You can use '**Zoom**' button to Zoom in and get a better observation.

   ![Zooming in](assets/zoom_in.png)

  1. Repeat the steps for each trail you just recorded.
1. Filter the noise using exponential decay
   1. In Spyder, open [exponential_decay_filter.py](src/exponential_decay_filter.py), enter the file name of your recorded data.
   1. Run this script, a figure should pop up.
   1. ✏️ Take a screen shot of the figure and describe what you find when applying moving average and with different exponential factor .
   1. Repeat the steps for each trail you just recorded.

## Estimate your heart rate

1. In Spyder, open [heart_rate_estimate.py](src/heart_rate_estimate.py), enter the file name of your recorded data.
1. Run this script, a figure should pop up and show the filtered signal by exponential decay.
1. You can check the coordinates of the peaks by pointing your cursor on the peak and the coordinate is on the top right corner.

   ![Heart Rate Estimation 1](assets/estimate_heart_rate1.png)

1. Find the time interval between 2 peaks, as the following figure shows. Repeat for 5 times and calculate the average of t.

   ![Heart Rate Estimation 2](assets/estimate_heart_rate2.png)

## Estimate your heart rate by:

hr = 60 / t

1. ✏️ Write down the heart rate for each member of your group.
1. Do some exercises, such as jumping jacks. Then take measurement again and estimate your heart rate, by repeating step 4 and 7. Your need to be quick as your heart rate may recover soon.
1. ✏️ Write down the heart rate after exercises and compare with the heart rate before exercises.
1. (verify the result by counting on pluses on wrist)

# Write-Up

The writeup for this lab should contain the following outline:

1. Title page (see template in the folder ‘Requirement of Lab Reports’)
2. Introduction
   ⅓ of a page describing the purpose and goals of this lab in your own words. Do not reproduce any material from this assignment document in any section of your writeup.
3. Results
   Each location in the instructions below marked with “✏️” indicates some data which must appear in your report.