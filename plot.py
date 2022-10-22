'''
Created on 22. jan. 2019

@author: Martinskole
'''

from __builtin__ import int
D= 0.5
f=0.05
L=392
g=9.8
dt=1

z_0 = -6
v_0 = 0
T=3.

z_n= z_0
v_n=v_0
N=int(T/dt)


z=np.zeroes(N+1)
v=np.zeroes(N+1)
t=np.zeroes(N+1)

for n in range(N):
    z[n+1]= z[n]+dt*v[n]
    v[n+1]=v[n]+dt*(-(2*g*z_n/L + f*v_n*v_n/(2*D)))
    
    t[n+1]= t[n] +dt
    
    print"z({0}) = {1}".format(t[n+1],z[n+1])
    print"v({0}) = {1}".format(t[n+1],v[n+1])
    
    
plt.figure()
plt.plot(t,z)
plt.xlabel("t")
plt.ylabel("z")
plt.show()