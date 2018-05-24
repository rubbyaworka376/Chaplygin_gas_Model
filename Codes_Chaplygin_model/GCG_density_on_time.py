import numpy as np  
     
def GCG(a, t, A, B, n):
    dadt = np.sqrt((A*a**6 + B)**(1/n) )/np.sqrt(3.*a)
    return dadt   


    
A = 1./3
B=0.3
n=0.2
a0 = 0.1
t = np.linspace(0, 16, 101)


from scipy.integrate import odeint
sol2 = odeint(GCG, a0, t, args=(A, B, n))


import matplotlib.pyplot as plt

    
def d2(a):
    G = (B/(a**(3.*(1/1+n))) + A)**(1./1+n)
    return G




plt.plot(t, d2(sol2[:]) ) 

plt.xlabel(r'time ($t$)')
plt.ylabel(r'density ($\rho$)')
plt.legend()
#plt.legend(loc="upper right")
#plt.grid()
#plt.title('density as function of time')
axes = plt.gca()
axes.set_ylim([-2,6000]) 

plt.show()




