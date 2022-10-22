'''
Created on 8. mar. 2019

@author: Martinskole
'''
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import scipy.sparse.linalg


#    Boundary conditions: T(0,t)=100 and T(1,t)=0
#    Initial conditions: T(x,0)=0
#def FTCS(U_old):
    #ny = U_old + r_1*(-2*A[:,i]+A[:,i-1]+A[:,i+1])
    #return ny
def solveNextTimestepFTCS(Told, D, T_b=100, T_t=0):
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

# Theta-scheme and using L'hopital for r=0
def thetaSchemeNumpyV1(theta, D, wOld):
    """ Algorithm for solving w^(n+1) for the startup of pipeflow 
        using the theta-schemes. L'hopitals method is used on the 
        governing differential equation for r=0.
        
        Args:
            theta(float): number between 0 and 1. 0->FTCS, 1/2->Crank, 1->Laasonen
            D(float): Numerical diffusion number [dt/(dr**2)]
            N(int): number of parts, or dr-spaces. In this case equal to the number of unknowns
            wOld(array): The entire solution vector for the previous timestep, n.
            
        Returns:
            wNew(array): solution at timestep n+1
    """
    
    N = len(wOld)
    
    superDiag = np.zeros(N - 2)
    subDiag = np.zeros(N - 2)
    mainDiag = np.zeros(N-2)
    
    RHS = np.zeros(N-2)
    tmp = D*(1. - theta)
    
    superDiag[:] = -D*theta*np.ones(N-2)
    mainDiag[:] = np.ones(N-2)*(1 + 2*D*theta)
    subDiag[:] = -D*theta*np.ones(N-2)
    
    a = tmp*wOld[0:-2]
    b = (1-2*tmp)*wOld[1:-1]
    c = tmp*wOld[2:]
    
    RHS[:] = a + b + c
    
    RHS[0] += D*theta*wOld[0]
    RHS[-1] += D*theta*wOld[-1]
    
    A = scipy.sparse.diags([subDiag, mainDiag, superDiag], [-1, 0, 1], (N-2, N-2), format='csc')
    wNew = np.zeros_like(wOld)
    wNew[1:-1] = scipy.sparse.linalg.spsolve(A, RHS)
    wNew[0] = 100
    wNew[-1] = 0
    print A.toarray()
    return wNew

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
'''for i in range(len(t)-1):
    U_old = A[:,i]
    U_new = FTCS(U_old)
    A[:,i+1] = U_new
    
    plt.plot(x,A[:,i])
    plt.pause(0.00000001)
    plt.clf()
'''

time = np.arange(0, T + dt, dt)

for i, t in enumerate(time[1:]):
    U_old = A[:,i]
    U_new = solveNextTimestepFTCS(U_old,r_1)
    A[:,i+1] = U_new
    
    if i > int(T/dt - 10):
        plt.plot(x,A[:,i])
        plt.title(t)
        plt.pause(0.0000000001)
        plt.clf()
plt.show()



for i, t in enumerate(time[1:]):
    U_old = A[:,i]
    U_new = thetaSchemeNumpyV1(0.5, r_1, U_old)
    A[:,i+1] = U_new
    
    
    plt.plot(x,A[:,i])

plt.show()