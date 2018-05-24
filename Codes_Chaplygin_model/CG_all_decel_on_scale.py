import numpy as np
import matplotlib.pyplot as plt

n=0.05
A=1/3.
B=3.
C=2.
a = np.linspace(0,12,100)
Y = B/(1.+A) + C/(a**(3*(1.+n)*(1+A)))
qm = 1/2. + (3*A)/2. - (3*B)/(2.*Y )
Z = B/(a**(3*(1+n))) + A
qg = 1/2. - (3*A)/(2.*Z )
M = B/(a**6) + A
qc = 1/2. - (3*A)/(2.*M )
#print q


plt.plot(a, qc, label='CG')
plt.plot(a, qg, label='GCG')
plt.plot(a, qm, label='MCG')
plt.legend(loc="upper right")    
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r'deceleration parameter ($q$)')
#plt.grid()
#plt.title('deceleration parameter as function of scale factor')
axes = plt.gca()
axes.set_ylim([-1.2,1.2])
plt.show()    
