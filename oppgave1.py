'''
Created on 24. mai 2020

@author: Martinskole
'''

import numpy as np
import matplotlib.pylab as plt
def theta_scheme(u, D, tmin, tmax):

    """Solve using the theta scheme"""

    dt = D*dx**2 # compute timestep

    m = round((tmax-tmin)/dt) # nr. of temporal intervals             

    time = np.linspace(tmin, tmax, m) # time vector

    # create matrix for sparse solver. Solve for interior values only (nx-1)

    diagonals = np.zeros((3,nx+1))

    diagonals[0,:] = -D*theta
    print diagonals[0,:]
    diagonals[1,:] = 1 + 2*D*theta

    diagonals[2,:] = -D*theta

    As = scipy.sparse.spdiags(diagonals, [-1, 0, 1], nx-1, nx-1, format='csc')  # sparse matrix instance

    # create rhs array

    d = np.zeros((nx-1, 1),'d')

    # advance in time and solve tridiagonal system for each t in time

    for t in time:

        d[:] = u[1:-1] + D*(1-theta)*(u[0:-2]-2*u[1:-1]+u[2:])

        d[0] += D*theta*u[0]

        w = scipy.sparse.linalg.spsolve(As,d)

        u[1:-1] = w[:, None]

    return u


r_1 = 0.2
r_2 = 0.5  
r_3 = 1.0
t_1 = 0.001 
t_2 = 0.025 
t_3 = 0.4
 
k = 1
L = 1
N = 5

T = 0.4

x = np.linspace(0,1,N+2)
dx = x[1]-x[0]
dt = r_1*dx**2
t = np.arange(0, T + dt,dt)

A = np.zeros((N+2,len(t)))
A[0,:] = 100
A[-1,:] = 0

plt.figure()
plt.plot(x, A[:,0])


time = np.arange(0, T + dt, dt)


for i, t in enumerate(time[1:]):
    U_old = A[:,i]
    U_new = theta_scheme(U_old, r_1, )
    A[:,i+1] = U_new
    
    
    plt.plot(x,A[:,i])

plt.show()