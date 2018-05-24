import numpy as np
import matplotlib.pyplot as plt

n=0.05
A=1/3.
B=3.
C=2.
a = np.linspace(0,10,100)
Y = B/(1.+A) + C/(a**(3*(1.+n)*(1+A)))
q = 1/2. + (3*A)/2. - (3*B)/(2.*Y )


plt.plot(a, q)
plt.legend()    
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r'deceleration parameter ($q$)')
#plt.grid()
#plt.title('deceleration parameter as function of scale factor')
axes = plt.gca()
axes.set_ylim([-1.2,1.2])
plt.show()    
