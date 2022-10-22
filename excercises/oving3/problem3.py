'''
Created on 24. feb. 2019

@author: Martinskole
'''
import numpy as np
import matplotlib.pylab as plt
import scipy
import scipy.sparse
import scipy.sparse.linalg

N = 8 # number of unknowns
x = np.linspace(0, 0.9, N + 2)
h = 0.9/(N + 1)

y_analytic = 0.5*(np.log(np.abs(x-1))-np.log(np.abs(x+1))) + 2

# y'' = -2*x*(y')^2

y_0, y_End = y_analytic[0], y_analytic[-1] # boundaries

Y0 = np.linspace(y_0, y_End, N + 2) # first value of Y2

itmax=10
def lin1():
    for i in range(itmax):
        Maindiag= -2*np.ones(N)
        Subdiag = np.ones(N-1)
        Supdiag = np.ones(N-1)
    
        x_unknown=np.linspace(0+h,0.9-h,N)
        d = -0.5*x_unknown*(Y0[2:]-Y0[0:-2])**2
        d[0]=d[0]-y_0
        d[-1]=d[-1]-y_End
    
    
    # A*y = d
        A = scipy.sparse.diags([Subdiag, Maindiag, Supdiag], [-1, 0, 1], format='csc') 
        Y2 = scipy.sparse.linalg.spsolve(A, d)
        Y_final = np.append(y_0,Y2)
        Y_final = np.append(Y_final,y_End)
        Y0=Y_final
        
        
        
        plt.figure()
        plt.plot(x, Y_final)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

for i in range(itmax):
    a= Y0[2:]-Y0[0:-2]
    x_unknown=np.linspace(0+h,0.9-h,N)
    
    Maindiag= -2*np.ones(N)
    Subdiag = 1-x_unknown[1:]*a[1:]
    Supdiag = 1+x_unknown[:-1]*a[:-1]

    d = 0.5*x_unknown*(Y0[2:]-Y0[0:-2])**2
    d[0]=d[0]-y_0*(1-x_unknown[0]*a[0])
    d[-1]=d[-1]-y_End*(1+x_unknown[-1]*a[-1])


# A*y = d
    A = scipy.sparse.diags([Subdiag, Maindiag, Supdiag], [-1, 0, 1], format='csc') 
    Y2 = scipy.sparse.linalg.spsolve(A, d)
    Y_final = np.append(y_0,Y2)
    Y_final = np.append(Y_final,y_End)
    Y0=Y_final
    
    
    
    plt.figure()
    plt.plot(x, Y_final)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()