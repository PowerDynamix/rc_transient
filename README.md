# RC Transient Simulator

Simulation of how voltage and current of a capacitor changes during RC circuit charging phase

## The main equations involved

V_c = V*(1-e^(-t/tc))
I_c=I*e^(-t/tc)

These model how much voltage or current is in the capacitor as time passes in terms of the time constnat τ, modeled by resistance and capacitance of the RC circuit.

To swap the plots to show either function, change the showV variable in the program to True or False depending on what outputs you want to see on the plot.

Plotting the x axis in terms of time constant allows you to easily figure out what percentage of the initial current or voltage remains in the circuit in that time.