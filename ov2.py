'''
Created on 4. feb. 2020

@author: Martinskole
'''
import scipy
import numpy as np
import matplotlib.pylab as plt

x = np.linspace(0,1.5,1001)

y_n = x-x**2+x**3/3-x**4/6+x**5/30-x**6/45
y_a = 3*np.sqrt(2*np.pi*np.exp)*np.exp(x*(1+x/2))*(scipy.special.erf(np.sqrt(2)/2*(1+x))-scipy.special.erf(np.sqrt(2)/2))+4*(1-np.exp(x*(1+x/2)))-x



plt.plot(x,y_n)
plt.plot(x,y_a)
plt.show()
