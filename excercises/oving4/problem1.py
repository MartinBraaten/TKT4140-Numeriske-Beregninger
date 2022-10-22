'''
Created on 8. mar. 2019

@author: Martinskole
'''
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pylab as plt
import scipy
import scipy.sparse
import scipy.sparse.linalg




def plotSurfaceNeumannDirichlet(Temp, Ttop, Tleft, l, N, nxTicks=4, nyTicks=4):
    """ Surface plot of the stationary temperature in quadratic beam cross-section.
       Note that the components of T has to be started in the
       lower left part of the grid with increasing indexes in the
       x-direction first.


        Args:
            Temp(array):  the unknown temperatures, i.e. [T_1 .... T_(NxN)]
            Ttop(float):  temperature at the top boundary
            Tleft(float): temperature at the left boundary
            l(float):     height/width of the sides
            N(int):       number of nodes with unknown temperature in x/y direction
            nxTicks(int): number of ticks on x-label (default=4)
            nyTicks(int): number of ticks on y-label (default=4)
    """
    
    x = np.linspace(0, l, N + 1)
    y = np.linspace(0, l, N + 1)
    
    X2, Y2 = np.meshgrid(x, y)
    
    T = np.zeros_like(X2)
    
    T[-1,:] = Ttop
    T[:,0] = Tleft
    k = 1
    for j in range(N):
        T[j,1:] = Temp[N*(k-1):N*k]
        k+=1

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X2, Y2, T, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_zlim(0, Ttop)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('T [$^o$C]')
    
    xticks=np.linspace(0.0, l, nxTicks+1)
    ax.set_xticks(xticks)
    
    yticks=np.linspace(0.0, l, nyTicks+1)
    ax.set_yticks(yticks)
    


Ttop = 100
Tleft = 50
l = 1
N = 9



Maindiag= -4*np.ones(N*N)
Subdiag = np.ones(N*N-N)
Supdiag = np.ones(N*N-1)
Sup_1 = np.ones(N*N-N)
Sub_1 = np.ones(N*N-1)

for i in range(N):
    Sup_1[i]= 2 
    
Supdiag[N-1::N] = 0
    
Sub_1[N-1::N] = 0
Sub_1[N-2::N] = 2

d = np.zeros(N*N)
d[0::N] = -50
d[-N:] += -100

A = scipy.sparse.diags([Sub_1, Subdiag, Maindiag, Supdiag, Sup_1], [-1, -N, 0, 1, N], format='csc') 

Temp = scipy.sparse.linalg.spsolve(A, d)


print A.toarray()



plotSurfaceNeumannDirichlet(Temp, Ttop, Tleft, l, N)
plt.show()