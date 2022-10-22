'''
Created on 4. feb. 2020

@author: Martinskole
'''


import numpy as np
import matplotlib.pylab as plt

#a
print "hello world"

#b
a = np.array([1,2,3])
b = np.array([4,5,6])
A = np.array([[1,1,2],[2,3,3],[4,4,5]])
B = np.array([[2,4,6],[8,10,12],[14,16,18]])

print a+b
print a*b
print A*B 
print np.transpose(A)
print np.invert(A)
print(np.linalg.solve(A,b))

#c

def fib(n):
    h=1
    for h in range(1,n+1,1):
        if n==1:
            print 1
        elif n==0:
            print 0
        else:
            print  
        print
    


fib(n = input("Tast inn hvor mange elementer av Finbonacci serien du vil ha:" ))




#d

x = np.linspace(0,2*np.pi,10)
x_1 = np.linspace(0,2*np.pi,100)
y = np.sin(x)
y_1 = np.sin(x_1)

plt.plot(x,y)
plt.plot(x_1,y_1)
plt.legend(["10 points", "100 points"], loc='best', frameon=False)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, which='both')
plt.savefig('sin(x).png', bbox_inches='tight')
plt.show()

#e




    
    
    
    