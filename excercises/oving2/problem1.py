'''
Created on 22. jan. 2019

@author: Martinskole
'''
from math import sqrt,pi,e
import matplotlib.pylab as plt
import numpy as np
from scipy.special import erf

N = 100
y_0= 0
x = np.linspace(0, 1.5, N + 1)
y=0

dy=1-3*x+y+x**2+x*y

y_newton = x-x**2+x**3/3-x**4/6+x**5/30-x**6/45
y_analytical = 3*np.sqrt(2*pi*e)*np.exp(x*(1+(x/2)))*(erf(sqrt(2)*(1+x)/2)-erf(np.sqrt(2)/2))+4*(1-np.exp(x*(1+x/2)))-x




h = x[1] - x[0] # steplength
Y2 = np.zeros_like(x) # vector for storing y values
Y2[0] = y_0 # first element of y = y(0)

for n in range(N):
    dy = 1-3*x[n]+Y2[n]+x[n]**2+x[n]*Y2[n]
    Y2[n + 1] = Y2[n] + h*dy



plt.figure()

plt.plot(x, y_analytical,color="blue")
plt.plot(x, y_newton,color="red")
plt.plot(x, Y2,color="green")

plt.legend(['Analytical', 'Newton','Euler'], loc='best', frameon=False)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, which='both')

plt.show()