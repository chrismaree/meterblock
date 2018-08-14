#basic script to test the loadcontroller functionality. turn on the load, sleep 5 seconds
# run max speed samples then turn load off. output voltage and current are then plotted.

import LoadController as lc
import LoadCalculationHelpers as lch
import matplotlib.pyplot as plt
from functools import reduce
from time import sleep

lc.loadOn()
sleep(3)

samplesnum = 1000
samples = lc.takeMaxSpeedSamples(samplesnum)

data1=lch.calcInstantaniousOutputVoltage(samples[0])
data2=lch.calcInstantaniousOutputCurrent(samples[1])

print(str(lch.calcOutputRMSOverSamples(data1)) + ' V_RMS')
print(str(lch.calcOutputRMSOverSamples(data2)) + ' A_RMS')

lc.loadOff()

t = range(0,samplesnum)

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

