#!/usr/bin/env python3

# plots voltage over time from a light source using a solar cell.
ACQTIME = 1.0  # seconds of data acquisition

SPS = 920 # samples per second

VRANGE = 4096 # voltage range in mV

nsamples = int(ACQTIME*SPS)
sinterval = 1.0/SPS

import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from Adafruit import ADS1x15

adc = ADS1x15()

indata = np.zeros((nsamples,1),'float')
# (nsamples,1) turns array into column array


print()
print('Initializing ADC...')
print()


#
# Default ADC IC is ADS1015
# Default address is 0x48 on the default I2C bus
#
#adc = ADS1x15()



# First two arguments are the channels
# Third argument is the full-scale range in mV (default +/- 6144).
#    options: 256, 512, 1024, 2048, 4096, 6144.
#    Note: input should not exceed VDD + 0.3
# Fourth argument is samples per second (default 250).
#    options: 128, 250, 490, 920, 1600, 2400, 3300.
#
adc.startContinuousDifferentialConversion(2, 3, pga=VRANGE, sps=SPS)

input('Press <Enter> to start %.1f s data acquisition...' % ACQTIME)
print()

t0 = time.perf_counter()

for i in range(nsamples):
   st = time.perf_counter()
   indata[i] = 0.001*adc.getLastConversionResults()
   while (time.perf_counter() - st) <= sinterval:
      pass
#print(indata)

t = time.perf_counter() - t0

a = str(indata) # turns solar cell data into a string to be written in a file.
b = a.replace('[','')
data = ' ' + b.replace(']','')
File = input('\n\nPlease input the name of the file thst will store : ')
#print(File)

from careful_write import careful_write
careful_write(data, File)

adc.stopContinuousConversion()

xpoints = np.arange(0, ACQTIME, sinterval)

print('Time elapsed: %.9f s.' % t)
print()

f1, ax1 = plt.subplots()

#
# Default plotting style connects points with lines
#
ax1.plot(xpoints, indata)
plt.xlabel('Time(s)')
plt.ylabel('Voltage(V)')
plt.title('Solar Cell Voltage', size = 20, weight = 'bold')
#
# Plotting with steps is better for visualizing sampling
#
# ax1.plot(xpoints, indata,'-',drawstyle='steps-post')

f1.show()

input("\nPress <Enter> to exit...\n")


#while True:
 #  v23 = adc.readADCDifferential23(4096, 128)*0.001  # returns float
 #  print('%.4f V' % v23)
 #  time.sleep(0.5)

