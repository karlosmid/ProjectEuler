# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 25, 2011 6:13:28 PM$"

import problem00003 as myPrime
import math

def calcMinEvenlyDivImproved(n):
    lPrimes = []
    rez = 1
    for i in range(2,n+1):
        if myPrime.isPrime(i):
            lPrimes.append(i)
    print lPrimes
    for prim in lPrimes:
        a = 1
        if prim <= math.sqrt(n):
           a = math.floor(math.log(n)/math.log(prim))           
        rez = rez * prim ** a
    return rez

def isEvenlyDivisible(n,m):
    for i in range(1,m+1):
        if n%i != 0:            
            return False
    return True
def calcMinEvenlyDiv(n):
    i = 1
    while 1:
        if isEvenlyDivisible(i,n):
            print i
            break
        i = i + 1
if __name__ == "__main__":
    print calcMinEvenlyDivImproved(30)
