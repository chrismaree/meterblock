from gpiozero import MCP3201
import time
import math
import matplotlib.pyplot as plt

samples = 40

pot = MCP3201(max_voltage=5.0)

values = []

for x in range(0,samples-1):
    values.append(pot.value*5-2.5)
    
max = max(values)
print("Max read voltage\t" +str(max))

min = min(values)
print("Min read voltage\t" +str(min))

ptp = max-min
print("Peak-to-peak\t" +str(ptp))

scalingFactor = (500.0/(500.0+2200.0+3.21))**-1.0
print("Scaling Factor\t" +str(scalingFactor))

secondaryPtp = ptp*scalingFactor
print("Secondary Peak-to-peak\t" +str(secondaryPtp))

turnsRatio = 25.81
print("Turns Ratio\t" +str(turnsRatio))

primaryPtp = secondaryPtp*turnsRatio
print("Primary Peak-to-peak\t" +str(primaryPtp))

primaryRMS = (primaryPtp/2)/math.sqrt(2)
print("Primary RMS\t" + str(primaryRMS))

actualVoltage = 231.0
#calibrationFactor = actualVoltage/primaryRMS
calibrationFactor = 1.0441795548146893
print("Calibration Factor\t"+str(calibrationFactor))

primaryRMS_calibrated = primaryRMS*calibrationFactor
print("Primary RMS_calibrated\t" + str(primaryRMS_calibrated))

voltageValues = []

for value in values:
    
    scalingFactor = (500.0/(500.0+2200.0+3.21))**-1.0
    secondaryPtp = value*scalingFactor*2*math.sqrt(2)
    turnsRatio = 25.81
    primaryPtp = secondaryPtp*turnsRatio
    primaryRMS = (primaryPtp/2)/math.sqrt(2)
    actualVoltage = 231.0
    primaryRMS_calibrated = primaryRMS*calibrationFactor
    voltageValues.append(primaryRMS_calibrated)
    print(primaryRMS_calibrated)
    


x = range(0,samples-1)
y = voltageValues
plt.stem(x, y)
plt.title('Voltage Over Samples')
plt.ylabel('Voltage (v)')
plt.xlabel('Samples n')
plt.show()

