import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

#Función que define comportamiento dinámico del tanque
def tanque(h, t):
    F0 = 1 # m^3
    A = 10 # m^2
    beta = 1
    dhdt = F0/A - beta/A * np.sqrt(h)  #m/min
    return dhdt

#vector de tiempo
t = np.linspace(0, 40)

#Función para resolver sistema 
h0 = 0
h = odeint(tanque, h0, t)

#Se generan los gráficos correspondientes para el modelo
plt.plot(t, h)
plt.xlabel('tiempo, [min]')
plt.ylabel('altura, [m]')
plt.show()


