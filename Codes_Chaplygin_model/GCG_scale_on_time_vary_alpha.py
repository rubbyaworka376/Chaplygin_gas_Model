################# general varying alpha

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def GCG(a, t, A, B, n):
    dadt = (np.sqrt((A*a**(3*n+3.) + B)**(1./(1+n)) - 3.*K*a))/(np.sqrt(3.*a))
    return dadt

B = 3
A = 1/3.
K = 0.
a0 = 1.
n = np.array([0.0002, 0.05, 0.5, 0.9, 1.0])
labels = [r"$\alpha=0.0002$",r"$\alpha=0.05$",r"$\alpha=0.5$",r"$\alpha=0.9$",r"$\alpha=1.0$"]
t = np.linspace(0., 13.0, 101)
#t = np.linspace(0., 21.0, 1001)

for i in range(len(n)):
    sol1 = odeint(GCG, a0, t, args=(A, B, n[i]))
    plt.plot(t,sol1,label=labels[i])
    
plt.legend(loc="upper left")    
plt.xlabel('time ($t$)')
plt.ylabel('scale factor ($a$)')
#plt.grid()
plt.title(r'Varying $\alpha$')
axes = plt.gca()

plt.show()    


