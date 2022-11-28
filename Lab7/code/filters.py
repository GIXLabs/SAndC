# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 17:49:45 2021

@author: 75678
"""

import numpy as np


def moving_average_filter(signal, k):
    signal_pad = np.zeros(len(signal)+k)
    signal_pad[:k] = signal[0] #padding
    signal_pad[k:] = signal
    
    signal_filtered = np.zeros(len(signal))
    for i in range(0, len(signal)):
        signal_filtered[i] = np.mean(signal_pad[i:i+k])
    
    return signal_filtered
    