'''
Created on 14. jan. 2019

@author: Martinskole
'''
from mpmath import fibonacci

print("Tast inn nr paa hvor mange fibonacci tall du vil ha: ")
n = input()

def fib(n):
    h=1
    for h in range(1,n+1,1):
        i=fib2(h)
        print "Fibonaccitall nr",h,":", i
        

def fib2(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)
    

fib(n)


