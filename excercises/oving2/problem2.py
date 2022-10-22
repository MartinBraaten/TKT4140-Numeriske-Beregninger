'''
Created on 22. jan. 2019

@author: Martinskole
'''
from math import pi, sin
import numpy as np
import matplotlib.pylab as plt

#    theta''+my/m*theta'+g/l*theta=0

my= 1
m= 1
g= 9.81
l= 1
theta_0 = 2*pi*85/360      #    r=2pi*theta/360
dtheta_0 = 0
ddtheta_0 = -g/l*sin(theta_0)


N = 1000
t = np.linspace(0, 10, N + 1)
h = t[1] - t[0] # steplength
y0_0 = theta_0 # initial condition
y1_0 = 0

Y2 = np.zeros((2, N + 1)) # 2D array for storing y values

Y2[0, 0] = y0_0 # apply initial conditions
Y2[1, 0] = y1_0


for n in range(N):
    y0_n = Y2[0, n]
    y1_n = Y2[1, n]
    
    Y2[0, n + 1] = y0_n + h*y1_n
    Y2[1, n + 1] = y1_n + h*((-my/m*y1_n)+(-g/l*sin(y0_n)))

thetha = Y2[0, :]


# change default values of plot to make it more readable
LNWDT=2; FNT=15
plt.rcParams['lines.linewidth'] = LNWDT
plt.rcParams['font.size'] = FNT

plt.figure()
plt.plot(t, thetha)

plt.legend([r'euler'], loc='best', frameon=False)
plt.xlabel('t')
plt.ylabel(r'$\theta$')
plt.show()