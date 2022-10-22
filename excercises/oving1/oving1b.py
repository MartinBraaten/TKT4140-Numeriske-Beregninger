'''
Created on 14. jan. 2019

@author: Martinskole
'''
from numpy import array, transpose, linalg
from numpy.linalg._umath_linalg import solve1

a=array([1,2,3])
b=array([4,5,6])
A = array([[1, 1, 2],[2,3,3],[4,4,5]])
B = array([[2,4,6],[8,10,12],[14,16,18]])
inverse_A = linalg.inv(A)

print"a+b =", a+b

print"a*b =", a*b

print"A*B =", A*B

print"A transponert =", transpose(A)

print"A^-1 =", inverse_A

print"Ax=b => x=", solve1(A,b)

