'''
Created on 18. mar. 2019

@author: Martinskole
'''
'''
Created on 12. mar. 2019

@author: Abhijat
'''
import numpy as np
from math import exp, sin, pi
import matplotlib.pyplot as plt

def solveNextTimestepFTCS(Uold, D, T_b=1, T_t=0):
    """ Method that solves the transient couetteflow using the FTCS-scheme..
        At time t=t0 the plate starts moving at y=0
        The method solves only for the next time-step.
        The Governing equation is:
        
        du/dt = d^2(u)/dx^2 , u = u(y,t), 0 < y < 1
        
        Boundary conditions: u(0, t) = 1, u(1, t) = 0
        
        Initial condition: u(t, 0) = 0 t<0,  u(t, 0) = 1 t>0
        
        Args:
            uold(array): solution from previous iteration
            D(float): Numerical diffusion number
            
        Returns:
            unew(array): solution at time t^n+1
    """
    Tnew = np.zeros_like(Told)
    
    Told_plus = Told[2:]
    Told_minus = Told[:-2]
    Told_mid = Told[1:-1]
    
    Tnew[1:-1] = D*(Told_plus + Told_minus) + (1 - 2*D)*Told_mid
    Tnew[0] = T_b
    Tnew[-1] = T_t
    
    return Tnew


r = 0.50 # numerical diffusion number

N = 100 
x = np.linspace(0, 1, N + 1)
h = x[1] - x[0]
dt = r*h**2
T = 0.4 # simulation time
time = np.arange(0, T + dt, dt)

# Spatial BC
T_L = 100. # MTst be 1 for analytical solution
T_R = 0. # Must be 0 for analytical solution

# solution matrices:
T = np.zeros((len(time), N + 1))
T[0, 0] = T_L   # no slip condition at the plate boTndary
T[0,-1] = T_R 


plt.figure()
plt.plot(x,T[0,:])


for n, t in enumerate(time[1:]):
    
    Told = T[n, :]
    
    T[n + 1, :] = solveNextTimestepFTCS(Told, r, T_b=T_L, T_t=T_R)
    
    plt.plot(x,T[n+1, :])
    plt.pause(0.0000000001)
    plt.clf()

plt.show()


