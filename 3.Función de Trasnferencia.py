import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
from scipy import signal

#Función que define comportamiento dinámico del tanque
def tanque(h, t):
    A = 1 # m^2
    alpha = 0.5
    dhdt = F/A - alpha/A * np.sqrt(h)  #m/min
    return dhdt

#Función de linealización del tanque dinámico
def tanque_lin(h_lin, t):
    F_lin = F - Fs 
    dhlindt = k /tau*F_lin - h_lin/tau  #m/min
    return dhlindt


#Vector de tiempo 
t = np.linspace(0, 100)
F = 2

#Sistema no lineal
h0 = 4
h = odeint(tanque, h0, t)

#Sistema Linealizado
Fs = 1 # m^3
hs = 4
A = 1 # m^2
alpha = 0.5 
k = 2*np.sqrt(hs)/alpha
tau = 2*A*np.sqrt(hs)/alpha

h0_lin = 0
h_lin = odeint(tanque_lin, h0_lin, t)
h_lin = h_lin + 4

#Función de transferencia 
num = [k]
den = [tau, 1]
sistema = signal.TransferFunction(num, den)
t1, ytf = signal.step(sistema)
ytf = ytf + 4

#Se generan los gráficos correspondientes para el modelo
plt.plot(t, h, t, h_lin, t1, ytf)
plt.xlabel('tiempo, [min]')
plt.ylabel('altura, [m]')
plt.show()


