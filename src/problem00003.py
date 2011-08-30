# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 24, 2011 5:46:57 PM$"


def maxPrimeFactor(m):
    for i in genPrime():
        if m%i == 0:
           m = m/i
           return m

def genPrime():
    i = 2    
    while 1:
        if i in [2,3]:
            yield i
        if isPrime(i):
            yield i            
        i = i + 1        
def isPrime(n):
    """
      >>> isPrime(1)
      True
      >>> isPrime(2)
      True
      >>> isPrime(3)
      True
      >>> isPrime(4)
      False
      >>> isPrime(5)
      True
      >>> isPrime(6)
      False
      >>> isPrime(7)
      True
      >>> isPrime(29)
      True
      >>> isPrime(3003)
      False
      >>> isPrime(13195)
      False
      >>> isPrime(104743)
      True
    """
    import math
    if n < 0:
        return False
    if n in [1,2,3]:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    number = 600851475143
    rez = maxPrimeFactor(number)
    while rez != 1:
        print rez,
        rez = maxPrimeFactor(rez)
    
