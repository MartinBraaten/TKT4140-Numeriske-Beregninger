'''
Created on 14. jan. 2019

@author: Martinskole
'''
import matplotlib.pyplot as plt
from math import sin, pi
import numpy as np




X2 = np.linspace(0,2*pi,10)
F = np.linspace(0,2*pi,100)

#Y = np.arange(0,2*pi,0,1)
#plt.plot(Y, np.sin(Y))

plt.plot(X2,np.sin(X2),color="blue")
plt.plot(F,np.sin(F),color="red")

plt.legend(['sin(x) with 10 points', 'sin(x) with 100 points'], loc='best', frameon=False)
#plt.plot(block=True)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, which='both')
plt.savefig('sin(x).png', bbox_inches='tight')

plt.show()





