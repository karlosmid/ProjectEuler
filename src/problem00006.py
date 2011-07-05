# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 25, 2011 6:13:28 PM$"


def sumOfSquares(n):    
    return (n/6.)*(2*n+1)*(n+1)

def squareOfSums(n):        
    #euler
    sum = n*(n+1)/2
    return sum*sum
if __name__ == "__main__":
    n = 1000
    print (squareOfSums(n) - sumOfSquares(n))
