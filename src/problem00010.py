# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 25, 2011 6:13:28 PM$"

def testSieve():
    sieve(2000000)
def testSieveOnlyOddNumbers():
    sieveUsingOnlyOddNumbers(2*1000*1000)
def sieveUsingOnlyOddNumbers(upperLimit):
    import math
    upperLimitOnlyOddNumber = (upperLimit -1)/2
    limitOnlyOddNumbersUpToSqrt = int(math.sqrt(upperLimit)-1)/2
    indexEsOfNumbers = initNumbersAllCrosed(upperLimitOnlyOddNumber)
    indexEsOfNumbers = unCrossNotPrimesInNumbers(indexEsOfNumbers,
                                                 upperLimitOnlyOddNumber,
                                                 limitOnlyOddNumbersUpToSqrt)
    sumOfPrimeNumbers = calcSumOfPrimes(indexEsOfNumbers)
    print sumOfPrimeNumbers
def initNumbersAllCrosed(upperLimit):
    i = 1
    numbers = []
    while i <= upperLimit:
        numbers = addCrosed(numbers)
        i = i + 1
    return numbers
def addCrosed(number):
    number.append(False)
    return number
def unCrossNotPrimesInNumbers(numbers,
                              upperLimitOnlyOddNumber,
                              limitOnlyOddNumbersUpToSqrt):        
    rangeLimitOnlyOddNumbersUpToSqrt = range(1, limitOnlyOddNumbersUpToSqrt+1)
    for i in rangeLimitOnlyOddNumbersUpToSqrt:
        if isCrosed(numbers[i]):
            j = calcSquareForOddNumberFromIndex(i)
            while j < upperLimitOnlyOddNumber:
                numbers = unCrossNumber(numbers,j)
                j = j + calcOddFromIndex(i)
    return numbers
def isCrosed(number):
    if not number:
        return True
    else:
        return False
def unCrossNumber(numbers,indexOfNumber):
    numbers[indexOfNumber] = True
    return numbers
def calcSquareForOddNumberFromIndex(i):
    return 2*i*(i+1)
def calcOddFromIndex(i):
    return 2*i+1
def onlyOddPrimes(numbers):
    #because 1 is not prime number
    return numbers[1:]
def calcSumOfPrimes(primes):
    sumOfPrimeNumbers = 0
    onlyEvenPrimeNumber = 2
    sumOfPrimeNumbers = sumOfPrimeNumbers + onlyEvenPrimeNumber
    i = 1
    for elem in onlyOddPrimes(primes):
        if isCrosed(elem):
            sumOfPrimeNumbers = sumOfPrimeNumbers + calcOddFromIndex(i)
        i = i + 1
    return sumOfPrimeNumbers
def sieve(limit):
    import math
    primes = []
    primes.append(False)
    primes.append(False)
    primes.append(True)
    i = 3
    while i < limit+1:
        if i%2 == 0:
            primes.append(False)
        else:
            primes.append(True)
        i = i + 1
    for i in range(3,int(math.sqrt(limit)+1)):
        if primes[i]:
            j = i*i
            while j < limit:
                primes[j] = False
                j = j + i
    sum = 0
    for i in range(2,len(primes)):
        if primes[i]:
            sum = sum + i
    print sum
def sumPrimes():
    import problem00003
    sum = 0
    i = 2
    while i<2000000:
        if problem00003.isPrime(i):
            sum = sum + i
            #print sum,i
        i += 1
    print sum

if __name__ == "__main__":
    testSieveOnlyOddNumbers()
    #142913828922
    #149070583624
