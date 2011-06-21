# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 19, 2011 6:47:28 PM$"

def sumDivBy(total,m):
    #1/2*p*(p+1)    
    p = (total-1)/m
    return m*p*(p+1)/2
def bruteforce(total):
    sum = 0    
    for i in range (3,total):
        if i%3 == 0:
            sum = sum + i
            continue
        if i%5 == 0:
            sum = sum + i
    return sum

if __name__ == "__main__":
    total = 100000000
#    print bruteforce(total)
    print sumDivBy(total,3)+sumDivBy(total,5)-sumDivBy(total,15)
