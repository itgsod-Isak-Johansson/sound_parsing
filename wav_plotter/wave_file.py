__author__ = 'thedoctor'

import scipy.io.wavfile as wavfile


class WaveFile:

    version = '0.1'

    def __init__(self, file_name, data):
        self.open_file(file_name)
        self.handle_channel_input(data)

    @staticmethod
    def open_file(file_name):
        rate, data = wavfile.read('{0}'.format(file_name))
        return data, rate

    @staticmethod
    def handle_channel_input(data):

        format = data.shape

        try:
            channels = format[1]

        except IndexError:
            channels = 1

        if channels == 2:
            data = data[:, 0]
        return data


