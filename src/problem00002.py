# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 21, 2011 7:24:58 PM$"

def useFibEven(max):
    sum = 0
    for i in fibEven():
        if i > max:
            break        
        sum = sum + i
#        print i,
    print sum
def useFib(max):
    sum = 0
    for i in fib():
        if i > max:
            break
        if i%2 == 0:
#            print i
            sum = sum + i
#        print i,
    print sum
def fibEven():
    a, b = 0, 2
    while 1:
        yield b
        a, b = b, a+4*b
def fib():
    a, b = 1, 1    
    while 1:
        yield b    
        a, b = b, a+b

if __name__ == "__main__":    
    m = 4*1000*1000*1000
    useFib(m)
    useFibEven(m)
