import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from math import pi
import cmath
import numpy as np


def shift_bit_length(x):
    return 1<<(x-1).bit_length()


#zeroPadding:
#https://stackoverflow.com/questions/34625626/zero-padding-data-until-its-length-is-equal-to-a-power-of-2

#explanation of zero padding:
#https://dsp.stackexchange.com/questions/741/why-should-i-zero-pad-a-signal-before-taking-the-fourier-transform

def padpad(data, iterations = 1): #This function is used when the array of data read in from the wav file isn't a power
    narray = data                 # of 2. It zero pads the array in the front and back - this doesn't impact the analysis
    for i in range(iterations):
        length = len(narray)
        diff = shift_bit_length(length + 1) - length
        print(diff)
        if length % 2 == 0:
            pad_width = int(diff / 2)
        else:
            # need an uneven padding for odd-number lengths
            left_pad = int(diff / 2)
            right_pad = diff - left_pad
            pad_width = (left_pad, right_pad)
        narray = np.pad(narray, pad_width, 'constant')
    return narray

def plotWaveFile(array_of_data):
    d = int(len(array_of_data) / 2)  # you only need half of the fft list (real signal symmetry)

    plt.plot(np.abs(array_of_data[:(d - 1)]), 'r') #goes through each abs value of the frequencies and plots them
    plt.show()
    
    
    #example reading wav file and plotting:
    #https://stackoverflow.com/questions/23377665/python-scipy-fft-wav-files

def readWavFile(filename):
    plotSoundFile(filename)
    fs, data = wavfile.read(filename) # load the data
    a = data.T[0:data.size] # this is a two channel soundtrack, I get the first track
    b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)

    b = padpad(b) #always zero pad extend, if it's already a power of two this won't matter

    c = fft(b) # calculate fourier transform (complex numbers list)
    plotWaveFile(c) #plot the result of the frequency transform

    
    
    #fft c++ and python implementation: 
    #https://rosettacode.org/wiki/Fast_Fourier_transform#C.2B.2B
def fft(x):
    N = len(x)
    if N <= 1: return x #divide and conquer algorithm of the FFT
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    T= [cmath.exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]

def plotSoundFile(filename):
    input_data = wavfile.read(filename)
    audio = input_data[1]
    # plot the first 1024 samples
    plt.plot(audio[0:1024])
    # label the axes
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    # set the title
    plt.title("Sample Wav")
    # display the plot
    plt.show()

filename = 'america.wav'
readWavFile(filename)
