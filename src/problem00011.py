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
        x = gridCoordinate[0]
        y = gridCoordinate[1]        
        if self.areGridCoordinatesInBoundaries(x,y):
            if currentDepth < self.depth:                
                gridCoordinate = self.updateGridCoordinate(direction,gridCoordinate)                
                return int(self.grid[x][y]) * self.goTo(direction,gridCoordinate,currentDepth+1)
            elif currentDepth == self.depth:                
                return int(self.grid[x][y])
        else:
            return 0


    def areGridCoordinatesInBoundaries(self,x,y):
        
        if y > self.noOfGridColumns - 1 or y < 0:
            return False
        elif x > self.noOfGridRows - 1 or x < 0:
            return False
        return True


    def updateGridCoordinate(self,direction,gridCoordinate):
        if direction == 'right':
            gridCoordinate[1] +=1
        elif direction == 'right-down':
            gridCoordinate[1] +=1
            gridCoordinate[0] +=1
        elif direction == 'down':
            gridCoordinate[0] +=1
        elif direction == 'left-down':
            gridCoordinate[1] -=1
            gridCoordinate[0] +=1
        elif direction == 'left':
            gridCoordinate[1] -=1
        elif direction == 'left-up':
            gridCoordinate[1] -=1
            gridCoordinate[0] -=1
        elif direction == 'up':
            gridCoordinate[0] -=1
        elif direction == 'up-right':
            gridCoordinate[1] +=1
            gridCoordinate[0] -=1
        elif direction not in self.directions:
            raise TypeError('Unknown direction!')
        return gridCoordinate

    def maxProductUsingExaustiveParseThroughGrid(self):
        max = 1
        for i in xrange(self.noOfGridColumns):
            for j in xrange(self.noOfGridRows):
               for direction in self.directions:
                   product = self.goTo(direction,[i,j],1)
                   if product > max:
                       max = product
        return max


if __name__ == "__main__":
    grid = GoThroughGrid('data11.txt',4,20,20)
    print grid.maxProductUsingExaustiveParseThroughGrid()