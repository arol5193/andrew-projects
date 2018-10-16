#!/usr/bin/env python3

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt


NPOINTS=640

xvals = np.linspace(0, 2.5*np.pi, NPOINTS)
yvals = np.linspace(0, 2.5*np.pi, NPOINTS)
x= np.zeros(NPOINTS)
y= np.zeros(NPOINTS)
x[:]= xvals[:]
y[:]= yvals[:]

x,y = np.meshgrid(x,y) #creates plane

z = np.cos(x)*np.sin(y) #function being plotted

fig = plt.figure()
ax1 = fig.gca(projection='3d')
surf = ax1.plot_surface(x,y,z, cmap = cm.coolwarm, linewidth=0)
fig.colorbar(surf,shrink=0.5, aspect=5)
ax1.set_xlabel('x(rad)')
ax1.set_ylabel('Y(rad)')
ax1.set_zlabel('z(x,y)')
ax1.set_title('z(x,y)=cos(x)sin(y)')

plt.show()

input("\nPress <Enter> to exit...\n")
