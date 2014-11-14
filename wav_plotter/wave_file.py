__author__ = 'thedoctor'

import scipy.io.wavfile as wavfile


def open_file(filename):
    rate, data = wavfile.read('{0}'.format(filename))
    return data, rate


def handle_channel_input(data):

    format = data.shape

    try:
        channels = format[1]

    except IndexError:
        channels = 1

    if channels == 2:
        data = data[:, 0]
    return data


