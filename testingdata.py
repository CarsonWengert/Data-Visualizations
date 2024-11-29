import matplotlib.pyplot as plt
import numpy as np

#outputs the upper y value for a point with a certain x value on a circle of radius x centered around (h,k)
def circleTop(x, r, h, k):
    return k + np.sqrt(r**2.0 - (x-h)**2.0)

#outputs the lower y value for a point with a certain x value on a circle of radius x centered around (h,k)
def circleBottom(x, r, h, k):
    return k - np.sqrt(r**2.0 - (x-h)**2.0)

#outputs the area of a section of a semicircle of a certain radius to the left of a certain x value
def semicircleArea(radius, xvalue):
    return (radius**2.0 * np.arcsin(xvalue / radius) + xvalue * np.sqrt(radius**2.0 - xvalue**2.0)) / 2.0 + np.pi * radius**2.0 / 4.0

#input variables
rLarge = 1.0 #outside circle radius
rRatio = .1 #inside circle radius, as a proportion of outside circle radius. important: maximum of 1/sqrt(2)=0.707
spacing = 0.1 #gap size between two halves
filllist = [[1, 'red'], [0.2, 'blue'], [0.1, 'black']] #list of fractions and colors. make this always decreasing; it overlays each additional layer

#setting up sections to use later
totalArea = np.pi / 2.0 * (rLarge**2.0 - (rLarge * rRatio)**2.0) #area of 1 d washer
fflim1 = semicircleArea(rLarge, -rLarge * rRatio) / totalArea #"fill fraction limit 1"
fflim2 = 0.5
fflim3 = 1 - fflim1
fflim4 = (semicircleArea(rLarge, np.sqrt(rLarge**2.0 - (rLarge * rRatio)**2.0)) - np.pi / 2.0 * (rLarge * rRatio)**2.0) / totalArea

