import numpy as np  
def MCG(a, t, A, B, C, n):
    dadt = np.sqrt(a**2/3.*(B/(1+A)+C/a**(3*(1+A)*(1+n)))**(1/1+n) )/np.sqrt(3.*a)
    return dadt
    
A =0.2      
B = 0.03      
n=0.5
C = 3
a0 =0.1

t = np.linspace(0, 29, 101)

from scipy.integrate import odeint

sol3 = odeint(MCG, a0, t, args=(A, B, C, n))

import matplotlib.pyplot as plt



def f3(a):
	D = (B/(1.+A) + C/(a**(3.*(1+A)*(1.+n))))**(1/1+n)
	return -a/6*(D +3*A*C -3*A/(D**n)) 
	   

plt.figure()
plt.plot(t, f3(sol3[:]) )
plt.xlabel(r'time ($t$)')
plt.ylabel(r' acceleration ($\ddot{a}$)')
#plt.legend(loc="upper left")
plt.legend()
#plt.grid()
#plt.title('acceleration as function of time')
axes = plt.gca()
axes.set_ylim([-3,5])   
plt.show()
