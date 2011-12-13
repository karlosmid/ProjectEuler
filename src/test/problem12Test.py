# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest
import problem00012


class  Problem12TestCase(unittest.TestCase):
    def setUp(self):
        self.triangle = problem00012.TriangleNumber(65000)
    

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None
    
    def testImprovedNumberOfDivisorsAgainstBruteForce(self):
        for n in range(101,600):
            self.assertEqual(self.triangle.calcNumberOfDivisorsUsingBruteForce(self.triangle.calcTriangle(n)),
                             self.triangle.calcNumberOfDivisorsForTriangleNumber(n))

    def testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingBruteForce(self):
        result = self.triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(50,
        self.triangle.calcNumberOfDivisorsUsingBruteForce)
        self.assertEqual([25200, 224, 90],result)
    def testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingImprovedAlgorithm(self):
        result = self.triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(50,
        self.triangle.calcNumberOfDivisorsForTriangleNumber)
        self.assertEqual([25200, 224, 90],result)
    def testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingPrimeNumbers(self):
        result = self.triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(50,
        self.triangle.calcNumberOfDivisorsUsingPrimes)
        self.assertEqual([25200, 224, 90],result)
    def testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingPrimeNumbersImproved(self):
        triangleImproved = problem00012.TriangleNumber(1000)
        result = triangleImproved.findFirstTriangleNumberWithGraterNumberOfDivisorsImprovedPrimes(50)
        self.assertEqual([25200, 224, 90],result)
    def testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingImprovedAlgorithmSolution(self):
        result = self.triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(500,
        self.triangle.calcNumberOfDivisorsForTriangleNumber)
        self.assertEqual([76576500, 12375, 576],result)
    def testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingPrimes(self):
        result = self.triangle.findFirstTriangleNumberWithGraterNumberOfDivisors(500,
        self.triangle.calcNumberOfDivisorsUsingPrimes)
        self.assertEqual([76576500, 12375, 576],result)
    def testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingPrimesImproved(self):
        triangleImproved = problem00012.TriangleNumber(1000)
        result = triangleImproved.findFirstTriangleNumberWithGraterNumberOfDivisorsImprovedPrimes(500)
        self.assertEqual([76576500, 12375, 576],result)

if __name__ == '__main__':
    suite = unittest.TestSuite()
#    suite.addTest(Problem12TestCase('testImprovedNumberOfDivisorsAgainstBruteForce'))
#    suite.addTest(Problem12TestCase('testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingBruteForce'))
#    suite.addTest(Problem12TestCase('testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingImprovedAlgorithm'))
#    suite.addTest(Problem12TestCase('testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingPrimeNumbers'))
#    suite.addTest(Problem12TestCase('testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingImprovedAlgorithmSolution'))
#    suite.addTest(Problem12TestCase('testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingPrimeNumbersImproved'))
    suite.addTest(Problem12TestCase('testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingPrimes'))
#    suite.addTest(Problem12TestCase('testfindFirstTriangleNumberWithGraterNumberOfDivisorsUsingPrimesImproved'))
    unittest.TextTestRunner(verbosity=2).run(suite)

