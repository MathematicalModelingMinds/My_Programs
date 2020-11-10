import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y,t):
    y1 = y[0]
    y2 = y[1]
    

    # Parameters and inputs
    U=1
    Vb=3*5*5
    A=3*5*2+3*5*2+5*5*2
    R=8.314
    Vin=1.2*A/3600
    Vout=Vin
    P = 101325
    T_out=280 
    RH_out=0.8

    #Coefficients to determine the saturation vapor pressure of water
    p1=5.2623e-09
    p2=-6.3323e-06
    p3=0.003072
    p4=-0.75032
    p5=92.195
    p6=-4556.2
    p7=91.59
   
    Psat = p1*pow(T_out,6) + p2*pow(T_out,5) + p3*pow(T_out,4) + p4*pow(T_out,3) + p5*pow(T_out,2) + p6*T_out + p7

    PH2O = RH_out*Psat              # [Pa] Vapor presure of water at considering temperature and pressure
    f_H2O_in = PH2O/P          # [moles of water vapor/moles of moist air] Molar fraction of water vapor in
    M_air = 28.9*0.001         # [kg/mol] Molar mass of dry air
    M_H2O = 18*0.001           # [kg/mol] Molar mass of water
    M_in = M_air*(1-f_H2O_in) + M_H2O*f_H2O_in      # [kg/mol] Molar mass of incoming moist air
    Rho_in = P*M_in/(R*T_out)   # [kg/m3] Density of inlet air

    xi=f_H2O_in*M_H2O/(1-f_H2O_in)/M_air
    Cp_dryair=1006
    h_dryair=Cp_dryair*T_out
    Cp_H2O=1840
    h_fg = 2260000
    h_H2O=Cp_H2O*T_out+h_fg
    h_air_in=h_dryair+xi*h_H2O

    xo=Vin*Rho_in*xi/(Vout*y1)

    h_air_out=Cp_dryair*y2+xo*(Cp_H2O*y2+h_fg)

    Cp_air=Cp_dryair+Cp_H2O*xo

    f_H2O_out = (xo/M_H2O)/(xo/M_H2O+(1-xo)/M_air)
    M_out = M_air*(1-f_H2O_out) + M_H2O*f_H2O_out

    Q_supply=1000
    Q_loss=U*A*(y2-T_out)
    Q=Q_supply-Q_loss

    dy1dt=(Vin*Rho_in-Vout*y1)/Vb
    dy2dt=(Vin*Rho_in*h_air_in-Vout*y1*h_air_out+Q)/(Vb*y1*(Cp_air-R/M_out))-y2/y1*dy1dt
    dydt=[dy1dt, dy2dt]
    return dydt

# Initial conditions
y0=[1.2,285]

# Time span
t=np.linspace(0,3600,36)

y=odeint(model,y0,t)


fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time (min)')
ax1.set_ylabel('Air temperature [C]', color=color)
ax1.plot(t/60,y[:,1]-273.15, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Air density', color=color)  # we already handled the x-label with ax1
ax2.plot(t/60,y[:,0], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  
plt.show()