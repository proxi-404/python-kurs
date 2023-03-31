# uni / plot / data_analysis
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f(x,a,b):
    return a*x+b
    
#data
temperatures = [23.2,27.2,36.2,42.7,49,54.6,61.1,67.4,73.5,79.2,85.4,91.2,97.5,99.5]
anz = len(temperatures)
times = range(0,anz*30,30)

#fit
par, pcov = curve_fit(f, times, temperatures)

#c
c=1/par[0]
print("Wäremespeicherkapazität c:",c)

#plot
plt.plot(times,temperatures, "x",label="data")
name = f"fit: {round(par[0],3)}K/kWs$\cdot$E+ {round(par[1],3)} °C"
plt.plot(times, [par[0]*i+par[1] for i in times], linestyle="dashed", label=name)
plt.title("specific heat capacity")
plt.xlabel("time in s / Energy in kWs")
plt.ylabel("Temperature")
plt.legend()
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
text = "c = Q/(M*T) = "+str(round(1/par[0],3))+"kJ/(kg*K)"
plt.text(80, 90, text , fontsize=10, horizontalalignment='center',verticalalignment='center', bbox=props)
plt.savefig("heat_capacity.png")
plt.show()
