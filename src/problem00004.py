# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 25, 2011 6:13:28 PM$"

def isPalindromNumber(n):
    l = list(str(n))    
    d = len(l)
    for index in range(0,d/2):
        if l[index] != l[d-1-index]:
            return False
    return True
def genPalindromNumber():
    i = 10
    while 1:
        i = i + 1
        l = list(str(i))
        palindrom = True
        d = len(l)
        for index in range(0,d/2):
            if l[index] != l[d-1-index]:
                palindrom = False
                break
        if palindrom:
            yield i
if __name__ == "__main__":
    palindrom = 0
    i = 999
    j = 999
    while i > 99:
        if i%11 == 0:
            j = 999
            dj = 1
        else:
            j = 990
            dj = 11
        while j > 99:
            if i >= j and isPalindromNumber(i*j):
                print i,j,i*j
                if palindrom < i*j:
                    palindrom = i*j
            j = j - dj
        i = i - 1        
    print palindrom
