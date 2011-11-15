# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Nov 15, 2011 9:18:19 PM$"

def goRight(product,grid20with20,gridCoordinate,currentDepth):    
    x = gridCoordinate[0]
    y = gridCoordinate[1]
    if x > 19:
            return 0
    if depth < 4:
        product = product * grid20with20[x][y]
        x +=1
        gridCoordinate[0] = x
        goRight(product,grid20with20,gridCoordinate,currentDepth+1)
    elif depth == 4:
        product = product * grid20with20[x][y]
        return product
def parseInput(dataFilePath):
    grid20with20 = []
    f = open(dataFilePath,'r')
    for item in f:
        item = item.replace('\n','')
        line = item.split(' ')
        grid20with20.append(line)
    f.close()
    return grid20with20

if __name__ == "__main__":
    a = parseInput('data11.txt')
    print a[19][19]