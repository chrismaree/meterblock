#Base script to control and measure the load state. Defined data standard is an
#array of arrays, with the inner array representing voltage and curret for each
#reading as [[voltage_reading1,voltageReading2...],[currentReading1,currentReading2...]]
from gpiozero import MCP3202, LED
import time

maxADCVoltage = 5

load = LED(21)

voltageSensor = MCP3202(channel = 1, differential = False, max_voltage = 5.0)
currentSensor = MCP3202(channel = 0, differential = False, max_voltage = 5.0)

def takeMaxSpeedSamples(number):
    values = [[],[]]
    for x in range(0,number):
        values[0].append(voltageSensor.value*maxADCVoltage)
        values[1].append(currentSensor.value*maxADCVoltage)
    return values

def takeDelayedSamples(number,delay):
    values = [[],[]]
    for x in range(0,number-1):
        values[0].append(voltageSensor.value*maxADCVoltage)
        values[1].append(currentSensor.value*maxADCVoltage)
        time.sleep(delay)
    return values
    
def loadOff():
    load.off()
    
def loadOn():
    load.on()

