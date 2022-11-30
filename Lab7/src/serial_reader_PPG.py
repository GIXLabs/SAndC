# -*- coding: utf-8 -*-
"""
UW GIX
Techin 512
Lab 7
"""

import serial
import time
import numpy as np
import matplotlib.pyplot as plt

file_name = 'trail_2.txt'
record_time = 10 # length of the trail in second

# set up the serial line
ser = serial.Serial('COM12', 57600)
time.sleep(3)


start_time = time.time()
# Read and record the data
data =[]                       # empty list to store the data
while time.time() - start_time < record_time:
    b = ser.readline()         # read a byte string
    string_n = b.decode()      # decode byte string into Unicode
    string = string_n.rstrip() # remove \n and \r

    try:
        ppg = float(string)    # convert string to float
    except:
        continue

    time_cur = time.time() - start_time
    new_line = [time_cur, ppg]
    print('Time: ' + str(time_cur))


    data.append(new_line)           # add to the end of data list

ser.close()

data_array = np.array(data)
print('Record ended, data shape: ' + str(data_array.shape))
print('Data saved at:' + file_name)
np.savetxt(file_name, data_array)


plt.figure(1, figsize=(18,8))
plt.plot(data_array[:,0],data_array[:,1])
plt.xlabel('Time (seconds)')
plt.ylabel('Sensor Reading')
plt.title('PPG')
plt.show()
