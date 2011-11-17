# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest
import problem00011


class  Problem11TestCase(unittest.TestCase):
    def setUp(self):
        self.grid = problem00011.GoThroughGrid('../data11.txt',4,20,20)
    

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None
    
    def testGridCoordinatesXToLarge(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries(20,19),False)
    def testGridCoordinatesYToLarge(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries(8,20),False)
    def testGridCoordinatesXToSmall(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries(-2,19),False)
    def testGridCoordinatesYToSmall(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries(8,-1),False)
    def testGridCoordinatesXYOK(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries(0,0),True)

    def testUpdateGridCoordinateRight(self):
        self.assertEqual(self.grid.updateGridCoordinate('right',[0,0]),[0,1])
    def testUpdateGridCoordinateRightDown(self):
        self.assertEqual(self.grid.updateGridCoordinate('right-down',[0,0]),[1,1])
    def testUpdateGridCoordinateDown(self):
        self.assertEqual(self.grid.updateGridCoordinate('down',[0,0]),[1,0])
    def testUpdateGridCoordinateLeftDown(self):
        self.assertEqual(self.grid.updateGridCoordinate('left-down',[0,0]),[1,-1])
    def testUpdateGridCoordinateLeft(self):
        self.assertEqual(self.grid.updateGridCoordinate('left',[0,0]),[0,-1])
    def testUpdateGridCoordinateLeftUp(self):
        self.assertEqual(self.grid.updateGridCoordinate('left-up',[0,0]),[-1,-1])
    def testUpdateGridCoordinateUp(self):
        self.assertEqual(self.grid.updateGridCoordinate('up',[0,0]),[-1,0])
    def testUpdateGridCoordinateUpRight(self):
        self.assertEqual(self.grid.updateGridCoordinate('up-right',[0,0]),[-1,1])
    def testUpdateGridCoordinateUnknownDirection(self):
        self.assertRaises(TypeError, self.grid.updateGridCoordinate,('mili',[0,0],[1,-1]))

    def testAnswerToMaxProduct(self):

        self.assertEqual(self.grid.maxProductUsingExaustiveParseThroughGrid(),70600674)

if __name__ == '__main__':
    unittest.main()

