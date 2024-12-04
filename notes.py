#print(mdl.User.get_by_id(1)
'''
import numpy, scipy, random
from scipy.special import erfinv
deltaXMean = 0.05
deltaXStDev = 0.01
deltaYMean = -0.03
deltaYStDev = 0.01
pixelCount = 256

deltaXList = []
deltaYList = []
xPosList = []
yPosList = []

class Pixel:
    def __init__(self, serialNum, xPos, yPos, deltaX, deltaY):
        self.serialNum = serialNum
        self.xPos = xPos
        self.yPos = yPos
        self.deltaX = deltaX
        self.deltaY = deltaY
    
    def randomDelta(self):
        self.deltaX = scipy.special.erfinv(2 * (random.random() - 0.5)) * deltaXStDev * numpy.sqrt(2.0) + deltaXMean
        self.deltaY = scipy.special.erfinv(2 * (random.random() - 0.5)) * deltaYStDev * numpy.sqrt(2.0) + deltaYMean
        deltaXList.append(self.deltaX)
        deltaYList.append(self.deltaY)
        xPosList.append(self.xPos)
        yPosList.append(self.yPos)

#this section was commented out in the comment
testPixel = Pixel(0, 0, 0, 0)

testcount = 1000
tested = 0

while tested < testcount:
    testPixel.randomDelta()
    tested += 1

runningSum = 0
for i in deltaXList:
    runningSum += i

average = runningSum / len(deltaXList)

#print(deltaXList)
print(average)
print(numpy.std(deltaXList))
#this section was commented out in the comment

pixels = []
for i in range(pixelCount + 1):
    if i > 0:
        newPixel = Pixel(i, 0, 0, 0, 0)
        newPixel.yPos = numpy.ceil(i / 16)
        newPixel.xPos = i - (16 * (newPixel.yPos - 1))
        newPixel.randomDelta()
        pixels.append(newPixel)

#this section was commented out in the comment
print(pixels)
print(pixels[0])
for i in range(len(pixels)):
    print(pixels[i].yPos, pixels[i].xPos)
#print(pixels[0].xPos)
print(pixels[0].deltaX)
print(numpy.ceil(1/16))
#this section was commented out in the comment

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')


# plot
fig, ax = plt.subplots()

x = xPosList
y = yPosList
u = deltaXList
v = deltaYList

#ax.scatter(u, v)
#ax.set(xlim=(-.1,.1), ylim=(-.1,.1))

ax.quiver(x, y, u, v)
ax.set(xlim=(-1, 17), ylim=(-1, 17))

plt.show()



#16x16 counter for good/bad, draw mean & standard dev oval
#progress bar to fill 2 Ds (full circle)
    #different sections based on module stage (assembled, tested, shipped)

#plots that look like a module (type 1)
# in module find pick & place assembly data to make displacement graph
#almost any kind of graph you want, theres a lot of data
'''
