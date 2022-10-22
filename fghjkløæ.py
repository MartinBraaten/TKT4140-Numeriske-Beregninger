__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np
t = 0
theta = 0
v = 1
dt = 0.001
L = 1
k = 0

def f(theta):
    dv = -9.81*math.sin(theta)*dt
    return dv

def g(v):
    dtheta = (v/L)*dt
    return dtheta

x = []
y = []

while k < 4:
    theta += g(v)
    v += f(theta)
    t += dt
    x.append(t)
    y.append((theta*180)/math.pi)
    if theta/(theta + g(v)) < 0:
        k+= 1


np.array(x)
np.array(y)
plt.xlabel('Tid (s)')
plt.ylabel('θ (grader)')
plt.title('Starthastighet = 1 m/s')
plt.plot(x,y)
plt.show()