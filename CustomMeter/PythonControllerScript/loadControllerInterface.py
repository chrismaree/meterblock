import LoadController as lc
import LoadCalculationHelpers as lch
import matplotlib.pyplot as plt
from time import sleep

standardQuerySize = 100

def queryPower():
    samples = lc.takeMaxSpeedSamples(standardQuerySize)
    voltage = lch.calcInstantaniousOutputVoltage(samples[0])
    current = lch.calcInstantaniousOutputCurrent(samples[1])
    
    voltageRMS = lch.calcOutputRMSOverSamples(voltage)
    currentRMS = lch.calcOutputRMSOverSamples(current)
    
    return (lch.calcPower(voltageRMS, currentRMS))

def powerOff():
    lc.loadOff()

def powerOn():
    lc.loadOn()
    
powerOn()
for x in range(0,500):
    print(queryPower())    
    sleep(0.1)

powerOff()