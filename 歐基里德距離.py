# Monte Carlo simulation to estimate the probability that two randomly chosen points in a unit square are within a distance of 1.

import random
def estimateProb(n):
    lessThan1n = 0
    for p in range(n):
        x1 = random.random()
        y1 = random.random()
        x2 = random.random()
        y2 = random.random()
        if ((x1 - x2)**2 + (y1 - y2)**2)**0.5 < 1:
            lessThan1n += 1
    return lessThan1n/n



print('The estimate probability of n = 100 is: ' + str(estimateProb(100)))
print('The estimate probability of n = 1000 is: '+ str(estimateProb(1000)))
print('The estimate probability of n = 10000 is: ' + str(estimateProb(10000)))