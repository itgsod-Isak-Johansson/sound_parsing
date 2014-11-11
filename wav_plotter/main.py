__author__ = 'thedoctor'

import sys
sys.path.append('../')
from wave_file import WaveFile
from plot import Plot
from matrices import Matrices


class Main:

    version = '0.1'

    def __init__(self, file_name):
        self.file_name = file_name
        self.class_manager()

    def class_manager(self):

        #open wave file
        data, rate = WaveFile.open_file(self.file_name)
        #handle mono and stereo wave files
        data = WaveFile.handle_channel_input(data)

        #Matrices
        time = Matrices.time_amplitude(data, rate)
        frequency, power = Matrices.frequency_power(data, rate)
        max_x, max_y = Matrices.find_frequency_of_highest_power_value(frequency, power)

        #Plots
        plot1 = Plot.time_amplitude_plot(time, data)
        plot2 =Plot.frequency_power_plot(frequency, power, max_x, max_y, file_name)
        return plot1, plot2


if __name__ == "__main__":
    file_name = raw_input('Please enter the name of the file to be plotted. >>  ')
    Main(file_name)