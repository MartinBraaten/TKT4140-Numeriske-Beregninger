'''
Created on 25. feb. 2019

@author: Martinskole
'''

import numpy as np
import matplotlib; matplotlib.use('Qt4Agg')
import matplotlib.pylab as plt
plt.get_current_fig_manager().window.raise_()

# y''=-2x(y')^2

S_0 = -0.5    # S = y'(0)
S_1 = -0.6
# y_0 = 2
y_0_9 = 0.5*(np.log(0.1)-np.log(1.9))+2


N = 90
x = np.linspace(0, 0.9, N + 1)

y_analytic = 0.5*(np.log(np.abs(x-1))-np.log(np.abs(x+1))) + 2

z0 = [2,S_0]


def rk4(func, z0, time):
    """The Runge-Kutta 4 scheme for solution of systems of ODEs.
    z0 is a vector for the initial conditions,
    the right hand side of the system is represented by func which returns
    a vector with the same size as z0 ."""

    z = np.zeros((np.size(time),np.size(z0)))
    z[0,:] = z0
    zp = np.zeros_like(z0)

    for i, t in enumerate(time[0:-1]):
        dt = time[i+1] - time[i]
        dt2 = dt/2.0
        k1 = np.asarray(func(z[i,:], t))                # predictor step 1
        k2 = np.asarray(func(z[i,:] + k1*dt2, t + dt2)) # predictor step 2
        k3 = np.asarray(func(z[i,:] + k2*dt2, t + dt2)) # predictor step 3
        k4 = np.asarray(func(z[i,:] + k3*dt, t + dt))   # predictor step 4
        z[i+1,:] = z[i,:] + dt/6.0*(k1 + 2.0*k2 + 2.0*k3 + k4) # Corrector step
    return z

def func(Y2,x):
    y_0 = Y2[0]
    y_1 = Y2[1]              # y'
    f_0 = y_1               # f_0 = y'
    f_1 = -2*x*y_1**2       # f_1 = y''
    
    return [f_0, f_1]

y = rk4(func, z0, x)
Y2 = y[:,0]

phi_0 = Y2[-1]-y_0_9
plt.figure()
for i in range(10):
    z0 = [2,S_1]
    y = rk4(func, z0, x)
    Y2 = y[:,0]
    phi_1 = Y2[-1]-y_0_9
    D_S = -phi_1*(S_1-S_0)/(phi_1-phi_0)
    S_0 = S_1
    S_1 = S_0+D_S
    phi_0 = phi_1
    plt.plot(x,Y2)



plt.xlabel("x")
plt.ylabel("y")
plt.show()



s_start, s_end = -0.5, -1.23
sList = np.linspace(s_start, s_end, 51)
phiList = np.zeros_like(sList)

for n, s in enumerate(sList):
    Y_0 = [2,s]
    Y_shoot = rk4(func, Y_0, x)
    y_shoot = Y_shoot[:,0]   # extract y, and not y'
    phiList[n] = y_shoot[-1]-y_0_9



plt.figure()
plt.plot(sList, phiList)
plt.plot(sList, np.zeros_like(sList), 'k--')
plt.xlim([s_start, s_end])
plt.ylim([np.min(phiList), np.max(phiList)])
plt.xlabel('s')
plt.ylabel(r'$\phi$')
plt.show()

