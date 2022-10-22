'''
Created on 31. jan. 2020

@author: Martinskole
'''

import matplotlib.pylab as plt
import numpy as np

P = 50000
k = 27000
c = 900
m = 3000
T_0 = 4
w_0 = np.pi/2

w_r = np.sqrt(k/m)
ksi = c/(2*np.sqrt(2*m))

beta1 = w_0/w_r
beta0 = 0
beta11= -beta1

u = complex(0,1)

F = P*(2*np.exp(u*w_0)-np.exp(2*u*w_0)+np.exp(-2*u*w_0)-2*np.exp(-u*w_0))/(4*u*w_0)
t = np.linspace(-3,7,1001)

H1 = 1/(k*((1-beta1**2)+(2*beta1*ksi)))
H0 = 0
H11 = 1/(k*((1-beta11**2)+(2*beta11*ksi)))

p = F*(-H11*np.exp(-u*w_0*t)+H1*np.exp(u*w_0*t))
P = F*(-np.exp(-u*w_0*t)+np.exp(u*w_0*t))

plt.plot(t,p)
plt.xlabel("t")
plt.ylabel("v [m]")
plt.show()

plt.plot(t,P)
plt.xlabel("t")
plt.ylabel("P [N]")
plt.show()
