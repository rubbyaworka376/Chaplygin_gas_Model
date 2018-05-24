import numpy as np
import matplotlib.pyplot as plt


A = 1/3.
B = 3.
C = 2
n = 0.05
a = np.linspace(0.3,20,101) 


rho3m = (B/(1.+A) + C/(a**((3.+3.*A)*(1.+n))))**(1./(1+n))


 
 
#plt.legend(loc="upper left")
plt.legend()
plt.plot(a,rho3m)  
plt.xlabel('scale factor ($a$)')
plt.ylabel(r' density ($\rho$)')
#plt.grid()
#plt.title('enegy density as function of scale factor')
axes = plt.gca()
axes.set_ylim([0.1,10.])
plt.axis([0,20,2,8])
plt.legend()
plt.show()   
