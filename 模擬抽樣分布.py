import random
import matplotlib.pyplot as plt

population = range(1,101)
sampleMeans = []

for times in range(1000):
    samples = random.sample(population, k = 40)
    sampleMean = sum(samples)/ len(samples)
    sampleMeans.append(sampleMean)


plt.hist(sampleMeans, bins = 15, edgecolor = 'black')
plt.title('Distribution of sample means')
plt.xlabel('Sample means')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

populationMean = sum(population)/ len(population)
populationVar = 0
for V in population:
    populationVar += (V - populationMean)**2 / len(population)
populationSD = populationVar**0.5

meanOfSampleMeans = sum(sampleMeans)/len(sampleMeans)
VarOfSampleMeans = 0
for v in sampleMeans:
    VarOfSampleMeans += (v - meanOfSampleMeans)**2 / len(sampleMeans)
SDofSampleMeans = VarOfSampleMeans**0.5


print('Population mean is: ' + str(populationMean))
print('Mean of sample means is: ' + str(meanOfSampleMeans))
print('Standard deviation of the population is: ' + str(populationSD))
print('Standard deviation of sample means is: ' + str(SDofSampleMeans))