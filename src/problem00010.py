# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 25, 2011 6:13:28 PM$"

class SieveAlgorithm:


    def __init__(self,calculatePrimesUpTo):
        self.calculatePrimesUpTo = calculatePrimesUpTo
        self.numberOfOddNumbers = (self.calculatePrimesUpTo -1)/2
        import math
        self.OddSieveMagicNumber = int(math.sqrt(calculatePrimesUpTo)-1)/2
        self.SieveMagicNumber = int(math.sqrt(self.calculatePrimesUpTo)+1)
        self.listOfIndexForOddNumbers = []
        self.listOfCrossedPrimes = []
        self.initOddNumbersAllCrosed()
        self.initNumbers()
        
    
    def initOddNumbersAllCrosed(self):
        i = 1        
        while i <= self.numberOfOddNumbers:
            self.addCrosed(self.listOfIndexForOddNumbers)
            i = i + 1
            
            
    def initNumbers(self):
        self.addUnCrosed(self.listOfCrossedPrimes)
        self.addUnCrosed(self.listOfCrossedPrimes)
        self.addCrosed(self.listOfCrossedPrimes)
        i = 3
        while i < self.calculatePrimesUpTo+1:
            if self.isEven(i):
                self.addUnCrosed(self.listOfCrossedPrimes)
            else:
                self.addCrosed(self.listOfCrossedPrimes)
            i = i + 1


    def addCrosed(self,list):
        list.append(False)


    def addUnCrosed(self,list):
        list.append(True)


    def isEven(self,number):
        if number%2 == 0:
            return True
        else:
            return False


    def usingOnlyOddNumbers(self):
        self.unCrossNotPrimesInNumbers()
        return self.calcSumOfPrimes()


    def unCrossNotPrimesInNumbers(self):
        OddSieveMagicNumberRange = range(1, self.OddSieveMagicNumber+1)
        for i in OddSieveMagicNumberRange:
            if self.isCrosed(self.listOfIndexForOddNumbers[i-1]):
                j = self.calcSquareIndexForOddNumberFromIndex(i)
                while j <= self.numberOfOddNumbers:
                    self.unCross(self.listOfIndexForOddNumbers,j-1)
                    j = j + self.calcOddFromIndex(i)


    def isCrosed(self,number):
        if not number:
            return True
        else:
            return False


    def calcSquareIndexForOddNumberFromIndex(self,i):
        return 2*i*(i+1)    


    def calcOddFromIndex(self,i):
        return 2*i+1


    def calcSumOfPrimes(self):
        sumOfPrimeNumbers = 0
        onlyEvenPrimeNumber = 2
        sumOfPrimeNumbers = sumOfPrimeNumbers + onlyEvenPrimeNumber
        i = 1
        for elem in self.listOfIndexForOddNumbers:
            if self.isCrosed(elem):
                sumOfPrimeNumbers = sumOfPrimeNumbers + self.calcOddFromIndex(i)
            i = i + 1
        return sumOfPrimeNumbers    


    def usingSieve(self):
        for i in range(3,self.SieveMagicNumber):
            if self.isCrosed(self.listOfCrossedPrimes[i]):
                j = i*i
                while j < self.calculatePrimesUpTo:
                    self.unCross(self.listOfCrossedPrimes,j)
                    j = j + i
        sum = 0
        i = 0
        for i in range(2,len(self.listOfCrossedPrimes)):
            if self.isCrosed(self.listOfCrossedPrimes[i]):
                sum = sum + i
        return sum


    def cross(self,list,index):
        list[index] = False


    def unCross(self,list,index):
        list[index] = True


    def sumPrimesByBruteForce(self):
        import problem00003
        sum = 0
        i = 2
        while i<=self.calculatePrimesUpTo:
            if problem00003.isPrime(i):
                sum = sum + i                
            i += 1
        return sum
        

if __name__ == "__main__":
    sieveImproved = SieveAlgorithm(10)
    print sieveImproved.usingOnlyOddNumbers()
    print sieveImproved.listOfIndexForOddNumbers
    print sieveImproved.sumPrimesByBruteForce()
    print sieveImproved.usingSieve()
    #142913828922
    #149070583624
