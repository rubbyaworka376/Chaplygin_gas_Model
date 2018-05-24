import numpy as np  

def MCG(a, t, A, B, C, n):
    dadt = np.sqrt(a**2/3.*(B/(1+A)+C/a**(3*(1+A)*(1+n)))**(1/1+n) )/np.sqrt(3.*a)
    return dadt
    
A = 1./3
B=1/3
n=0.2
C = 3
a0 = 0.1

t = np.linspace(0, 16, 101)


from scipy.integrate import odeint
sol3 = odeint(MCG, a0, t, args=(A, B, C, n))

import matplotlib.pyplot as plt

def d3(a):
	den = (B/(1.+A) + C/a**(3.*(1+A)*(1.+n)))**(1/1+n)
	return den
	   


plt.plot(t, d3(sol3[:]) )
plt.xlabel(r'time ($t$)')
plt.ylabel(r'density ($\rho$)')
plt.legend()
#plt.legend(loc="upper right")
#plt.grid()
#plt.title('density as function of time')
axes = plt.gca()
axes.set_ylim([-2,20])
plt.show()




