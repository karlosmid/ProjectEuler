# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 25, 2011 6:13:28 PM$"


def sumOfSquares(n):
    rez = 0
    for i in n:
        rez += i*i
    return rez

def squareOfSums(n):
    rez = 0
    for i in n:
        rez += i
    return rez*rez
if __name__ == "__main__":
    n = range(101)
    print (squareOfSums(n) - sumOfSquares(n))
