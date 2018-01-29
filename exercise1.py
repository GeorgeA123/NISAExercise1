    #!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import argparse
import array


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-question')
    parser.add_argument('-bits_x')
    parser.add_argument('-bits_y')
    parser.add_argument('-chi')
    parser.add_argument('-repetitions')
    parser.add_argument('-population')
    parser.add_argument('-k')
    parser.add_argument('-n')
    parser.add_argument('-lam','-lambda')

    args = parser.parse_args()
    print (args)
    exercise = args.question
    lambdaVari = args.lam
    n = args.n
    bitsX = args.bits_x
    bitsY = args.bits_y
    if args.population != None:
        population = convertPopToList(args.population)
    if args.k != None:
        k = int(args.k)
    chi = ''
    chiNum = True
    repNum = True
    questionFiveVarCorrect = True
    if args.chi != None:
        try:
            chi = float(args.chi)

        except:
            chiNum = False
            chi = ''
    try:
        rep = int(args.repetitions)

    except:
        repNum = False
    try:
        lambdaVari = int(args.lam)
        n = int(args.n)
    except:
        questionFiveVarCorrect = False

    if exercise == '1' and chiNum == True and repNum == True:
        for a in range(0,rep):
            print(exerciseOne(bitsX, chi))

    elif exercise == '2' and repNum == True:
        for a in range(0, rep):
            print(exerciseTwo(bitsX, bitsY, ))
    elif exercise == '3':
        print(exerciseThree(bitsX))
    elif exercise == '4' and repNum == True:
        for a in range(0,rep):
            print(exerciseFour(population,k))
    elif exercise == '5' and questionFiveVarCorrect:
        for a in range(0, rep):
           print(exerciseFive(n,chi,k,lambdaVari))

    else:
        print ("incorrect usage")


def exerciseOne(bitsX, chi):

    for i in range(0, len(bitsX)):

        if random.random() <  (chi / len(bitsX)):
            if bitsX[i] == '1':
                bitsX = bitsX[:i] + '0' + bitsX[i + 1:]
            else:
                bitsX = bitsX[:i] + '1' + bitsX[i + 1:]

    return bitsX


def exerciseTwo(bitsX, bitsY):
    resultBits = ''
    for i in range(0, len(bitsX)):
        if bitsX[i] == bitsY[i]:
            resultBits += bitsX[i]
        else:
            if random.random() >= 0.5:
                resultBits += bitsX[i]
            else:
                resultBits += bitsY[i]



    return resultBits



def exerciseThree(bitsX):
    counter = 0
    for i in range(0, len(bitsX)):
        counter += int(bitsX[i])

    return counter


def exerciseFour(population, k):

    subsetOfPop = []
    best = ""
    for i in range(0, k):
       subsetOfPop.append(population[random.randint(0,len(population) -1)])

    bestOfSubset = findBestFitness(subsetOfPop)
    best  = bestOfSubset[random.randint(0, len(bestOfSubset) - 1)]

    return (best)

def findBestFitness(list):
    bestVa = 0
    bestEn = []
    for a in list:
      
        if exerciseThree(a) > bestVa:
            bestVa = exerciseThree(a)
            bestEn.clear()
            bestEn.append(a)
        elif exerciseThree(a) == bestVa:
            bestEn.append(a)
    return bestEn

def convertPopToList(population):
    return population.split(" ")

def createBitString(length):
    bit = ""
    for i in range(0, length):
        if random.random() >= 0.5:
            bit = bit + '1'
        else:
            bit = bit + '0'
    return bit


def exerciseFive(n, chi, k, lam):

    population= []
    for i in range(0, lam):
        population.append(createBitString(n))
    sat = False
    tP = []
    tP.append(population)
    t =0
    index = 0
    while(not sat):
        newPopulation = []
        t += 1
        for i in range(0, lam):

            x = exerciseFour(tP[t-1], k)
            y = exerciseFour(tP[t-1], k)
            newPopulation.append(exerciseTwo(exerciseOne(x,float(chi)), exerciseOne(y,float(chi))))

        tP.append(newPopulation)
        for p in range(0, len(newPopulation)):
            if exerciseThree(newPopulation[p]) == n:
                sat = True
                index = p



    return (str(n) + "\t"+ str(chi) + " \t" + str(lam) + " \t" + str(k) + " \t" + str(t) + " \t" + str(float(exerciseThree(tP[t][index]))) + " \t" + tP[t][index])





main(sys.argv)


