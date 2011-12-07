# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest
import problem00010


class  Problem10TestCase(unittest.TestCase):


    def setUp(self):
        pass
    

    def tearDown(self):
        pass


    def testInitOddNumbersAllCrosed(self):
        sieve = problem00010.SieveAlgorithm(10)
        expected = [False,False,False,False]
        result = sieve.listOfIndexForOddNumbers
        self.assertListEqual(expected, result)


    def testInitNumbers(self):
        sieve = problem00010.SieveAlgorithm(10)
        expected = [True,True,False,False,True,False,True,False,True,False,True]
        result = sieve.listOfCrossedPrimes
        self.assertListEqual(expected, result)


    def testAddCrosed(self):
        sieve = problem00010.SieveAlgorithm(10)
        expected = [False]
        result = []
        sieve.addCrosed(result)
        self.assertListEqual(expected, result)


    def testAddUnCrosed(self):
        sieve = problem00010.SieveAlgorithm(10)
        expected = [True]
        result = []
        sieve.addUnCrosed(result)
        self.assertListEqual(expected, result)


    def testIsEvenTrue(self):
        sieve = problem00010.SieveAlgorithm(10)
        self.assertEqual(sieve.isEven(2), True)


    def testIsEvenFalse(self):
        sieve = problem00010.SieveAlgorithm(10)
        self.assertEqual(sieve.isEven(5), False)


    def testUusingOnlyOddNumbers10(self):
        sieve = problem00010.SieveAlgorithm(10)
        expected = 17
        self.assertEqual(expected,sieve.usingOnlyOddNumbers())


    def testusingOnlyOddNumbersTwoMillion(self):
        sieve = problem00010.SieveAlgorithm(2*1000*1000)
        expected = 142913828922
        self.assertEqual(expected,sieve.usingOnlyOddNumbers())


    def testUnCrossNotPrimesInNumbers20(self):
        sieve = problem00010.SieveAlgorithm(20)
        expected = [False, False, False, True, False, False, True, False, False]
        sieve.usingOnlyOddNumbers()
        self.assertListEqual(expected,sieve.listOfIndexForOddNumbers)


    def testIsCrosed(self):
        sieve = problem00010.SieveAlgorithm(10)
        expected = False
        result = sieve.isCrosed(True)
        self.assertEqual(expected,result)


    def testCalcSquareForOddNumberFromIndex(self):
        sieve = problem00010.SieveAlgorithm(10)
        expected = 60
        result = sieve.calcSquareIndexForOddNumberFromIndex(5)
        self.assertEqual(expected,result)


    def testCalcOddFromIndex(self):
        sieve = problem00010.SieveAlgorithm(10)
        expected = 11
        result = sieve.calcOddFromIndex(5)
        self.assertEqual(expected,result)


    def testcalcSumOfPrimes(self):
        sieve = problem00010.SieveAlgorithm(11)
        expected = 37
        self.assertEqual(expected,sieve.calcSumOfPrimes())

   
    def testUsingSieve(self):
        sieve = problem00010.SieveAlgorithm(11)
        expected = 28
        result = sieve.usingSieve()
        self.assertEqual(expected,result)


    def testCross(self):
        sieve = problem00010.SieveAlgorithm(11)
        expected = [False]
        result = [True]
        sieve.cross(result,0)
        self.assertEqual(expected,result)


    def testUnCross(self):
        sieve = problem00010.SieveAlgorithm(11)
        expected = [True]
        result = [False]
        sieve.unCross(result,0)
        self.assertEqual(expected,result)


    def testSumPrimesByBruteForce(self):
        sieve = problem00010.SieveAlgorithm(11)
        expected = 28
        result = sieve.sumPrimesByBruteForce()
        self.assertEqual(expected,result)


    def testSideBySideUpToEven(self):
        sieve = problem00010.SieveAlgorithm(28)
        expected = [100,100,100]
        result = []
        result.append(sieve.sumPrimesByBruteForce())
        result.append(sieve.usingSieve())
        result.append(sieve.usingOnlyOddNumbers())
        self.assertListEqual(expected,result)


    def testSideBySideUpToOdd(self):
        sieve = problem00010.SieveAlgorithm(11)
        expected = [28,28,28]
        result = []
        result.append(sieve.sumPrimesByBruteForce())
        result.append(sieve.usingSieve())
        result.append(sieve.usingOnlyOddNumbers())
        self.assertListEqual(expected,result)


    def testSideBySideUpToPair(self):
        sieve = problem00010.SieveAlgorithm(1100)
        expected = [92953,92953,92953]
        result = []
        result.append(sieve.sumPrimesByBruteForce())
        result.append(sieve.usingSieve())
        result.append(sieve.usingSieve())
        self.assertListEqual(expected,result)


        
if __name__ == '__main__':
    unittest.main()

