import numpy as np
import matplotlib.pyplot as plt

rh0 = 1.
t = np.linspace(0,10,100)



s1 = (3/4.*rh0)**(1/3)
scalefac1 = s1*(t**(2/3.))

s2 = (4/3.*rh0)**(1/4.)
scalefac2 = s2*(t**(1/2.))

scalefac3 = np.exp(np.sqrt(rh0/3.)*t)

plt.plot(t,scalefac1, label=r'$a(t)_{m}$')
plt.plot(t,scalefac2, label=r'$a(t)_{\gamma}$')
plt.plot(t,scalefac3, label=r'$a(t)_{\Lambda}$')
plt.legend(loc="upper right")    
plt.xlabel(r'time ($t$)')
plt.ylabel(r'scale factor ($a$)')
#plt.grid()
#plt.title('Scale factor as function of time')
axes = plt.gca()
axes.set_ylim([0,20])
plt.show()    
