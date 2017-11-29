import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from math import pi, exp


def plotWaveFile(array_of_data):
    d = int(len(array_of_data) / 2)  # you only need half of the fft list (real signal symmetry)

    plt.plot(abs(array_of_data[:(d - 1)]), 'r')
    plt.show()


def readWavFile(filename):
    fs, data = wavfile.read(filename) # load the data
    a = data.T[0:data.size] # this is a two channel soundtrack, I get the first track
    b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    c = fft(b) # calculate fourier transform (complex numbers list)


def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    T= [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]

