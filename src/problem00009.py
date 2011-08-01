# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 25, 2011 6:13:28 PM$"

import math


def pythagorean(s):
    b = 0.3*s
    while b < s:
        a = s*(2*b - s)/(2*(b - s))
        if a%10 == 0 and a > 0:
            yield b
        b = b + 1
if __name__ == "__main__":    
    s = 1000*1000*1000
    for b in pythagorean(s):
        a = s*(2*b - s)/(2*(b - s))
        c = math.sqrt(a*a+b*b)
        print 'a='+str(a),'a='+str(b),'c='+str(c),a+b+c,a*b*c
