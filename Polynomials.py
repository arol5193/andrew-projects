#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.pylab as lab


#plot of N order plynomial determined by the user.

while True:
	n =  input('\nPlease enter an integer value of points from 3 to 100 to be randomly distributed:\n')
	try:
		N = int(n)
		if N <= 100 and N >= 3:
			break
		else:
			print('The integer was not between 3 and 100.', file = sys.stderr)
	except ValueError:
		print('That was not an integer. Please try again.\n', file = sys.stderr)

x = 100*np.random.random(N) 
y = 100*np.random.random(N) 

xsort = np.sort(x)

f1, ax1 = plt.subplots()
ax1.scatter(xsort, y)
ax1.set_xlim(0, 100) 
ax1.set_ylim(0, 100)

fit = np.polyfit(xsort, y, 1) #fits to degree 1 polynomial
fitfunc = np.poly1d(fit) # fit functions

fit2 = np.polyfit(xsort, y, N-1) #fit to degree N-1
fitfunc2 = np.poly1d(fit2)

fit3 = np.polyfit(xsort, y, N-3) #fit to degree N-3
fitfunc3 = np.poly1d(fit3)

ax1.plot(xsort, fitfunc(xsort), 'b')#blue line
ax1.plot(xsort, fitfunc2(xsort), 'r')# red  line
ax1.plot(xsort, fitfunc3(xsort), 'k')#black line

f1.show()

input('\nPress <Enter> to exit...\n')
