import random
import matplotlib.pyplot as plt
import numpy
import numpy as np
import math
import operator
import progressbar
import time
from random import randrange
from random import randint
from numpy.random import choice




individuals = 4
geneLength = 5
population = []
Fitness = []
RWFitness = []
CFitness = []
MFitness = []
OVRAverage = []
OVRMax = []
OVRMin = []
SUM = []
Probability = []
tempPopulation = []
tempPopulation2 = []
spCrossover = randrange(1, geneLength)
MutationRate = 0.02
CrossoverRate = 1.0
Generation = 25



#################################################### GENERATE RANDOM BASE 10 INDIVIDUAL BETWEEN 0-255 & CONVERT TO BASE 2 ####################################
def init_pop2():
    z = 0
    Sum = 0
    Average = 0
    Max = 0
    for i in range(0, individuals):
        base10 = (random.randint(0,31))
        base2 = "{0:b}".format(base10)
        if (len(base2) < geneLength):
            if(len(base2) == 1):
                base2 = "0000" + base2
            if(len(base2) == 2):
                base2 = "000" + base2
            if(len(base2) == 3):
                base2 = "00" + base2
            if(len(base2) == 4):
                base2 = "0" + base2
        population.append(base2)

        ############################################### FITNESS = f(x) = x*x #################################
        z += 1

def RW2():
    z = 0
    Sum = 0
    Average = 0
    Max = 0
    Fitness.clear()
    for i in range(0, len(population)):
        xValue = (int(population[z], 2))
        Fitness.append(xValue * xValue)
        Sum = Sum + Fitness[z]
    #    print("INDIVIDUAL", z, " | ", "BASE 2 >", population[z], " | ", "BASE 10 >", xValue, " | ", "FITNESS", Fitness[z], " | ", "SUM", Sum, )
        z += 1
    SUM.append(Sum)
    Average = Sum / individuals
    Max = max(Fitness)

    #print("SUM START", Sum)
    #print("AVERAGE START", Average)
    #print("MAXIMUM", Max)

    z = 0
    for i in range(0, len(population)):
        probability = (Fitness[z] / Sum)
        Probability.append(probability)
    #    print("INDIVIDUAL", z, " | ", "BASE 2 >", population[z], " | ", "FITNESS", Fitness[z], " | ", "SUM", Sum, "Probability", probability )
        z += 1


    z = 0
    for i in range(0, individuals):
        x = choice(population, 1, p=Probability, replace=True)
        tempPopulation.append(x[0])
        #print(x[0])
        #print(tempPopulation[z])
        z += 1

def Crossover():
    two = (individuals / 2)
    z = 0
    for i in range(0, int(two)):
        randinter = randint(0, 100) / 100
    #    print(randinter)
        if(randinter <= CrossoverRate):
            parent1 = tempPopulation[z]
            x = [int(i) for i in parent1]
            Pa = x[0:spCrossover]
            Pb = x[spCrossover:len(x)]
            z += 1

            parent2 = tempPopulation[z]
            y = [int(i) for i in parent2]
            Pc = y[0:spCrossover]
            Pd = y[spCrossover:len(y)]
            z += 1

    #  #  #print("P1", parent1, Pa,Pb)
        #print("P2", parent2, Pc,Pd)

            child2 = Pa + Pd
            child1 = Pc + Pb

        #print("Child 1", child1)
        #print("Child 2", child2)

            n = 0
            c1 = ""
            for i in range(0, len(child1)):
                c1 = str(child1[n]) + c1
                n += 1
            c1 = c1[::-1]
            population.append(c1)
    #    print(c1, "Child 1")


            n = 0
            c2 = ""
            for i in range(0, len(child2)):
                c2 = str(child2[n]) + c2
                n += 1
            c2 = c2[::-1]
            population.append(c2)
        #print(c2, "Child 2")
        if(randinter > CrossoverRate):
            population.append(tempPopulation[z])
            z +=1
            population.append(tempPopulation[z])
            z +=1

#    print(population)
    z = 0
    Sum = 0
    for i in range(0, len(population)):
        xValue = (int(population[z], 2))
        CFitness.append(xValue * xValue)
        Sum = Sum + CFitness[z]
        #print("Crossover Individual", z, "| BASE 2 > ", population[z], "| BASE 10 >", xValue, "| Fitness >", CFitness[z], "/", Sum)
        z += 1

    Average = Sum / individuals
    Max = max(CFitness)
    #print("SUM", Sum)#print("AVERAGE", Average)print("MAXIMUM", Max)
def Mutation():
    tempPopulation.clear()
    z = 0
    for i in range(0, individuals):
        x = population[z]
        #print("SPLIT")
        n = 0
        new = ""
        for i in range(0, len(x)):
            Random = random.randint(1,100) / 100
            if(MutationRate >= Random):
                a = int(x[n])
            #    print(a, "CHANGE")

                if a == 1:
                    a = 0
                elif a == 0:
                    a = 1

            #    print("MUTATION")
                #print(x[n], a, "CHANGE1")
                new = new + str(a)

            if(MutationRate < Random):
                #print("NO MUTATION")
                new = new + x[n]
                #print(x[n])
            n += 1
        tempPopulation.append(new)
    #    print(tempPopulation[z])
            #print(population[z])
        z += 1

    z = 0
    Sum = 0
    Max = 0
    Average = 0
    MFitness.clear()
    population.clear()
    for i in range(0, len(tempPopulation)):
        xValue = (int(tempPopulation[z], 2))
        MFitness.append(xValue * xValue)
        Sum = Sum + MFitness[z]
        population.append(tempPopulation[z])
    #    print("Mutation Individual", z, "| BASE 2 > ", tempPopulation[z], "| BASE 10 >", xValue, "| Fitness >", MFitness[z], "/", Sum)
        z += 1

    Average = Sum / individuals
    Max = max(MFitness)
    Min = min(MFitness)

    print("SUM MUTATION", Sum)
    print("AVERAGE END", Average)
    OVRAverage.append(Average)
    OVRMax.append(Max)
    OVRMin.append(Min)
    print("MAXIMUM", Max, "MIN", Min, "\n")

def main():
    init_pop2()
    gen = 0
    genr = []

    for i in range(0, Generation):
        print("GENERATION ", gen)
        RW2()
        population.clear()
        Probability.clear()
        Crossover()
        Mutation()
        genr.append(gen)
        gen += 1


    ovr_average, = plt.plot(genr, OVRAverage, label="Average")
    ovr_max = plt.plot(genr, OVRMax, label ="Max")
    ovr_min = plt.plot(genr, OVRMin, label = "Min")
    plt.legend()
    plt.ylabel('Fitness | f(x) = x*x  |')
    plt.xlabel('Generation')
    plt.title("MR:" + str(MutationRate) + "| CR:" + str(CrossoverRate) + "| POP SIZE:" + str(individuals) + "| GENS:" + str(Generation))
    plt.show()



main()
