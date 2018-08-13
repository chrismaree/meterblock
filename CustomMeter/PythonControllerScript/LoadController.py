from gpiozero import MCP3202, LED
import time
import math
#import matplotlib.pyplot as plt
from functools import reduce


load = LED(21)
voltageSensor = MCP3202(channel = 1, differential = False, max_voltage = 5.0)
currentSensor = MCP3202(channel = 0, differential = False, max_voltage = 5.0)

def takeMaxSpeedSamples(number):
    values = []
    for x in range(0,number-1):
        values.append([voltageSensor.value, currentSensor.value])
    return values

def takeDelayedSamples(number,delay):
    values = []
    for x in range(0,number-1):
        values.append([voltageSensor.value, currentSensor.value])
        time.sleep(delay)
    return values
    
def loadOff():
    load.off()
    
def loadOn():
    load.on()

def consuming(samples):
    totalPower = 0.0
    for sample in samples:
        totalPower+= sample[0]*sample[1]
    if totalPower>0.0:
        return True
    if totalPower<0.0:
        return False

