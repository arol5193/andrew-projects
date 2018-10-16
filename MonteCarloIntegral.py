#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

#Monte Carlo method for solving the integral of e^(-x^2).
x = 10*np.random.random(100000)
y = np.random.random(100000)
hit = 0
	
for i in range(100000):
	if y[i] <= np.exp(-(x[i]*x[i])):
		hit = hit + 1

a = hit*10 / 100000
 
n = 2*a #value of integral
frac = abs(np.sqrt(np.pi) - n)/np.sqrt(np.pi) #fractional error

print('The integral of e^(-x^2) using the Monte Carlo Method is: %8f' %n)

print('The fractional error of the Monte Carlo method is: %8f' %frac)


def error(N):
	x = 10*np.random.random(N)
	y = np.random.random(N)
	hit = 0
	for i in range(N):
		if y[i] <= np.exp(-(x[i]*x[i])):
			hit = hit + 1



	a = hit*10 / N
	n = 2*a 
	frac = abs(np.sqrt(np.pi) - n)/np.sqrt(np.pi)
	return frac



N=10
xval = np.zeros(14)
yval = np.zeros(14)                                                              
for i in range(14):
    xval[i] = N
    yval[i] = error(N)
    N = N*2

f1, ax1 = plt.subplots()
ax1.scatter(xval, yval, label = 'Fractional  Error')
plt.title('Monte Carlo Fractional Error', size=24, weight = 'bold')
plt.xlabel('Number of Points')
plt.ylabel('Fractional Error')
ax1.legend()

f1.show()

input("\nPress <Enter> to exit...\n")
