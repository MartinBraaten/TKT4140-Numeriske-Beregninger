'''
Created on 3. apr. 2020

@author: Martinskole
'''


import numpy as np
def f(x):    
    """Assigning a value of 1.0 for values less than 0.1"""    
    f = np.zeros_like(x)    
    f[np.where((x>=2) &(x <= 3))] = 1.0    
    return f
def upwind(u, a_0, dx, dt):    
    """ implementation of the upwind scheme        
    Args:            
    u (array): solution at current time-step (length N)            
    a_0 (float): wave speed            
    dx (float): spatial discretization step            
    dt (floa): temporal discretization step        
    Returns:            
    u (array): solution of the interior nodes (excluding BCs) at next time-step (length N - 2)    """
    ####################    
    ####################    
    # fill in here!!!! (implement upwind scheme)  
    C = a_0*dt/dx
    if a_0 <=0:
        u[1:-1] = u[1,-1] - C*(u[:-2] - u[1:-1])
    else: 
        u[1:-1] = u[1,-1] - C*(u[1:-1] - u[2:])    
        
    return u
##################### 
# discretization
####################
N = 101 # number of nodes in spatial direction
x_start, x_end = 0, 5
x = np.linspace(x_start, x_end, N)
dx = # fill in here!!!! (evaluate spatial discretization step)
a_0 = -1
c_abs = 0.8
c = np.sign(a_0)*c_abs
dt = # fill in here (calculate time-step)
T = 2t = np.arange(0, T + dt, dt)
####################
# creation of matrices for storing solutions
####################
U_sol = np.zeros((len(t), N))
U_sol_analytical = np.zeros((len(t), N))
####################
# apply initial solution
####################
U_sol[0, :] = # fill in here!!!! (set the initial solution at t=0)
U_sol_analytical[0,:] = # fill in here!!!! (evaluate analytical solution at t=0)
####################
# solving loop
####################
for n in range(len(t) - 1):    
    u = # fill in here!!!! (retrieve numerical solution at current time-step)    
    U_sol[n + 1, 1:-1] = # fill in here!!!! (store numerical solution at interior nodes for the next time-step)    
    U_sol_analytical[n + 1, :] = # fill in here!!!! (store analytical solution for the next time-step)    
    # apply boundary-condition depending the sign of a_0    
    if #### fill in the correct condition here!!!! ####:        
        U_sol[n + 1, 0] = np.interp(x_start - a_0*dt, x, u)    
    else:        
        U_sol[n + 1, -1] = np.interp(x_end - a_0*dt, x, u)
        
        
        
