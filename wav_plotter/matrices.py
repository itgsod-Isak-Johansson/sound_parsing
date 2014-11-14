__author__ = 'thedoctor'

import numpy as np

def time_amplitude(data, rate):
    time = np.arange(len(data))*1.0/rate
    return time

def frequency_power(data, rate):
    power = 20*np.log10(np.abs(np.fft.rfft(data)))
    frequency = np.linspace(0, rate/2, len(power))
    return frequency, power

def find_frequency_of_highest_power_value(frequency, power):
    max_y = max(power)
    max_x = frequency[power.argmax()]
    return max_x, max_y
