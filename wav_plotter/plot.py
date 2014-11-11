__author__ = 'thedoctor'

import matplotlib.pyplot as plt
import StringIO


class Plot:

    version = '0.1'

    def __init__(self, time, data, frequency, power, max_x, max_y, file_name):

        self.time_amplitude_plot(time, data)
        self.frequency_power_plot(frequency, power, max_x, max_y, file_name)

    @staticmethod
    def time_amplitude_plot(time, data):

        plt.plot(time, data, color='#FF69B4')
        plt.xlabel('time', color='#4B0082')
        plt.ylabel('amplitude', color='#4B0082')

        plt.savefig('../website/static/img/plot1.png')


    @staticmethod
    def frequency_power_plot(frequency, power, max_x, max_y, file_name):

        star_label = 'Highest power: {0}db, corresponding frequency value: {1}hz'.format(int(max_y), int(max_x))

        #create subplots ax1 and ax2
        f, (ax1, ax2) = plt.subplots(2)
        plt.xlabel('Frequency(hz)', color='#4B0082')
        plt.ylabel('Power(db)', color='#4B0082')

        #plot axis1
        ax1.set_title('Plot of file: {0}'.format(file_name), color='#4B0082')
        ax1.plot(frequency, power, label='Power', color='#FF69B4')
        ax1.plot(max_x, max_y, '*', label=star_label, color='#FF7F00')
        legend = ax1.legend(loc='lower center', shadow=True, fontsize='x-small')
        # legend.get_frame().set_facecolor('#FF69B4')

        #plot axis2
        ax2.plot(frequency, power, label='Power', color='#FF69B4')
        ax2.plot(max_x, max_y, '*', label=star_label, color='#FF7F00')
        ax2.set_xlim([(max_x - 50), (max_x + 50)])
        legend = ax2.legend(loc='lower center', shadow=True, fontsize='x-small')
        # legend.get_frame().set_facecolor('')

        plt.savefig('../website/static/img/plot2.png')
