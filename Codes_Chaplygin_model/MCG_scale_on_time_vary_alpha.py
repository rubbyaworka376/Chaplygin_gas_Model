################# modified chaplygin gas by varying $\alpha$

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def MCG(a, t, A, B, n):
    ter_1 = np.sqrt(1/(3*a**(3*A+1)))
    ter_2 = np.sqrt(((B*a**((1+A)*(1+n)) + C*(1+A))/(1+A))**(1/float(1+n)) -3*K*a**(3*A+1)  )
    dadt = ter_2*ter_1
    return dadt
B = 2
A = 1/3.
K = 0.
a0 = 1.
C= 3
n = np.array([0.00, 0.02, 0.5, 0.8, 1.0])
labels = [r"$\alpha=0.0002$",r"$\alpha=0.05$",r"$\alpha=0.5$",r"$\alpha=0.9$",r"$\alpha=1.0$"]
t = np.linspace(0., 21.0, 101)


for i in range(len(n)):
    sol1 = odeint(MCG, a0, t, args=(A, B, n[i]))
    plt.plot(t,sol1,label=labels[i])
    
plt.legend(loc="upper left")    
plt.xlabel('time ($t$)')
plt.ylabel('scale factor ($a$)')
plt.grid()
plt.title(r'Varying $\alpha$')
#plt.title(r'Scale factor as function of time. $p=A\rho -B/\rho^{\alpha}$')
axes = plt.gca()

plt.show()    


