# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest
import problem00012


class  Problem12TestCase(unittest.TestCase):
    def setUp(self):
        self.triangle = problem00012.TriangleNumber()
    

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None
    
    def testImprovedNumberOfDivisorsAgainstBruteForce(self):
        for n in range(101,600):
            self.assertEqual(self.triangle.calcNumberOfDivisorsUsingBruteForce(n),
                             self.triangle.calcNumberOfDivisors(n))

    def testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingBruteForce(self):
        result = self.triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(50,
        self.triangle.calcNumberOfDivisorsUsingBruteForce)
        self.assertEqual([25200, 224, 90],result)
    def testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingImprovedAlgorithm(self):
        result = self.triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(50,
        self.triangle.calcNumberOfDivisors)
        self.assertEqual([25200, 224, 90],result)
    def testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingPrimeNumbers(self):
        result = self.triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(50,
        self.triangle.calcNumberOfDivisorsUsingPrimes)
        self.assertEqual([25200, 224, 90],result)
    def testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingImprovedAlgorithmSolution(self):
        result = self.triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(500,
        self.triangle.calcNumberOfDivisors)
        self.assertEqual([76576500, 12375, 576],result)

if __name__ == '__main__':
    unittest.main()

