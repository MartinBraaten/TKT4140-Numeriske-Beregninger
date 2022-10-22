'''
Created on 23. mai 2020

@author: Martinskole
'''
import numpy as np
def upwind(u):    
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
    a_0 = 1
    if a_0 <=0:
        u[1:-1] = u[1,-1] - (u[:-2] - u[1:-1])
    else: 
        u[1:-1] = u[1,-1] - (u[1:-1] - u[2:])    
        
    return u


u = np.array([1,2,3])

print(u[2:])
upwind(u)
