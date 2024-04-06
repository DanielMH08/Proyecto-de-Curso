import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
from scipy.optimize import fsolve

#Valores de condición inicial 
y0 = 0
A = 10 # m^2
beta = 2

#Función que describe el tanque dinámico
def tanque(h, t):
    A = 10 # m^2
    beta = 2
    dhdt = F0/A - beta/A * np.sqrt(h)  #m/min
    return dhdt

#vector de tiempo
t = np.linspace(0, 100, 150)
F0 = 1 # m^3

#Sistema Linealizado
ns = len(t)
ysp = 0.5
hs = ysp
kp = 2*np.sqrt(hs)/beta 
taup = 2*A*np.sqrt(hs)/beta
td = 1

#Variables de acumulación de error y constantes del PID
kcu = 20
Pu = 2
epp_0 = 0
ep_0 = 0
ep = 0

#Modelos de controladores, comentar y descomentar para ejecutar 

### Ziegler - Nichols PI
kc = 0.45*kcu 
tauI = Pu/1.2
tauD = 0

### Ziegler - Nichols PID
# kc = 0.6*kcu  
# tauI = Pu*2      
# tauD = Pu/8  

### Tyreus - Luyben PI
# kc = 0.31*kcu
# tauI = Pu*2.2
# tauD = 0

### Tyreus - Luyben PID
# kc = 0.45*kcu
# tauI = Pu*2.2
# tauD = Pu/6.3


F0_ctrl = 0
yd0 = y0
ydf = []
F0_ctrl_t = []
ydf.append(float(y0))

#Ciclo para discretizar entre cero y un tiempo menor al inicial 
for i in range (0, ns-1):
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
    
t_sp = [0, t[-1]]
y_sp = [ysp, ysp]

#Se generan los gráficos correspondientes para el modelo
plt.plot(t_sp, y_sp, t, ydf)
plt.xlabel('tiempo, [min]')
plt.ylabel('altura, [m]')
plt.show()

 

