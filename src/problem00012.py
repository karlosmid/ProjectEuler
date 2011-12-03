# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Dec 1, 2011 9:18:19 PM$"

import problem00010

class TriangleNumber:
    #http://projecteuler.net/problem=12, need to register on home page.

    def calcTriangle(self,n):
        return n*(n+1)/2

    def calcNumberOfDivisorsUsingPrimes(self,n):                
        if n == 1:
            return 1
        elif n == 2:
            return 2
        triangleNumber = self.calcTriangle(n)
        noOfDivisors = 1
        sieveImproved = problem00010.SieveAlgorithm(n)
        lOfPrimes = sieveImproved.listOfIndexForOddNumbers        
        index = 1
        for prime in lOfPrimes:
            if sieveImproved.isCrosed(prime):
                prime = sieveImproved.calcOddFromIndex(index)
                primeExponent = 0
                triangleNumberTmp = triangleNumber
                while triangleNumberTmp%prime == 0:
                    primeExponent = primeExponent + 1
                    triangleNumberTmp = triangleNumberTmp/prime
                noOfDivisors = (primeExponent + 1) * noOfDivisors
            index = index + 1
        return noOfDivisors + 2


    def calcNumberOfDivisors(self,n):        
        if n == 1:
            return 1
        elif n == 2:
            return 2
        noOfDivisors = 2
        triangleNumber = self.calcTriangle(n)
        upperLimit = n/2 + 1
        for num in range(2,upperLimit+1):
             if triangleNumber%num == 0:            
                 noOfDivisors = noOfDivisors + 2                 
        return noOfDivisors    
    def findFirstTriangleNumberWithGraterNumberOfDivisors(self,noOfDivisorsEdge):
        n = 1
        #noOfDivisors = self.calcNumberOfDivisors(1)
        noOfDivisors = self.calcNumberOfDivisorsUsingPrimes(1)
        while noOfDivisors < noOfDivisorsEdge:
            n = n + 1
#            noOfDivisors = self.calcNumberOfDivisors(n)
            noOfDivisors = self.calcNumberOfDivisorsUsingPrimes(n)
        return [self.calcTriangle(n),n,noOfDivisors]

if __name__ == "__main__":
    triangle = TriangleNumber()
    print triangle.calcNumberOfDivisors(4)
#    print triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(5)
    print triangle.calcNumberOfDivisorsUsingPrimes(4)