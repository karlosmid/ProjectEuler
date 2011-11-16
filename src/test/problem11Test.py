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

    def testGridCoordinatesUnknownMove(self):
        self.assertRaises(TypeError, self.grid.areGridCoordinatesInBoundaries,('desno',19,19))
    def testGridCoordinatesBothAreInBoundariesForRightMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('right',19,19),True)
    def testGridCoordinatesXNotInBoundariesForRightMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('right',20,19),False)
    def testGridCoordinatesYNotInBoundariesForRightMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('right',19,190),True)
    def testGridCoordinatesBothAreInBoundariesForRightDownMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('right-down',19,19),True)
    def testGridCoordinatesYNotInBoundariesForRightDownMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('right-down',19,20),False)
    def testGridCoordinatesBothAreNotInBoundariesForRightDownMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('right-down',20,20),False)
    def testGridCoordinatesBothAreInBoundariesForDownMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('down',19,19),True)
    def testGridCoordinatesYNotInBoundariesForDownMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('down',19,20),False)
    def testGridCoordinatesXNotInBoundariesForDownMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('down',20,19),True)
    def testGridCoordinatesBothAreInBoundariesForLeftDownMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('left-down',0,0),True)
    def testGridCoordinatesBothAreNotInBoundariesForLeftDownMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('left-down',-1,-1),False)
    def testGridCoordinatesXNotInBoundariesForLeftDownMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('left-down',-1,19),False)
    def testGridCoordinatesBothAreInBoundariesForLeftMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('left',0,0),True)
    def testGridCoordinatesXNotInBoundariesForLeftMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('left',-1,0),False)
    def testGridCoordinatesYNotInBoundariesForLeftMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('left',0,-1),True)
    def testGridCoordinatesBothAreInBoundariesForLeftUpMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('left-up',0,0),True)
    def testGridCoordinatesBothNotInBoundariesForLeftUpMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('left-up',-1,-1),False)
    def testGridCoordinatesYNotInBoundariesForLeftUpMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('left-up',0,-1),False)
    def testGridCoordinatesBothAreInBoundariesForUpMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('up',0,0),True)
    def testGridCoordinatesXNotInBoundariesForUpMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('up',-1,0),True)
    def testGridCoordinatesYNotInBoundariesForUpMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('up',0,-1),False)
    def testGridCoordinatesBothAreInBoundariesForUpRightMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('up-right',0,0),True)
    def testGridCoordinatesXIsNotInBoundariesForUpRightMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('up-right',20,0),False)
    def testGridCoordinatesYNotInBoundariesForUpRightMove(self):
        self.assertEqual(self.grid.areGridCoordinatesInBoundaries('up-right',0,-1),False)

    def testUpdateGridCoordinateRight(self):
        self.assertEqual(self.grid.updateGridCoordinate('right',[0,0]),[1,0])
    def testUpdateGridCoordinateRightDown(self):
        self.assertEqual(self.grid.updateGridCoordinate('right-down',[0,0]),[1,1])
    def testUpdateGridCoordinateDown(self):
        self.assertEqual(self.grid.updateGridCoordinate('down',[0,0]),[0,1])
    def testUpdateGridCoordinateLeftDown(self):
        self.assertEqual(self.grid.updateGridCoordinate('left-down',[0,0]),[-1,1])
    def testUpdateGridCoordinateLeft(self):
        self.assertEqual(self.grid.updateGridCoordinate('left',[0,0]),[-1,0])
    def testUpdateGridCoordinateLeftUp(self):
        self.assertEqual(self.grid.updateGridCoordinate('left-up',[0,0]),[-1,-1])
    def testUpdateGridCoordinateUp(self):
        self.assertEqual(self.grid.updateGridCoordinate('up',[0,0]),[0,-1])
    def testUpdateGridCoordinateUpRight(self):
        self.assertEqual(self.grid.updateGridCoordinate('up-right',[0,0]),[1,-1])
    def testUpdateGridCoordinateUnknownDirection(self):
        self.assertRaises(TypeError, self.grid.updateGridCoordinate,('mili',[0,0],[1,-1]))

if __name__ == '__main__':
    unittest.main()

