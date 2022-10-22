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
theta_0 = 2*pi*85/360      #    radianer=2pi*theta/360
dtheta_0 = 0
ddtheta_0 = -g/l*sin(theta_0)


N = 100
t = np.linspace(0, 5, N + 1)
h = t[1] - t[0] # steplength
y0_0 = theta_0 # initial condition
y1_0 = 0

Y2 = np.zeros((2, N + 1)) # 2D array for storing y values

Y2[0, 0] = y0_0 # apply initial conditions
Y2[1, 0] = y1_0

for n in range(N):
    y0_n = Y2[0, n]
    y1_n = Y2[1, n]

    y0_p = y0_n + h*y1_n
    y1_p = y1_n + h*((-my/m*y1_n)+(-g/l*sin(y0_n)))
    
    Y2[0, n + 1] = y0_n + h/2*(y1_n+y1_p)
    Y2[1, n + 1] = y1_n + h/2*((-my/m*y1_n)+(-g/l*sin(y0_n))+(-my/m*y1_p)+(-g/l*sin(y0_p)))

thetha = Y2[0, :]
dtheta = Y2[1, :]
X_max = []
theta_max = []
period = []
for i in range(N):
    if np.sign(dtheta[i])  != np.sign(dtheta[i+1]):
        #print dtheta[i]
        X_max.append(t[i])
        theta_max.append(thetha[i])
        if len(X_max)>1:
            period.append((X_max[-1]-X_max[-2])*2)
    
print period

# change default values of plot to make it more readable
LNWDT=2; FNT=15
plt.rcParams['lines.linewidth'] = LNWDT
plt.rcParams['font.size'] = FNT

plt.figure()
plt.plot(t, thetha)
plt.plot(t, dtheta)
plt.plot(X_max, theta_max, "o")

plt.legend(['Heuns','d'], loc='best', frameon=False)
plt.xlabel('t')
plt.ylabel(r'$\theta$')
plt.show()