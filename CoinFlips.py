#!/usr/bin/env python3

#Function that simulates a coin flip. Plot of the probability of heads per trial.

import numpy as np
import matplotlib.pyplot as plt

def coin(attempts):
	flips = np.random.random(attempts)
	result = np.zeros(attempts)
	for i in range(attempts):
		if flips[i] < 0.5 :
			result[i]=1
		else:
			result[i]=0

	heads = sum(result)
	return heads

set = np.zeros(1000)

for i in range(1000):
	set[i] = coin(100)

mean = np.mean(set)
#print(mean)

std = np.std(set) #standard deviation
#print(std)
q = 33

f1, ax1 = plt.subplots()
n,bins2,patches = ax1.hist(set,q,normed=1,label = "Heads Prob.")
a = round(std,3)
b = round(mean,3)
d = str(a)
c = str(b)

y  = ((1 / (np.sqrt(2 * np.pi) * std)) *np.exp(-0.5 * (1 / std * (bins2 - mean))**2))
ax1.plot(bins2, y, 'g', label =" Gaussian Fit"+ "\nMean: " + c + "\nStan. Dev: " + d)
plt.title('Coin Toss Distribution', size=24, weight = 'bold')
plt.xlabel('Number of 100 flip trials')
plt.ylabel('Probabilty of heads')
ax1.legend()
f1.show()
input("\nPress <Enter> to exit...\n")
