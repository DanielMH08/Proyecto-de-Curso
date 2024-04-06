import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

#Función que define comportamiento dinámico del tanque
def tanque(h, t):
    A = 1 # m^2
    alpha = 0.5
    dhdt = F/A - alpha/A * np.sqrt(h)  #m/min
    return dhdt

#Función de linealización del tanque dinámico
def tanque_lin(h_lin, t):
    Fs = 1 # m^3
    hs = 4
    A = 1 # m^2
    alpha = 0.5
    F_lin = F - Fs
    k = 2*np.sqrt(hs)/alpha
    tau = 2*A*np.sqrt(hs)/alpha
    
    ##Fórmula de linealización
    dhlindt = k /tau*F_lin - h_lin/tau #m/min
    return dhlindt

F = 2

#Sistema no lineal 
t = np.linspace(0, 50)
h0 = 4
h = odeint(tanque, h0, t)

#sistema linealizado
h0_lin = 0
h_lin = odeint(tanque_lin, h0_lin, t)
#h_lin = h_lin + 4

#Se generan los gráficos correspondientes para el modelo
plt.plot(t, h, t, h_lin)
plt.xlabel('tiempo, [min]')
plt.ylabel('altura, [m]')
plt.show()


