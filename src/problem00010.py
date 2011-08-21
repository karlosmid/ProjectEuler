# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 25, 2011 6:13:28 PM$"

def testSieve():
    sieve(2000000)
def testImprovedSieve():
    sieveImproved(2000000)
def sieveImproved(limit):
    import math
    primes = []    
    i = 1
    while i <= (limit-1)/2:
        primes.append(True)
        i = i + 1
    for i in range(1,int(math.sqrt(limit)-1)/2 +1):
        if primes[i]:
            j = 2*i*(i+1)
            while j < (limit-1)/2:
                primes[j] = False
                j = j + 2*i+1
    sum = 2
    i = 1
    for elem in primes[1:]: #because 1 is not prime number
        if elem:
            sum = sum + 2*i + 1
        i = i + 1
    print sum
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
    testImprovedSieve()
