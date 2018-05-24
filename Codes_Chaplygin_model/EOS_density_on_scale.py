import numpy as np
import matplotlib.pyplot as plt


a= np.linspace(0.4,1.6,101)
rho_0 = 3.

rho1 = rho_0 *(a**(-3-3*0.))
rho2 = rho_0 *(a**(-3-3*(1/3.)))
rho3 = rho_0 *(a**(-3-3*(-1.)))
    
    
    
#plt.legend(loc="upper left") 
plt.plot(a,rho1, label=r'$\rho(a)_{m}$')
plt.plot(a,rho2, label=r'$\rho(a)_{\gamma}$ ') 
plt.plot(a,rho3, label=r'$\rho(a)_{\Lambda}$') 
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r' Density ($\rho$)')
#plt.grid()
#plt.title(r'Density as function of Scale factor, $\rho = \rho_0 a^{-3(1+w)}$')
axes = plt.gca()
axes.set_ylim([0,10])
plt.legend()
plt.show()       
