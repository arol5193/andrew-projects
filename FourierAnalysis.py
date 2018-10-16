#!/usr/bin/env python3

#creates a Fourier analysis plot of solar cell data
import numpy as np
import matplotlib.pyplot as plt

from file_readlines import file_readlines

from matplotlib.mlab import psd

File = input("Enter the text file name you would like to import: ")
print(File)
indata = file_readlines(File)
length = len(indata)
#print(indata)

array = np.zeros(length) #array that is of the size of the text file
for i in range(length):
	array[i]=float(indata[i]) #turns the strings in the array to floats
	i =i+1
sums = sum(array)
avg = sums/length 

for i in range(length): #loop that takes away the DC value at 0.
    array[i]=array[i]-avg
    i =i+1
#print(array)

FTIME = 1       # function range in seconds
FS = 920         # samples per second
points = FTIME*FS  # number of sample points

fft = np.fft.fft(array, n=16*points)
fftnormal = abs(fft)
p = fftnormal**2
xvals = np.fft.fftfreq(len(p), 1.0/FS)
f1, ax1 = plt.subplots()
ax1.plot(xvals,p)
ax1.set_xlim(0,200)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('Fourier Analysis', size = 20, weight = 'bold')
f1.show()

y, x = psd(array, NFFT=points, Fs=FS, pad_to=16*points)
f2, ax2 = plt.subplots()
ax2.plot(x,y)
ax2.set_xlim(0,200)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('PSD of Solar Data', size = 20, weight = 'bold')

f2.show()

input("\nPress <Enter> to exit...\n")
