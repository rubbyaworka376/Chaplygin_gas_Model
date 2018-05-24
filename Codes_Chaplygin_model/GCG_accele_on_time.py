import numpy as np 
import matplotlib.pyplot as plt

def GCG(a, t, A, B, n):
    	dadt = np.sqrt((A*a**6 + B)**(1/n) )/np.sqrt(3.*a)
    	return dadt 
    
    
    
A=1/3.   
B = 0.215
n=0.21    
a0 =0.1

t = np.linspace(0, 29, 101)
from scipy.integrate import odeint
sol2 = odeint(GCG, a0, t, args=(A, B, n))
def f2(a):
	den = A + B/(a**(3+3.*n)) 
    	G = den**(1./(1+n))
    	U = A/(G**n)
    	return - a/6 * (G - 3*U)
    
    
plt.figure()
plt.plot(t, f2(sol2[:]) )
plt.xlabel(r'time ($t$)')
plt.ylabel(r' acceleration ($\ddot{a}$)')
#plt.legend(loc="upper left")
plt.legend()
#plt.grid()
#plt.title('acceleration as function of time')
axes = plt.gca()
plt.show()    
