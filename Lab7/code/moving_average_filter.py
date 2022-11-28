# -*- coding: utf-8 -*-
"""
UW GIX
Techin 512
Lab 7
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('trail_1.txt')

def moving_average_filter(signal, k):
    signal_pad = np.zeros(len(signal)+k)
    signal_pad[:k] = signal[0] #padding
    signal_pad[k:] = signal
    
    signal_filtered = np.zeros(len(signal))
    for i in range(0, len(signal)):
        signal_filtered[i] = np.mean(signal_pad[i:i+k])
    
    return signal_filtered

time = data[:,0]
ppg_reading = data[:,1]

ppg_reading_filtered_1 = moving_average_filter(signal = ppg_reading, k = 5)
ppg_reading_filtered_2 = moving_average_filter(signal = ppg_reading, k = 20)
ppg_reading_filtered_3 = moving_average_filter(signal = ppg_reading, k = 50)

plt.figure(figsize=(18,8))

plt.plot(time, ppg_reading, label = 'raw')
plt.plot(time, ppg_reading_filtered_1, label = 'k=5')
plt.plot(time, ppg_reading_filtered_2, label = 'k=20')
plt.plot(time, ppg_reading_filtered_3, label = 'k=50')


plt.grid()
plt.locator_params(nbins=40, axis='x')
plt.xlabel('Time (seconds)')
plt.ylabel('Sensor Reading')
plt.title('PPG - Moving average filter')
plt.legend()
plt.show()