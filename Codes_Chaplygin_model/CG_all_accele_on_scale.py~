import numpy as np
import matplotlib.pyplot as plt
a = np.linspace(0.04,20,101)
A = 1/3.
B = 2.
C = 3.
n = 0.05

chap1 = -a/6.*(np.sqrt(A+(B/a**6.)) -3.*A/(np.sqrt(A+(B/a**6.))) )

gen1 = (A + B/(a**(3.*n + 3.)) )**(1./(1.+n))  + (-3.*A)/((A + B/(a**(3.*n + 3.)) )**(1./(1.+n)))

chap2 = -a/6.*(gen1)

mod1 = (B/(1. + A) + C/(a**((3.+ 3.*n)*(1+A) )) )**(1./(1.+n))  + 3.*A*((B/(1. + A) + C/(a**((3.+ 3.*n)*(1+A) )) )**(1./(1.+n)))  
mod2 = -3.*B/((B/(1. + A) + C/(a**((3.+ 3.*n)*(1+A) )) )**(n/(1.+n))) 
chap3 = -a/6.*(mod1 + mod2)

plt.plot(a,chap1, label='CG')
plt.plot(a,chap2, label='GCG')
plt.plot(a,chap3, label='MCG')
plt.legend(loc="lower right")    
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r'acceleration ($\ddot{a}$)')
#plt.grid()
#plt.title('acceleration as function of scale factor')
axes = plt.gca()
axes.set_ylim([-10.,11])
plt.show()    
    
