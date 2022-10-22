'''
Created on 14. jan. 2019

@author: Martinskole
'''
from math import pi,sqrt
b=0.1
h=0.2
r=0.15
L=1.0
P=1*1e6
E_steel=200*1e9
E_alu=69*1e9
dx=0.1

I_rectangular = b*h**3/12.
I_circular = pi*r**4/4.0
y_tip_steel_rectangular = -L**3*P/(3*E_steel*I_rectangular)*1e3
y_tip_steel_circular = -L**3*P/(3*E_steel*I_circular)*1e3
print "tip deflection for steel with rectangular cross-section: ", y_tip_steel_rectangular
print "tip deflection for steel with rectangular cross-section: ", y_tip_steel_circular
print "area rectangular: ", b*h, "area circular: ", pi*r**2
print "r: ", sqrt(b*h/pi)
N=int(L/dx)+1
X2=[]
for n in range(N):
    X2=n*dx
    X2.append(x)
print X2
