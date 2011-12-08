# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Dec 1, 2011 9:18:19 PM$"

import problem00010

class TriangleNumber:
    #http://projecteuler.net/problem=12, need to register on home page.

    def __init__(self):
        self.sieveImproved = None
        self.lOfCrossedPrimes = []

    def calcTriangle(self,n):
        return n*(n+1)/2

    def calcPrimeExponent(self,prime,number):
        primeExponent = 0
        while number%prime == 0:
                primeExponent = primeExponent + 1
                number = number/prime
        return primeExponent

    def calcNumberOfDivisorsUsingBruteForce(self,n):
        triangleNumber = self.calcTriangle(n)
        if triangleNumber > 1:
            noOfDivisors = 2
        else:
            noOfDivisors = 1
        for number in range(2,triangleNumber):
            if triangleNumber % number == 0:
                noOfDivisors = noOfDivisors + 1
        return noOfDivisors

    def calcNumberOfDivisorsUsingPrimes(self,n):
        self.sieveImproved = problem00010.SieveAlgorithm(65500)        
        self.lOfCrossedPrimes = self.sieveImproved.listOfCrossedPrimesWhereIndexIsPrimeValue
        triangleNumber = self.calcTriangle(n)
        noOfDivisors = 1        
#        print self.lOfCrossedPrimes
        primeValue = 0
        for primeCrossedFlag in self.lOfCrossedPrimes:
            if self.sieveImproved.isCrosed(primeCrossedFlag):                
                primeExponent = 0
                primeExponent = self.calcPrimeExponent(primeValue,triangleNumber)
                if primeExponent > 0:
                    noOfDivisors = (primeExponent + 1) * noOfDivisors
            primeValue = primeValue + 1
        return noOfDivisors


    def calcNumberOfDivisors(self,n):        
        if n == 1:
            return 1
        elif n == 2:
            return 2
#        noOfDivisors = 2
        noOfDivisors = 0
        triangleNumber = self.calcTriangle(n)
#        upperLimit = n/2 + 1
        upperLimit = n
        for num in range(1,upperLimit + 1):
             if triangleNumber%num == 0:            
                 if triangleNumber/num > n:
                     noOfDivisors = noOfDivisors + 2
                 else:
                     noOfDivisors = noOfDivisors + 1
        return noOfDivisors    
    def findFirstTriangleNumberWithGraterNumberOfDivisors(self,noOfDivisorsEdge,algorithm):
        n = 1
        noOfDivisors = algorithm(n)
        while noOfDivisors < noOfDivisorsEdge:
            n = n + 1
            noOfDivisors = algorithm(n)
        return [self.calcTriangle(n),n,noOfDivisors]

if __name__ == "__main__":
    triangle = TriangleNumber()
#    print triangle.calcNumberOfDivisors(53)
    print triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(50,triangle.calcNumberOfDivisorsUsingPrimes)
    print triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(50,triangle.calcNumberOfDivisorsUsingBruteForce)
    print triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(50,triangle.calcNumberOfDivisors)
#    print triangle.calcNumberOfDivisorsUsingPrimes(53)