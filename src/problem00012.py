# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Dec 1, 2011 9:18:19 PM$"

import problem00010

class TriangleNumber:
    #http://projecteuler.net/problem=12, need to register on home page.

    def __init__(self,noOfPrimes):
        self.sieveImproved = None
        self.lOfCrossedPrimes = []
        self.noOfPrimes = noOfPrimes
        self.sieveImproved = problem00010.SieveAlgorithm(self.noOfPrimes)

    def calcTriangle(self,n):
        return n*(n+1)/2

    def calcPrimeExponent(self,prime,number):
        primeExponent = 0
        while number%prime == 0:
                primeExponent = primeExponent + 1
                number = number/prime
        return primeExponent

    def calcNumberOfDivisorsUsingBruteForce(self,n):        
        if n > 1:
            noOfDivisors = 2
        else:
            noOfDivisors = 1
        for number in range(2,n):
            if n % number == 0:
                noOfDivisors = noOfDivisors + 1
        return noOfDivisors

    def calcNumberOfDivisorsUsingPrimes(self,n):        
        self.lOfCrossedPrimes = self.sieveImproved.listOfCrossedPrimesWhereIndexIsPrimeValue        
        noOfDivisors = 1
        primeValue = 0
        for primeCrossedFlag in self.lOfCrossedPrimes:
            if self.sieveImproved.isCrosed(primeCrossedFlag):                
                primeExponent = 0
                primeExponent = self.calcPrimeExponent(primeValue,n)
                if primeExponent > 0:
                    noOfDivisors = (primeExponent + 1) * noOfDivisors
            primeValue = primeValue + 1
        return noOfDivisors

    def calcNumberOfDivisorsForTriangleNumber(self,upToN):
        triangleNumber = self.calcTriangle(upToN)
        if upToN == 1:
            return 1
        elif upToN == 2:
            return 2
        noOfDivisors = 0        
        upperLimit = upToN
        for num in range(1,upperLimit + 1):
             if triangleNumber%num == 0:
                 if triangleNumber/num > upToN:
                     noOfDivisors = noOfDivisors + 2
                 else:
                     noOfDivisors = noOfDivisors + 1
        return noOfDivisors    
    def findFirstTriangleNumberWithGraterNumberOfDivisors(self,noOfDivisorsEdge,noOfDivisorsAlgorithm):
        n = 1
        noOfDivisors = noOfDivisorsAlgorithm(n)
        while noOfDivisors < noOfDivisorsEdge:
            n = n + 1
            if noOfDivisorsAlgorithm.__name__ == 'calcNumberOfDivisorsForTriangleNumber':
                noOfDivisors = noOfDivisorsAlgorithm(n)            
            else:
                noOfDivisors = noOfDivisorsAlgorithm(self.calcTriangle(n))                
        return [self.calcTriangle(n),n,noOfDivisors]

    def findFirstTriangleNumberWithGraterNumberOfDivisorsImprovedPrimes(self,noOfDivisorsEdge):
        n = 1
        noOfDivisors = self.calcNumberOfDivisorsUsingPrimes(n) * self.calcNumberOfDivisorsUsingPrimes((n+1)/2)
        while noOfDivisors < noOfDivisorsEdge:
            n = n + 1            
            if n%2 == 0:
                nPlus1 = self.calcNumberOfDivisorsUsingPrimes(n+1)
                noOfDivisors = self.calcNumberOfDivisorsUsingPrimes(n/2) * nPlus1
            else:
                noOfDivisors = nPlus1 * self.calcNumberOfDivisorsUsingPrimes((n+1)/2)
        return [self.calcTriangle(n),n,noOfDivisors]

if __name__ == "__main__":
    triangle = TriangleNumber(65000)
    triangleImproved = TriangleNumber(1000)
#    print triangle.calcNumberOfDivisors(53)
    print triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(50,triangle.calcNumberOfDivisorsUsingPrimes)
    print triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(50,triangle.calcNumberOfDivisorsUsingBruteForce)
    print triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(50,triangle.calcNumberOfDivisorsForTriangleNumber)
    print triangleImproved.findFirstTriangleNumberWithGraterNumberOfDivisorsImprovedPrimes(50)
#    print triangle.calcNumberOfDivisorsUsingPrimes(53)