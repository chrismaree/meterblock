from gpiozero import MCP3202
import time
import math
import matplotlib.pyplot as plt
from functools import reduce


samples = 300

voltage = MCP3202(channel = 1, differential = False, max_voltage = 5.0)
current = MCP3202(channel = 0, differential = False, max_voltage = 5.0)

voltageValues = []
currentValues = []

for x in range(0,samples-1):
    voltageValues.append(voltage.value*5)
    #print(str(voltage.value)+ " " + str(current.value))
    currentValues.append(current.value*5)
    
    
t = range(0,samples-1)
data1 = voltageValues
data2 = currentValues

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('samples (n)')
ax1.set_ylabel('Voltage (V)', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Current(A)', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()



