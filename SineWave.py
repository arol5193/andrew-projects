#!/usr/bin/env python3


NPOINTS = 512

import sys
import os

import numpy as np
import matplotlib.pyplot as plt

xvals = np.linspace(0, 2.5*np.pi, NPOINTS)
yvals = np.linspace(0, 2.5*np.pi, NPOINTS)
#print(xvals)

f1, ax1 = plt.subplots()
ax1.plot(xvals,np.cos(xvals))
ax1.plot(yvals,np.sin(yvals))

plt.title('sin(x)(orange) and cos(x)(blue)', size=20, weight = 'bold')
plt.xlabel('Angle (radians)')
plt.ylabel('f(x)')
f1.show()

input("\nPress <Enter> to exit...\n")



