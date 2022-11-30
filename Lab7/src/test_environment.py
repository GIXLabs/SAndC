# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 10:43:51 2021

@author: 75678
"""

import numpy as np
import matplotlib.pyplot as plt
import filters
import serial


x = np.linspace(0, 6*np.pi, 2000)
sin_wave = np.sin(x)
sin_wave_noised = sin_wave + 0.1 * np.random.normal(loc=0.0, scale=1.0, size=len(sin_wave))

sin_wave_filtered = filters.moving_average_filter(signal = sin_wave_noised, k=20)

fig = plt.figure()
plt.subplot(211)
plt.plot(x, sin_wave_noised)

plt.subplot(212)
plt.plot(x, sin_wave_filtered)
plt.show()
