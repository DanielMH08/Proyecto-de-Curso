import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

#Condición inicial 
y0 = 0

#Función que define comportamiento dinámico del tanque
def tanque(h, t):
    A = 10 # m^2
    beta = 2
    dhdt = F0/A - beta/A * np.sqrt(h)  #m/min
    return dhdt

#vector de tiempo
t = np.linspace(0, 40)
F0 = 1 # m^3

#condiciones de entrada 
y = odeint(tanque, y0, t)
ns = len(t)
yd0 = y0
ydf = []
ydf.append(float(y0))

#Ciclo para discretizar entre cero y un tiempo menor al inicial  
for i in range (0, ns-1):
    if i > 25:            #Modificación de la perturbacuión en el tiempo
        F0 = 1 + 0.5
    ts = [t[i], t[i+1]]
    yd = odeint(tanque, yd0, ts)
    yd0 = yd[-1]
    ydf.append(float(yd0))

#Se generan los gráficos correspondientes para el modelo
plt.plot(t, y, t, ydf)
plt.xlabel('tiempo, [min]')
plt.ylabel('altura, [m]')
plt.show()


