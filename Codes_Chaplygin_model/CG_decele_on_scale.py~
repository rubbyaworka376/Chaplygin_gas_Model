########## Chaplygin gas
import numpy as np
import matplotlib.pyplot as plt

A=1/3.
B=3.
a = np.linspace(0,10,100)
den2 = B/(a**6) + A
q = 1/2. - (3*A)/(2.*den2 )
#print qS

plt.plot(a, q) 
plt.legend()    
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r'deceleration parameter ($q$)')
#plt.grid()
#plt.title('deceleration parameter as function of scale factor')
axes = plt.gca()
axes.set_ylim([-1.3,1])
plt.show()    
