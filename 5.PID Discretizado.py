import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

#Condición inicial 
y0 = 0

def tanque(h, t):   
    A = 10 # m^2
    beta = 2
    dhdt = F0/A - beta/A * np.sqrt(h)  #m/min
    return dhdt

#vector de tiempo
t = np.linspace(0, 100, 101)
F0 = 1 # m^3

#condiciones de entrada 
y = odeint(tanque, y0, t)

ns = len(t)

#Variables de acumulación de error, set point y constantes del PID
ysp = 0.25
epp_0 = 0
ep_0 = 0
ep = 0
kc = 2
tauI = 1 
tauD = 0
F0_ctrl = 0

yd0 = y0
ydf = []
F0_ctrl_t = []
ydf.append(float(y0))

#Ciclo para discretizar entre cero y un tiempo menor al inicial 
for i in range (0, ns-1):
    #if i > 25:       #Modificación de la perturbacuión en el tiempo
    #    F0 = 1 + 0.5
    ts = [t[i], t[i+1]]
    F0 = F0_ctrl
    yd = odeint(tanque, yd0, ts)
    yd0 = yd[-1]
    ydf.append(float(yd0))
 
    #PID 
    delta_t = t[i+1]-t[i]
    epp_0 = ep_0
    ep_0 = ep 
    ep = ysp - yd0
    #Ecuación del PID discretizado por Ecuación de velocidad
    delta_u = kc*((ep-ep_0) + ep/float(tauI)*delta_t + tauD /float(delta_t)*(ep-2*ep_0+epp_0))
    F0_ctrl = F0_ctrl + delta_u
    F0_ctrl_t.append(float(F0_ctrl))

#Se generan los gráficos correspondientes para el modelo
plt.plot(t, y, t, ydf)
plt.xlabel('tiempo, [min]')
plt.ylabel('altura, [m]')
plt.show()


