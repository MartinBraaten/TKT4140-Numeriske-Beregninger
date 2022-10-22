'''
Created on 14. jan. 2019

@author: Martinskole
'''
from mpmath import fibonacci
import matplotlib.pyplot as plt
import numpy as np
import pylab


print("Tast inn nr paa hvor mange fibonacci tall du vil ha: ")
n = input()
X2 = []
Y2 = []
def fib(n):
    h=1
    for h in range(1,n+1):
        i=fibonacci(h)
        'print "Fibonaccitall nr",h,":", i'
        X2.append(i)
        b=sum(X2)
        'print b'
        Y2.append(b)
    'print Y2'

    plt.plot(Y2)
    plt.semilogy()
    
    plt.legend(['Sum av Fibonacci-tall'], loc='best', frameon=False)
    'plt.plot(block=True)'
    plt.xlabel('x')
    plt.ylabel('y (log)')
    plt.show()


fib(n)
