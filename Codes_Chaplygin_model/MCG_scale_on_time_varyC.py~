############################ modified
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def MCG(a, t, A, B, C):
    ter_1 = np.sqrt(1/(3*a**(3*A+1)))
    ter_2 = np.sqrt(((B*a**((1+A)*(1+n)) + C*(1+A))/(1+A))**(1/float(1+n)) -3*K*a**(3*A+1)  )
    dadt = ter_2*ter_1
    return dadt


n = 0.05 ### the alpha
A = 1/3.
K = 0.
a0 = 1.
B= 2.
C = np.array([0.00001,0.6,1.8,2.5,5.0])
labels = ["C=0.00001","C=0.6","C=1.8","C=2.5","C=5.0"]
t = np.linspace(0., 21, 101)


for i in range(len(C)):
    sol1 = odeint(MCG, a0, t, args=(A, B, C[i]))
    plt.plot(t,sol1,label=labels[i])
    
plt.legend(loc="upper left")    
plt.xlabel('time ($t$)')
plt.ylabel('scale factor ($a$)')
plt.grid()
plt.title(r'Varying $C$')
#plt.title(r'Scale factor as function of time, $p = A\rho-B/\rho^{\alpha}$')
axes = plt.gca()

plt.show()    
    





