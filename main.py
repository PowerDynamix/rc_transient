import numpy as np
import matplotlib.pyplot as plt

def calcVc(V_s,t,tc):
    return V_s*(1-np.e**(-t/tc))

def calcI(I_i,t,tc):
    return I_i*np.e**(-t/tc)

def main():
    # Main input
    V_battery = 10
    R = 2500
    C = 0.0002
    num_tc = 10

    # Constants
    tc = R*C

    # Main outputs
    I = 10/2500
    showV = False

    x = np.linspace(0,tc*num_tc,V_battery*10)
    x_ticks = np.zeros(num_tc,dtype=float)
    x_labels = []
    for i in range(1,num_tc+1):
        x_ticks[i-1] = tc*i
        x_labels.append(str(i)+"τ")
    
    if showV:
        # Show voltage of capacitor during charging phase
        y = calcVc(V_battery,x,tc)
        plt.figure(figsize=(15,5))
        plt.plot(x,y,color="green",linewidth=2)
        plt.xlabel("Time")
        plt.xticks(x_ticks,labels=x_labels)
        plt.ylabel("Voltage (V)")
        plt.grid(True,linestyle=":",alpha=0.6)
    else:
        # Show current during charging phase
        y = calcI(I,x,tc)
        plt.figure(figsize=(15,5))
        plt.plot(x,y,color="red",linewidth=2)
        plt.xlabel("Time")
        plt.xticks(x_ticks,labels=x_labels)
        plt.ylabel("Current (mA)")
        plt.grid(True,linestyle=":",alpha=0.6)
    
    plt.show()
    

if __name__ == "__main__":
    main()