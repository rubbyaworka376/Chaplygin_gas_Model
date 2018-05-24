import numpy as np
import matplotlib.pyplot as plt

rh0 = 1.

a = np.linspace(0.04,1.9,100)


acc1 = -(1./6)*(rh0*(a**(-2.)))
acc2 = -(1./3)*(rh0*(a**(-3.)))
acc3 = (rh0/3.)*a 

plt.plot(a,acc1, label=r'$\ddot{a}(a)_{m}$')
plt.plot(a,acc2, label=r'$\ddot{a}(a)_{\gamma}$')
plt.plot(a,acc3, label=r'$\ddot{a}(a)_{\Lambda}$')
plt.legend(loc="lower right")    
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r'acceleration ($\ddot{a}$)')
#plt.grid()
#plt.title('acceleration as function of scale factor')
axes = plt.gca()
axes.set_ylim([-3,2])
plt.show() 
