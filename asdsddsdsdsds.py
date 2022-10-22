'''
Created on 23. mai 2020

@author: Martinskole
'''
import numpy as np
from matplotlib.pyplot import *
#------------------------------------------------------------------
LNWDT=3; FNT=11
rcParams['lines.linewidth'] = LNWDT; rcParams['font.size'] = FNT
#------------------------------------------------------------------
def heun(func, z0, xt):
    """The Heun scheme for solution of systems of ODEs.
    z0 is a vector for the initial conditions,
    the right hand side of the system is represented by func which returns
    a vector with the same size as z0 ."""

    z = np.zeros((np.size(xt), np.size(z0)))
    z[0,:] = z0
    zp = np.zeros_like(z0)

    for i, x in enumerate(xt[0:-1]):
        dx = xt[i+1] - xt[i]
        zp = z[i,:] + np.asarray(func(z[i,:],x))*dx   # Predictor step
        z[i+1,:] = z[i,:] + (np.asarray(func(z[i,:],x)) + np.asarray(func(zp,x+dx)))*dx/2.0 # Corrector step

    return z
#------------------------------------------------------------------
def dsfunction(phi0,phi1,s0,s1):
    if (abs(phi1-phi0)>0.0):   
        return -phi1 *(s1 - s0)/float(phi1 - phi0)
    else:
        return 0.0
#------------------------------------------------------------------
def f(z, t):
    """RHS for hanging cable"""
    zout    = np.zeros_like(z)
    zout[:] = [z[1],(w/T)*np.sqrt(1.0+z[0]*z[0])]
    return zout 
#------------------------------------------------------------------
# Physical parameters
#------------------------------------------------------------------
# Distance between two towers
L   = 3.0
# Height of the towers
U_0 = 10.0
U_L = 12.0
# Weight per unit length of the cable
w = 18.0
# Horizontal component of the tension
T = 10.0
#------------------------------------------------------------------
# Numerical parameters
#------------------------------------------------------------------
# Number of steps
N=200
# Discretized independent variable
x = np.linspace(0,L,N+1)
# Boundary value error
beta = U_L # Boundary value at x = L
# maximum number of iterations
nmax = 100
# Tolerance
eps  = 1.0e-10
# Guessed values
s=[-10.0, 20.0]
# Initialize variables
z0    = np.zeros(2)
z0[0] = U_0
z0[1] = s[0]
#------------------------------------------------------------------
# Start numerical procedure
#------------------------------------------------------------------
z    = heun(f,z0,x)
phi0 = z[-1,0] - beta
for n in range(nmax):
    z0[1] = s[1]
    z     = heun(f,z0,x)
    phi1  = z[-1,0] - beta
    ds    = dsfunction(phi0,phi1,s[0],s[1])
    s[0]  = s[1]
    s[1] +=  ds
    phi0  = phi1
    print ('n = {}  s1 = {} and ds = {}'.format(n,s[1],ds))
    if (abs(ds)<=eps):
        print ('Solution converged for eps = {} and s1 ={} and ds = {}. \n'.format(eps,s[1],ds))
        break
#------------------------------------------------------------------
# plot results
#------------------------------------------------------------------
legends=[] # empty list to append legends as plots are generated

plot(x,z[:,0])
legends.append(r'$\theta$')

## Add the labels
legend(legends,loc='best',frameon=False) # Add the legends
ylabel(r'$u(x)$')
xlabel('x')
grid(b=True, which='both', color='0.65',linestyle='-')

show()