__author__ = 'thedoctor'

import sys
sys.path.append('../')
from wave_file import open_file, handle_channel_input
from plot import frequency_power_plot, time_amplitude_plot
from matrices import time_amplitude, find_frequency_of_highest_power_value, frequency_power


class Main:

    version = '0.1'

    def __init__(self, file_name_path, plot1, plot2):
        self.file_name_path = file_name_path
        self.plot1 = plot1
        self.plot2 = plot2

    def class_manager(self):

        #open wave file
        data, rate = open_file(self.file_name_path)
        #handle mono and stereo wave files
        data = handle_channel_input(data)

        #Matrices

        time = time_amplitude(data, rate)
        frequency, power = frequency_power(data, rate)
        max_x, max_y =find_frequency_of_highest_power_value(frequency, power)

        #Plots

        time_amplitude_plot(time, data, self.plot1)
        frequency_power_plot(frequency, power, max_x, max_y, self.plot2)




