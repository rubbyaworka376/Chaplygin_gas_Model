#################### general Chaplygin varying B
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def GCG(a, t, A, B, K):
    ter_1 = np.sqrt((A*a**(3*n+3.) + B)**(1./(1+n)) - 3*K*a)
    dadt = ter_1/np.sqrt(3.*a)
    return dadt

n = 0.05 ### the alpha
A = 1/3.
K = 0.
a0 = 1.
B = np.array([0.,0.6,1.8,2.5,5.0])
labels = ["B=0.0","B=0.6","B=1.8","B=2.5","B=5.0"]
t = np.linspace(0., 21, 201)
#t = np.linspace(21., 200, 2001)


for i in range(len(B)):
    sol1 = odeint(GCG, a0, t, args=(A, B[i], 0.))
    plt.plot(t,sol1,label=labels[i])
    
plt.legend(loc="upper left")    
plt.xlabel('time ($t$)')
plt.ylabel('scale factor ($a$)')
plt.grid()
plt.title(r'Varying $B$')
axes = plt.gca()

plt.show()    
    


