import numpy as np
import pylab as plt

xlist = np.arange(0, 1.1, .1)
def curve(x, k):
    return 1 - 1 / (k * x + 1)
def curved(x, k):
    return curve(x, k) / curve(1, k)
def sigmoid(x, k, b):
    return 1 / (1 + np.e**(-k * (x - b)))
def sigmoided(x, k, b):
    return (sigmoid(x, k, b) - sigmoid(0, k, b)) / (sigmoid(1, k, b) - sigmoid(0, k, b))
y1 = []
y2 = []
y3 = []
choice = 0
for i in xlist:
    if choice == 1:
        y1.append(curved(i, 1))
        y2.append(curved(i, 2) - curved(i, 1))
        y3.append(curved(i, 3) - curved(i, 2))
    else:
        y1.append(sigmoided(i, 5, 0.95))
        y2.append(sigmoided(i, 2.25, 0.075) - sigmoided(i, 5, 0.95))
        y3.append(sigmoided(i, 8, 0.1) - sigmoided(i, 2.25, 0.075))
y = [y1, y2, y3]

plt.stackplot(xlist, *y)
plt.show()