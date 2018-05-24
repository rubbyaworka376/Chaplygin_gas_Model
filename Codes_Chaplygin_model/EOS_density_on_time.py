import numpy as np
import matplotlib.pyplot as plt


rho = 3.
t = np.linspace(0,14,100)



den1 = (4/3.)*(t**(-2))
den2 = (3/4.)*(t**(-2))
den3 = rho*(t**0.)

plt.plot(t,den1, label=r'$\rho(t)_{m}$')
plt.plot(t,den2, label=r'$\rho(t)_{\gamma}$')
plt.plot(t,den3, label=r'$\rho(t)_{\Lambda}$')
plt.legend(loc="upper right")    
plt.xlabel(r'time ($t$)')
plt.ylabel(r'density ($\rho$)')
#plt.grid()
#plt.title('density as function of time')
axes = plt.gca()
axes.set_ylim([-1,5])
plt.show()     
