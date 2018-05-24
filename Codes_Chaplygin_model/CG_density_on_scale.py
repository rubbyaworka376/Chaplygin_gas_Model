import numpy as np
import matplotlib.pyplot as plt

########### Chaplygin gas
A = 1/3.
B = 3.
a = np.linspace(0.3,20,101) 

#rho = np.sqrt(A+(B/(a**6.)))

rho1 =np.sqrt((B/(a**6.))+A)



 
 
#plt.legend(loc="upper left")
plt.plot(a,rho1 )    
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r'enegy density ($\rho$)')
#plt.grid()
#plt.title('enegy density as function of scale factor')
axes = plt.gca()
#axes.set_ylim([0.,10.])
plt.legend()
plt.show()   