for i in filllist:
    fillfrac = i[0]
    inputcolor = i[1]

    #since there was no closed-form solution to find the y value i went with an approximation loop, but i'm sure there's a better way
    if fillfrac <= fflim1:
        lowerGuess = -rLarge
        higherGuess = -rLarge * rRatio
        yGuess = -(rLarge + rLarge * rRatio) / 2.0
        area = semicircleArea(rLarge, yGuess)
        areaError = fillfrac * totalArea - area
        while abs(areaError) > 0.001:
            if area / totalArea < fillfrac:
                lowerGuess = yGuess
            elif area / totalArea > fillfrac:
                higherGuess = yGuess
            yGuess = (lowerGuess + higherGuess) / 2.0
            area = semicircleArea(rLarge, yGuess)
            areaError = fillfrac * totalArea - area
    elif fillfrac > fflim1 and fillfrac <= fflim3: #this combines ranges 2&3
        lowerGuess = -rLarge * rRatio
        higherGuess = rLarge * rRatio
        yGuess = 0.0
        area = semicircleArea(rLarge, yGuess) - semicircleArea(rLarge * rRatio, yGuess)
        areaError = fillfrac * totalArea - area
        while abs(areaError) > 0.001:
            if area / totalArea < fillfrac:
                print('thinks area too small')
                print('area: ', area)
                print('fraction: ', area / totalArea)
                lowerGuess = yGuess
            elif area / totalArea > fillfrac:
                print('thinks area too large')
                higherGuess = yGuess
            yGuess = (lowerGuess + higherGuess) / 2.0
            area = semicircleArea(rLarge, yGuess) - semicircleArea(rLarge * rRatio, yGuess)
            areaError = fillfrac * totalArea - area
    elif fillfrac > fflim3:
        lowerGuess = rLarge * rRatio
        higherGuess = rLarge
        yGuess = (rLarge + rLarge * rRatio) / 2.0
        area = semicircleArea(rLarge, yGuess) - np.pi / 2.0 * (rLarge * rRatio)**2.0
        areaError = fillfrac * totalArea - area
        while abs(areaError) > 0.001:
            if area / totalArea < fillfrac:
                lowerGuess = yGuess
            elif area / totalArea > fillfrac:
                higherGuess = yGuess
            yGuess = (lowerGuess + higherGuess) / 2.0
            area = semicircleArea(rLarge, yGuess) - np.pi / 2.0 * (rLarge * rRatio)**2.0
            areaError = fillfrac * totalArea - area
    filly = yGuess

    #defines sections of d washer to shade
    xrange1A = np.linspace(-0.5 * spacing - np.sqrt(rLarge**2.0 - filly**2.0), -0.5 * spacing, 100)
    xrange2A = np.linspace(-0.5 * spacing - np.sqrt(rLarge**2.0 - filly**2.0), -0.5 * spacing - np.sqrt((rLarge * rRatio)**2.0 - filly**2.0), 100)
    xrange3A = np.linspace(-0.5 * spacing - np.sqrt((rLarge * rRatio)**2.0 - filly**2.0), -0.5 * spacing, 100)
    xrange4A = np.linspace(-0.5 * spacing - rLarge, -0.5 * spacing - np.sqrt(rLarge**2.0 - filly**2.0), 100)
    xrange5A = np.linspace(-0.5 * spacing - np.sqrt(rLarge**2.0 - filly**2.0), -0.5 * spacing - (rLarge * rRatio), 100)
    xrange6A = np.linspace(-0.5 * spacing - (rLarge * rRatio), -0.5 * spacing - np.sqrt((rLarge * rRatio)**2.0 - filly**2.0))
    xrange7A = np.linspace(-0.5 * spacing - (rLarge * rRatio), -0.5 * spacing, 100)
    xrange8A = np.linspace(-0.5 * spacing - rLarge, -0.5 * spacing - (rLarge * rRatio), 100)
    xrange9A = np.linspace(-0.5 * spacing - (rLarge * rRatio), -0.5 * spacing - np.sqrt(rLarge**2.0 - filly**2.0), 100)
    xrange10A = np.linspace(-0.5 * spacing - np.sqrt(rLarge**2.0 - filly**2.0), -0.5 * spacing, 100)

    xrange1B = np.linspace(0.5 * spacing, 0.5 * spacing + np.sqrt(rLarge**2.0 - filly**2.0), 100)
    xrange2B = np.linspace(0.5 * spacing + np.sqrt((rLarge * rRatio)**2.0 - filly**2.0), 0.5 * spacing + np.sqrt(rLarge**2.0 - filly**2.0), 100)
    xrange3B = np.linspace(0.5 * spacing, 0.5 * spacing + np.sqrt((rLarge * rRatio)**2.0 - filly**2.0), 100)
    xrange4B = np.linspace(0.5 * spacing + np.sqrt(rLarge**2.0 - filly**2.0), 0.5 * spacing + rLarge, 100)
    xrange5B = np.linspace(0.5 * spacing + (rLarge * rRatio), 0.5 * spacing + np.sqrt(rLarge**2.0 - filly**2.0), 100)
    xrange6B = np.linspace(0.5 * spacing + np.sqrt((rLarge * rRatio)**2.0 - filly**2.0), 0.5 * spacing + (rLarge * rRatio), 100)
    xrange7B = np.linspace(0.5 * spacing, 0.5 * spacing + (rLarge * rRatio), 100)
    xrange8B = np.linspace(0.5 * spacing + (rLarge * rRatio), 0.5 * spacing + rLarge, 100)
    xrange9B = np.linspace(0.5 * spacing + np.sqrt(rLarge**2.0 - filly**2.0), 0.5 * spacing + (rLarge * rRatio), 100)
    xrange10B = np.linspace(0.5 * spacing, 0.5 * spacing + np.sqrt(rLarge**2.0 - filly**2.0), 100)

    yvals11A = circleBottom(xrange1A, rLarge, -0.5 * spacing, 0.0)
    yvals12A = filly
    yvals21A = circleBottom(xrange2A, rLarge, -0.5 * spacing, 0.0)
    yvals22A = filly
    yvals31A = circleBottom(xrange3A, rLarge, -0.5 * spacing, 0.0)
    yvals32A = circleBottom(xrange3A, rLarge * rRatio, -0.5 * spacing, 0.0)
    yvals41A = circleBottom(xrange4A, rLarge, -0.5 * spacing, 0.0)
    yvals42A = circleTop(xrange4A, rLarge, -0.5 * spacing, 0.0)
    yvals51A = circleBottom(xrange5A, rLarge, -0.5 * spacing, 0.0)
    yvals52A = filly
    yvals61A = circleTop(xrange6A, rLarge * rRatio, -0.5 * spacing, 0.0)
    yvals62A = filly
    yvals71A = circleBottom(xrange7A, rLarge, -0.5 * spacing, 0.0)
    yvals72A = circleBottom(xrange7A, rLarge * rRatio, -0.5 * spacing, 0.0)
    yvals73A = circleTop(xrange7A, rLarge * rRatio, -0.5 * spacing, 0.0)
    yvals74A = filly
    yvals81A = circleBottom(xrange8A, rLarge, -0.5 * spacing, 0.0)
    yvals82A = circleTop(xrange8A, rLarge, -0.5 * spacing, 0.0)
    yvals91A = circleTop(xrange9A, rLarge * rRatio, -0.5 * spacing, 0.0)
    yvals92A = circleTop(xrange9A, rLarge, -0.5 * spacing, 0.0)
    yvals101A = circleTop(xrange10A, rLarge * rRatio, -0.5 * spacing, 0.0)
    yvals102A = filly

    yvals11B = circleBottom(xrange1B, rLarge, 0.5 * spacing, 0.0)
    yvals12B = filly
    yvals21B = circleBottom(xrange2B, rLarge, 0.5 * spacing, 0.0)
    yvals22B = filly
    yvals31B = circleBottom(xrange3B, rLarge, 0.5 * spacing, 0.0)
    yvals32B = circleBottom(xrange3B, rLarge * rRatio, 0.5 * spacing, 0.0)
    yvals41B = circleBottom(xrange4B, rLarge, 0.5 * spacing, 0.0)
    yvals42B = circleTop(xrange4B, rLarge, 0.5 * spacing, 0.0)
    yvals51B = circleBottom(xrange5B, rLarge, 0.5 * spacing, 0.0)
    yvals52B = filly
    yvals61B = circleTop(xrange6B, rLarge * rRatio, 0.5 * spacing, 0.0)
    yvals62B = filly
    yvals71B = circleBottom(xrange7B, rLarge, 0.5 * spacing, 0.0)
    yvals72B = circleBottom(xrange7B, rLarge * rRatio, 0.5 * spacing, 0.0)
    yvals73B = circleTop(xrange7B, rLarge * rRatio, 0.5 * spacing, 0.0)
    yvals74B = filly
    yvals81B = circleBottom(xrange8B, rLarge, 0.5 * spacing, 0.0)
    yvals82B = circleTop(xrange8B, rLarge, 0.5 * spacing, 0.0)
    yvals91B = circleTop(xrange9B, rLarge * rRatio, 0.5 * spacing, 0.0)
    yvals92B = circleTop(xrange9B, rLarge, 0.5 * spacing, 0.0)
    yvals101B = circleTop(xrange10B, rLarge * rRatio, 0.5 * spacing, 0.0)
    yvals102B = filly

    #shades sections of d washers depending on fill fraction section
    if fillfrac <= fflim1:
        coordinatelist = [[xrange1A, yvals11A, yvals12A], [xrange1B, yvals11B, yvals12B]]
    elif fillfrac > fflim1 and fillfrac <= fflim2:
        coordinatelist = [[xrange2A, yvals21A, yvals22A], [xrange3A, yvals31A, yvals32A], [xrange2B, yvals21B, yvals22B], [xrange3B, yvals31B, yvals32B]]
    elif fillfrac > fflim2 and fillfrac <= fflim3:
        coordinatelist = [[xrange4A, yvals41A, yvals42A], [xrange5A, yvals51A, yvals52A], [xrange6A, yvals61A, yvals62A], [xrange7A, yvals71A, yvals72A], [xrange4B, yvals41B, yvals42B], [xrange5B, yvals51B, yvals52B], [xrange6B, yvals61B, yvals62B], [xrange7B, yvals71B, yvals72B]]
    elif fillfrac > fflim3 and fillfrac <= fflim4:
        coordinatelist = [[xrange4A, yvals41A, yvals42A], [xrange5A, yvals51A, yvals52A], [xrange7A, yvals71A, yvals72A], [xrange7A, yvals73A, yvals74A], [xrange4B, yvals41B, yvals42B], [xrange5B, yvals51B, yvals52B], [xrange7B, yvals71B, yvals72B], [xrange7B, yvals73B, yvals74B]]
    elif fillfrac > fflim4:
        coordinatelist = [[xrange7A, yvals71A, yvals72A], [xrange8A, yvals81A, yvals82A], [xrange9A, yvals91A, yvals92A], [xrange10A, yvals101A, yvals102A], [xrange7B, yvals71B, yvals72B], [xrange8B, yvals81B, yvals82B], [xrange9B, yvals91B, yvals92B], [xrange10B, yvals101B, yvals102B]]
    for i in coordinatelist:
        plt.fill_between(i[0], i[1], i[2], color=inputcolor)

    #draws top of filled section
    if fillfrac <= fflim1 or fillfrac >= fflim3:
        x5, y5 = [-0.5 * spacing - np.sqrt(rLarge**2.0 - filly**2.0), -0.5 * spacing], [filly, filly]
        x6, y6 = [0.5 * spacing + np.sqrt(rLarge**2.0 - filly**2.0), 0.5 * spacing], [filly, filly]
    else:
        x5, y5 = [-0.5 * spacing - np.sqrt(rLarge**2.0 - filly**2.0), -0.5 * spacing - np.sqrt((rLarge * rRatio)**2.0 - filly**2.0)], [filly, filly]
        x6, y6 = [0.5 * spacing + np.sqrt(rLarge**2.0 - filly**2.0), 0.5 * spacing + np.sqrt((rLarge * rRatio)**2.0 - filly**2.0)], [filly, filly]
    plt.plot(x5, y5, x6, y6, color='black')

