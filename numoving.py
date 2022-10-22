__author__ = 'Martinskole'
# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt


k=1
m=4
x0=1
v0=1
dt=0.01
antallsteg=10000
x=np.zeros(antallsteg-1)
v=np.zeros(antallsteg-1)
tid=np.zeros(antallsteg-1)
x[0]=x0
v[0]=v0
i=0

while tid[i]==(dt(antallsteg-1)):
    i=1
    f=-k*x[i-1]
    dv=f/m*dt
    v[i]=v[i-1]*dv
    x[i]=x[i-1]*dx
    tid[i]=tid[i-1]*dt


np.array(x)
np.array(y)
plt.xlabel('Tid (s)')
plt.ylabel('θ (grader)')
plt.title('Starthastighet = 1 m/s')
plt.plot(x,y)
plt.show()