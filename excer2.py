'''
Created on 29. apr. 2020

@author: Martinskole
'''
import numpy as np
import matplotlib.pylab as plt
from math import pi, sqrt, exp
import scipy

# problem 1


y_0 = 0
N = 1000
x = np.linspace(0, 1.5, N+1)
y = np.zeros_like(x)
y[0] = y_0
h = x[1] - x[0]


y_der = 1 - 3*x + y + x**2 +x*y

y_newton = x - x**2 + x**3/3 - x**4/6 + x**5/30 - x**6/45

#y_correct = 3*sqrt(2*pi*exp) * exp(x*(1+x/2)) * (scipy.special.erf(sqrt(2)*(1+x)/2) - scipy.special.erf(sqrt(2)/2) + 4*(1-exp(x*(1+x/2)))) - x

for n in range(N):
    f = y_der[n]
    y_der[n+1] = y_der[n] + h*f

plt.figure()
#plt.plot(x, y_correct, 'b', linewidth=2.0)
plt.plot(x, y_der, linewidth=2.0)
plt.xlabel('x')
plt.ylabel('y')
#plt.savefig('../fig-ch1/euler_simple.png', transparent=True)
plt.show()



