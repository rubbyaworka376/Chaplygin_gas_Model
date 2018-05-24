import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

########## chaplygin gas
def CG(a, t, A, B, K):
    dadt = np.sqrt(np.sqrt(A*a**6 + B) - 3*K*a)/np.sqrt(3.*a)
    return dadt

A = 1/3.
K = 0.
a0 = 1.
B = np.array([0.,0.6,1.8,2.5,5.0])
labels = ["B=0.0","B=0.6","B=1.8","B=2.5","B=5.0"]
t = np.linspace(0., 21., 101) 

#plt.figure()
for i in range(len(B)):
    sol1 = odeint(CG, a0, t, args=(A, B[i], 0.))
    plt.plot(t,sol1[:],label=labels[i])
    
plt.legend(loc="upper left")    
plt.xlabel('time ($t$)')
plt.ylabel('scale factor ($a$)')
plt.grid()
plt.title(r'Varying $B$')
#plt.title(r'Scale factor as function of time')
axes = plt.gca()
#axes.set_ylim([-3,8000])
plt.show()    
    


