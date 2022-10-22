'''
Created on 23. sep. 2019

@author: Martinskole
'''
from math import sqrt, sinh, cosh, tanh
import matplotlib.pylab as plt
import numpy as np



b = 100
t_1 = 50
t_2 = 50
d_g = 1
l = 250
E_1 = 10000
E_2 = 10000
Glue_line = b*d_g
G_1 = 300
G_2 = 500
G_3 = 1000
tau_1 = 2
tau_2 = 3
tau_3 = 4


G_values=[G_1, G_2, G_3]
Tau_values = [tau_1, tau_2, tau_3]
tau=[]

A_1 = b*t_1
A_2 = b*t_2
alpha = E_1*A_1/(E_2*A_2) # alpha=1

L = 250.
dx = 0.1
N = int(L/dx) + 1
for n in range(N):
        x = n*dx

#tau = tau_m*w/((1+alpha)*sinh(w))*(alpha*cosh(w*x/l)+cosh(w*(1-x/l)))
def var():
    for i in range(len(G_values)):
        r = G_values[i]/d_g
        w = sqrt(b*r*l**2*(1+alpha)/(E_1*A_1))
        F_max = (Tau_values[i])*w/(r*l)*(1/(E_1*A_1*sinh(w))+1/E_2*A_2*tanh(w))**-1


        tau_m = F_max/(b*l)
        
        tau.append(i) = tau_m*w/((1+alpha)*sinh(w)) * (alpha*cosh(w*x/l)+cosh(w*(1-x/l)))
        print(tau[i])
        return tau[i]
var()
def tre():
    L = 250.
    dx = 0.1
    N = int(L/dx) + 1

    X2 = []
    Y2 = []
    plt.figure()

    for n in range(N):
        x = n*dx
        
    
        for i in range(len(G_values)):
            r = G_values[i]/d_g
            w = sqrt(b*r*l**2*(1+alpha)/(E_1*A_1))
            F_max = (Tau_values[i])*w/(r*l)*(1/(E_1*A_1*sinh(w))+1/E_2*A_2*tanh(w))**-1


            tau_m = F_max/(b*l)
    
            tau = tau_m*w/((1+alpha)*sinh(w)) * (alpha*cosh(w*x/l)+cosh(w*(1-x/l)))
            print (tau, "dette er tau")
            
            y = tau
            X2.append(x)
            Y2.append(y)

    
            plt.plot(X2,Y2,'b--')
    plt.ylim(0,2*10**4)
    #plt.legend(["", ""])
    plt.xlabel("x")
    plt.ylabel("y")
    
    
    plt.show()

