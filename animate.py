'''
Created on 23. mai 2020

@author: Martinskole
'''
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
def f(x):
#Assigning a value of 1.0 for values less than 0.1
    f = np.zeros_like(x)
    f[np.where((x>=2) &(x <= 3))] = 1.0
    return f
def upwind(u, a_0, dx, dt):
# implementation of the upwind scheme
# Args:
# u (array): solution at current time-step (length N)
# a_0 (float): wave speed
# dx (float): spatial discretization step
# dt (floa): temporal discretization step
# Returns:
# u (array): solution of the interior nodes (excluding BCs) at next time-step (length N - 2)

    ####################
    ####################
    # fill in here!!!! (implement upwind scheme)
    ####################
    ####################
    if a_0 <= 0:
        u[1:-1] = u[1:-1] - a_0*dt/dx*(u[2:] - u[1:-1])
    else:
        u[1:-1] = u[1:-1] - a_0*dt/dx*(u[1:-1] - u[:-2])
    return u[1:-1]
####################
# discretization
####################
N = 101 # number of nodes in spatial direction
x_start, x_end = 0, 5
x = np.linspace(x_start, x_end, N)
dx = float((x_end-x_start)/N)# fill in here!!!! (evaluate spatial discretization step)
a_0 = -1
c_abs = 0.8
c = np.sign(a_0)*c_abs
dt = 0.5*c/a_0*dx  # fill in here (calculate time-step)
T = 2
t = np.arange(0, T + dt, dt)
####################
# creation of matrices for storing solutions
####################
U_sol = np.zeros((len(t), N))
U_sol_analytical = np.zeros((len(t), N))
####################
# apply initial solution
####################
U_sol[0, :] = f(x) # fill in here!!!! (set the initial solution at t=0)
U_sol_analytical[0,:] = f(x)# fill in here!!!! (evaluate analytical solution at t=0)
####################
# solving loop
####################
for n in range(len(t) - 1):
    u = U_sol[n, :] # fill in here!!!! (retrieve numerical solution at current time-step)
    U_sol[n + 1, 1:-1] = upwind(u, a_0, dx, dt)# fill in here!!!! (store numerical solution at interior nodes for the next time-step)
    U_sol_analytical[n + 1, :] = f(x-a_0*t[n]) # fill in here!!!! (store analytical solution for the next time-step)
    # apply boundary-condition depending the sign of a_0
    if a_0 <= 0:#### fill in the correct condition here!!!! ####:
        U_sol[n + 1, 0] = np.interp(x_start - a_0*dt, x, u)
    else:
        U_sol[n + 1, -1] = np.interp(x_end - a_0*dt, x, u)

### Animation 
 
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(x_start,x_end), ylim=(np.min(U_sol), np.max(U_sol)*1.1))

lines=[]     # list for plot lines for solvers and analytical solutions
legends=[]   # list for legends for solvers and analytical solutions

line, = ax.plot([], [])
lines.append(line)
legends.append(upwind.__name__)

line, = ax.plot([], []) #add extra plot line for analytical solution
lines.append(line)
legends.append('Analytical')

plt.xlabel('x-coordinate [-]')
plt.ylabel('Amplitude [-]')
plt.legend(legends, loc=3, frameon=False)
 
# initialization function: plot the background of each frame
def init():
    for line in lines:
        line.set_data([], [])
    return lines,

# animation function.  This is called sequentially
def animate(i):
    for k, line in enumerate(lines):
        if (k==0):
            line.set_data(x, U_sol[i,:])
        else:
            line.set_data(x, U_sol_analytical[i,:])
    return lines,

def animate_alt(i):
    for k, line in enumerate(lines):
        if (k==len(lines)-1):
            line.set_data(x, U_sol_analytical[i,:])
        else:
            line.set_data(x, U_sol[i,:])
    return lines,

 
# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate_alt, init_func=init, frames=N, interval=100, blit=False)
plt.show()