#defining outlines of d washers
xValsA = np.linspace(-rLarge - 0.5 * spacing, -0.5 * spacing, 100)
yValsUpA = circleTop(xValsA, rLarge, -0.5 * spacing, 0)
yValsDownA = circleBottom(xValsA, rLarge, -0.5 * spacing, 0)
xValsB = np.linspace(0.5 * spacing, rLarge + 0.5 * spacing, 100)
yValsUpB = circleTop(xValsB, rLarge, 0.5 * spacing, 0)
yValsDownB = circleBottom(xValsB, rLarge, 0.5 * spacing, 0)

xValsL = np.linspace(-rLarge * rRatio - 0.5 * spacing, -0.5 * spacing, 1000)
xValsR = np.linspace(0.5 * spacing, rLarge * rRatio + 0.5 * spacing, 1000)
yValsUpL = circleTop(xValsL, rLarge * rRatio, -0.5 * spacing, 0)
yValsDownL = circleBottom(xValsL, rLarge * rRatio, -0.5 * spacing, 0)
yValsUpR = circleTop(xValsR, rLarge * rRatio, 0.5 * spacing, 0)
yValsDownR = circleBottom(xValsR, rLarge * rRatio, 0.5 * spacing, 0)

x1, y1 = [-0.5 * spacing, -0.5 * spacing], [-rLarge, -rLarge * rRatio]
x2, y2 = [-0.5 * spacing, -0.5 * spacing], [rLarge, rLarge * rRatio]
x3, y3 = [0.5 * spacing, 0.5 * spacing], [-rLarge, -rLarge * rRatio]
x4, y4 = [0.5 * spacing, 0.5 * spacing], [rLarge, rLarge * rRatio]

plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, color='black')

ax = plt.gca()
ax.set_aspect('equal', adjustable='box')

plt.plot(xValsA, yValsUpA, color='black')
plt.plot(xValsA, yValsDownA, color='black')
plt.plot(xValsB, yValsUpB, color='black')
plt.plot(xValsB, yValsDownB, color='black')
plt.plot(xValsL, yValsUpL, color='black')
plt.plot(xValsL, yValsDownL, color='black')
plt.plot(xValsR, yValsUpR, color='black')
plt.plot(xValsR, yValsDownR, color='black')

plt.subplot().set_axis_off()
plt.show()