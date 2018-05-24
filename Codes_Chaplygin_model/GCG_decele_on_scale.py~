############ Generalized Chaplygin gas

import numpy as np
import matplotlib.pyplot as plt

n=0.05
A=1/3.
B=3.
a = np.linspace(0,20,100)
Y = B/(a**(3*(1+n))) + A
q = 1/2. - (3*A)/(2.*Y )
#print q

plt.plot(a, q)
plt.legend(loc="upper right")    
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r'deceleration parameter ($q$)')
#plt.grid()
#plt.title('deceleration parameter as function of scale factor')
axes = plt.gca()
axes.set_ylim([-1.3,1])
plt.show()    
