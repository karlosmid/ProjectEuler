# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 25, 2011 6:13:28 PM$"

if __name__ == "__main__":
    import problem00003
    prime = 0
    i = 2
    while 1:
        if problem00003.isPrime(i):
            prime += 1
            print prime,i
        if prime == 10001:
            print i,
            break
        i += 1
    #104743
