import LoadController as lc
import LoadCalculationHelpers as lch
from time import sleep

standardQuerySize = 100

voltageCurrentSamples = []

def queryPower():
    global voltageCurrentSamples
    samples = lc.takeMaxSpeedSamples(standardQuerySize)
    
    voltage = lch.calcInstantaniousOutputVoltage(samples['voltage'])
    current = lch.calcInstantaniousOutputCurrent(samples['current'])
    
    voltageCurrentSamples = {'voltage': voltage, 'current': current}
    
    voltageRMS = lch.calcOutputRMSOverSamples(voltage)
    currentRMS = lch.calcOutputRMSOverSamples(current)
    
    return (lch.calcPower(voltageRMS, currentRMS))

def powerOff():
    lc.loadOff()

def powerOn():
    lc.loadOn()

def isConsuming():
    global voltageCurrentSamples
    return lch.isConsuming(voltageCurrentSamples)
    
