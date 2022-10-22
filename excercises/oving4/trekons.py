'''
Created on 28. sep. 2019

@author: Martinskole
'''
from math import sqrt, sinh, cosh, tanh
import matplotlib.pylab as plt

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

#G_values=[G_1, G_2, G_3]
#Tau_values = [tau_1, tau_2, tau_3]

A_1 = b*t_1
A_2 = b*t_2
alpha = E_1*A_1/(E_2*A_2) # alpha=1

#r = G_values[i]/d_g
r_1 = G_1/d_g
r_2 = G_2/d_g
r_3 = G_3/d_g

#w = sqrt(b*r*l**2*(1+alpha)/(E_1*A_1))
w_1 = sqrt(b*r_1*l**2*(1+alpha)/(E_1*A_1))
w_2 = sqrt(b*r_2*l**2*(1+alpha)/(E_1*A_1))
w_3 = sqrt(b*r_3*l**2*(1+alpha)/(E_1*A_1))

#F_max = (Tau_values[i])*w/(r*l)*(1/(E_1*A_1*sinh(w))+1/E_2*A_2*tanh(w))**-1
F_max_1 = tau_1*w_1/(r_1*l*10**6)*(1/(E_1*A_1*sinh(w_1))+1/E_2*A_2*tanh(w_1))**-1 #divide by 10^6 for MPa
F_max_2 = tau_2*w_2/(r_2*l*10**6)*(1/(E_1*A_1*sinh(w_2))+1/E_2*A_2*tanh(w_2))**-1
F_max_3 = tau_3*w_3/(r_3*l*10**6)*(1/(E_1*A_1*sinh(w_3))+1/E_2*A_2*tanh(w_3))**-1

tau_m_1 = F_max_1/(b*l)
tau_m_2 = F_max_2/(b*l)
tau_m_3 = F_max_3/(b*l)
    
L = 250.
dx = 0.1
N = int(L/dx) + 1

X2 = []
Y2 = []
A = []
B = []
C = []
D = []

for n in range(N):
    x = n*dx
    # tau = tau_m*w/((1+alpha)*sinh(w)) * (alpha*cosh(w*x/l)+cosh(w*(1-x/l)))
    tau_1 = tau_m_1*w_1/((1+alpha)*sinh(w_1))*(alpha*cosh(w_1*x/l)+cosh(w_1*(1-x/l)))
    tau_2 = tau_m_2*w_2/((1+alpha)*sinh(w_2))*(alpha*cosh(w_2*x/l)+cosh(w_2*(1-x/l)))
    tau_3 = tau_m_3*w_3/((1+alpha)*sinh(w_3))*(alpha*cosh(w_3*x/l)+cosh(w_3*(1-x/l)))
    
    y_1 = tau_1
    X2.append(x)
    Y2.append(y_1)
    
    y_2 = tau_2
    A.append(x)
    B.append(y_2)
    
    y_3 = tau_3
    C.append(x)
    D.append(y_3)

plt.plot(X2,Y2,'b')
plt.xlabel("x [mm] ")
plt.ylabel(r'$\tau$(x) [MPa]')
plt.legend([r'$\tau$=2 MPa, G=300 MPa'], loc='best', frameon=False)
plt.show()

plt.plot(A,B,'r')
plt.xlabel("x [mm] ")
plt.ylabel(r'$\tau$(x) [MPa]')
plt.legend([r'$\tau$=3 MPa, G=500 MPa'], loc='best', frameon=False)
plt.show()

plt.plot(C,D,'g')
plt.xlabel("x [mm] ")
plt.ylabel(r'$\tau$(x) [MPa]')
plt.legend([r'$\tau$=4 MPa, G=1000 MPa'], loc='best', frameon=False)
plt.show()

