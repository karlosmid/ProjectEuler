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
    prime = True
    while 1:
        if i not in [2,3]:
            for j in range(2,i):
                if i%j == 0:
                    prime = False        
        if prime:
            yield i            
        i = i + 1
        prime = True
def isPrime(n):
    """
      >>> is_prime(1)
      True
      >>> is_prime(2)
      True
      >>> is_prime(3)
      True
      >>> is_prime(4)
      False
      >>> is_prime(5)
      True
      >>> is_prime(6)
      False
      >>> is_prime(7)
      True
      >>> is_prime(29)
      True
      >>> is_prime(3003)
      False
      >>> is_prime(13195)
      False
    """
    if n < 0:
        return False
    if n in [1,2,3]:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
    rez = maxPrimeFactor(600851475143)
    while rez != 1:
        print rez,
        rez = maxPrimeFactor(rez)
    
