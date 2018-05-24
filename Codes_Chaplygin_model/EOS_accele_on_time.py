import numpy as np
import matplotlib.pyplot as plt

rh0 = 1.
t = np.linspace(0,5,100)

a1= ( -rh0/6.)*(((3/4.)*rh0)**(-2/3.))
accele1 = a1*(t**(-4/3.))

a2 = (-rh0/3.)*((rh0*4/3.)**(-3/4))
accele2 = a2*(t**(-3/2.))

accele3 = rh0/3.*(np.exp(np.sqrt(rh0/3.)*t))

plt.plot(t,accele1, label=r'$\ddot{a}(t)_m$')
plt.plot(t,accele2, label=r'$\ddot{a}(t)_{\gamma}$')
plt.plot(t,accele3, label=r'$\ddot{a}(t)_{\Lambda}$')
plt.legend(loc="upper left")    
plt.xlabel(r'time ($t$)')
plt.ylabel(r'acceleration ($\ddot{a}$)')
#plt.grid()
#plt.title('acceleration as function of time')
axes = plt.gca()
axes.set_ylim([-6,7])
plt.show() 


