__author__ = 'thedoctor'

import sys
sys.path.append('../')
from wave_file import WaveFile
from plot import Plot
from matrices import Matrices


class Main:

    version = '0.1'

    def __init__(self, file_name_path, file_name):
        self.file_name_path = file_name_path
        self.file_name = file_name


    def class_manager(self):

        #open wave file
        data, rate = WaveFile.open_file(self.file_name_path)
        #handle mono and stereo wave files
        data = WaveFile.handle_channel_input(data)

        #Matrices
        matrices = Matrices(data, rate)
        time = matrices.time_amplitude(data, rate)
        frequency, power = matrices.frequency_power(data, rate)
        max_x, max_y = matrices.find_frequency_of_highest_power_value(frequency, power)

        #Plots
        plot = Plot(self.file_name)
        plot1 = plot.time_amplitude_plot(time, data)
        plot2 = plot.frequency_power_plot(frequency, power, max_x, max_y)
        return plot1, plot2


