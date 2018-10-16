#!/usr/bin/env python3

ACQTIME = 80.0  # seconds of data acquisition

#    samples per second
#    options: 128, 250, 490, 920, 1600, 2400, 3300.
SPS = 4

#    full-scale range in mV
#    options: 256, 512, 1024, 2048, 4096, 6144.
#VRANGE = 4096

nsamples = int(ACQTIME*SPS)
sinterval = 1.0/SPS

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import Adafruit.MCP9808 as MCP9808
import matplotlib.pylab as lab

from careful_write import careful_write

sensor = MCP9808()
sensor.begin()

indata = np.zeros((nsamples,1),'float')

print("\nStart the heating or cooling process now" )

print()
print('Initializing MCP9808...')


#adc = ADS1x15()

# First two arguments are the channels
# Third argument is the full-scale range in mV (default +/- 6144).
#    options: 256, 512, 1024, 2048, 4096, 6144.
#    Note: input should not exceed VDD + 0.3
# Fourth argument is samples per second (default 250).
#    options: 128, 250, 490, 920, 1600, 2400, 3300.
#
#adc.startContinuousDifferentialConversion(2, 3, pga=VRANGE, sps=SPS)


input('Press <Enter> to start %.1f s data acquisition...' % ACQTIME)
print()

t0 = time.perf_counter()
l = str(indata[0])
for i in range(nsamples): #for loop that puts the temp. reading in the array
   t = time.perf_counter()
   Tc = sensor.readTempC()
   indata[i] = Tc
   while (time.perf_counter() - t) <= sinterval:
      pass

t = time.perf_counter() - t0

xval = np.arange(0, ACQTIME, sinterval) #array of xvalues
xval2= xval[30:] 
x1 =np.log(xval) #turns xval into its log form
x2 = x1[30:] #section that contains the heating or cooling curve
log = np.log(indata) #turns y-values into its log form
log2 = log[30:]
#f2, ax2 = plt.subplots()
#ax2.scatter(x2,nat)

print('Time elapsed: %.9f s.' % t)
print()

plotfit =lab.polyfit(x2,log2,1)

p1= lab.polyval(plotfit,x2)


p2 = np.exp(p1)
lab.plot(x2,p1)
a,b = lab.polyfit(x2,log2,1)
p3= a*x2+b 
k1 =np.around(1/a,2) #rounding function
k=float(k1)
print("Time constant k is :", str(k),"s/degC")

f1, ax1 = plt.subplots()
plt.title('Exponential Temperature Decay', size=20, weight = 'bold')
ax1.scatter(xval, indata, label = 'Data')
ax1.plot(xval2,p2,'r',linewidth=1, label ='Exponential fit\n k='+ str(k)+"s/degC")
plt.xlabel('Time(s)')
plt.ylabel('Temperature(degC)')
ax1.legend()

f2, ax2 = plt.subplots()
lab.plot(x2,p1)
ax2.plot(x2,p1)
ax2.scatter(x2,log2)
plt.xlabel('Time(s)')
plt.ylabel('Temperature(degC)')
plt.title('Linear fit of Temperature Decay', size=20, weight = 'bold')
ax2.legend()

f1.show()
f2.show()
input("\nPress <Enter> to exit...\n")
