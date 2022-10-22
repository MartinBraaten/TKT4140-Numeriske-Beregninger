'''
Created on 24. feb. 2019

@author: Martinskole
'''
import numpy as np
import scipy
import scipy.sparse
import scipy.sparse.linalg
import matplotlib.pylab as plt

h=0.25
h2=0.1
h3=0.01
b=4  #beta^2
x=0

def asd():
    
    N = int(1/h-1)

    ilist=np.linspace(0, N+1, N+2)

    Maindiag= -(ilist[1:-1]*2+b*h)
    Subdiag = ilist[2:-1]-1
    Supdiag = ilist[1:-2]+1

    d=np.zeros(N)
    d[-1]=-(N+1)

    A = scipy.sparse.diags([Subdiag, Maindiag, Supdiag], [-1, 0, 1], format='csc') 

    theta = scipy.sparse.linalg.spsolve(A, d) # sparse solver.
    #theta2 = np.linalg.solve(A, d) # numpy linalg solver

    theta_0 = theta[0]/(1+b*h/2+b**2*h**2/12)
    theta=np.append(theta_0,theta)
    theta=np.append(theta,1)
    
    print "h =", h
    print theta

for i in range(1):
    asd()
    h=h2
    asd()
    h=h3 
    asd()
    