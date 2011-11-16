# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Nov 15, 2011 9:18:19 PM$"

class GoThroughGrid:
    def __init__(self,gridDataFilePath,depth,noOfGridRows,noOfGridColumns):
        self.grid = self.parseInput(gridDataFilePath)
        self.noOfGridRows = noOfGridRows
        self.noOfGridColumns = noOfGridColumns
        self.depth = depth
        self.directions = ['right','right-down','down','left-down','left','left-up','up','up-right']


    def parseInput(self,dataFilePath):
        grid = []
        file = open(dataFilePath,'r')
        for line in file:
            line = line.replace('\n','')
            lineAsList = line.split(' ')
            grid.append(lineAsList)
        file.close()
        return grid

    
    def goTo(self,direction,gridCoordinate,currentDepth):
        print gridCoordinate
        x = gridCoordinate[0]
        y = gridCoordinate[1]
        if self.areGridCoordinatesInBoundaries(direction,x,y):
            if currentDepth < self.depth:                
                return int(self.grid[x][y]) * self.goTo(direction,self.updateGridCoordinate(direction,gridCoordinate),currentDepth+1)
            elif currentDepth == self.depth:                
                return int(self.grid[x][y])
        else:
            return 0


    def areGridCoordinatesInBoundaries(self,direction,x,y):
        if direction == 'right':
            if x > self.noOfGridColumns:
                return False
        elif direction == 'right-down':
            if x > self.noOfGridColumns or y > self.noOfGridRows:
                return False
        elif direction == 'down':
            if y > self.noOfGridRows:
                return False
        elif direction == 'left-down':
            if x < 0 or y > self.noOfGridRows:
                return False
        elif direction == 'left':
            if x < 0:
                return False
        elif direction == 'left-up':
            if x < 0 or y < 0:
                return False
        elif direction == 'up':
            if y < 0:
                return False
        elif direction == 'up-right':
            if x > self.noOfGridColumns or y < 0:
                return False
        elif direction not in self.directions:
            raise TypeError('Unknown direction!')
        return True


    def updateGridCoordinate(self,direction,gridCoordinate):
        if direction == 'right':
            gridCoordinate[0] =+1
        elif direction == 'right-down':
            gridCoordinate[0] =+1
            gridCoordinate[1] =+1
        elif direction == 'down':
            gridCoordinate[1] =+1
        elif direction == 'left-down':
            gridCoordinate[0] =-1
            gridCoordinate[1] =+1
        elif direction == 'left':
            gridCoordinate[0] =-1
        elif direction == 'left-up':
            gridCoordinate[0] =-1
            gridCoordinate[1] =-1
        elif direction == 'up':
            gridCoordinate[1] =-1
        elif direction == 'up-right':
            gridCoordinate[0] =+1
            gridCoordinate[1] =-1
        elif direction not in self.directions:
            raise TypeError('Unknown direction!')
        return gridCoordinate

    def maxProductUsingExaustiveParseThroughGrid(self):
        max = 1
        for i in xrange(self.noOfGridColumns):
            for j in xrange(self.noOfGridRows):
               for direction in self.directions:
                   product = self.goTo(direction,[i,j],0)                   
                   if product > max:
                       max = product
        return max


if __name__ == "__main__":
    grid = GoThroughGrid('data11.txt',4,20,20)
    print grid.maxProductUsingExaustiveParseThroughGrid()