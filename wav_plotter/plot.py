__author__ = 'thedoctor'

from matplotlib import pyplot as plt



def time_amplitude_plot(time, data, save_to):
    plt.xkcd()
    plt.plot(time, data, color='#FF69B4')
    plt.title('Time-Amplitude plot', color='#4B0082')
    plt.xlabel('time', color='#4B0082')
    plt.ylabel('amplitude', color='#4B0082')

    plt.savefig(save_to)



def frequency_power_plot(frequency, power, max_x, max_y, save_to):
    star_label = 'Highest power: {0}db, corresponding frequency value: {1}hz'.format(int(max_y), int(max_x))

    #create subplots ax1 and ax2
    plt.xkcd()
    f, (ax1, ax2) = plt.subplots(2)

    plt.xlabel('Frequency(hz)', color='#4B0082')
    plt.ylabel('Power(db)', color='#4B0082')

    #plot axis1
    ax1.set_title('Frequency-Power plot', color='#4B0082')
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

    plt.savefig(save_to)


