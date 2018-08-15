#This script is used to perform some basic comutation regarding
#finding midpoints, calculating voltage and current from readings
#and calculating power consumed at any point in time
from __future__ import division
import math
import numpy as np

voltageCalibrationFactor = 1.0
#This calculated accomidates for the voltage devider, parrellel resistor combination,
#capacitor and voltage transformer turns ratio
voltageOutputConversion = 138.1596831

currentCalibrationFactor = 1.0
#this takes into account the voltage devider circut, capacitor
#and the turns ratio of the current transformer
currentOutputConversion = 20.63661977

def calibrateVoltage(actual,measured):
    voltageCalibrationFactor = actual/measured

def calibrateCurrent(actual,measured):
    currentCalibrationFactor = actual/measured

def calcMidPoint(samples):
    return sum(samples) / len(samples)

def calcMaxMin(samples):
    return [max(samples),min(samples)]

def calcPeakToPeak(samples):
    return (max(samples)- min(samples))

def calcNormalizedSamples(samples):
    midpoint = calcMidPoint(samples)
    return [sample - midpoint for sample in samples]

def calcInstantaniousOutputCurrent(samples):
    normalizedSamples = calcNormalizedSamples(samples)
    return [sample*currentOutputConversion*currentCalibrationFactor for sample in normalizedSamples]

def calcInstantaniousOutputVoltage(samples):
    normalizedSamples = calcNormalizedSamples(samples)
    return [sample*voltageOutputConversion*voltageCalibrationFactor for sample in normalizedSamples]

def calcRMS(Vp):
    return Vp/(math.sqrt(2.0))

def calcOutputRMSOverSamples(samples):
    return calcRMS(calcPeakToPeak(samples)/2)


def calcPower(voltage, current):
    return voltage*current

def isConsuming(samples):
    totalPower = 0.0
    for x in range(0,len(samples['voltage'])):
        totalPower += samples['voltage'][x]*samples['current'][x]
    if totalPower>0.0:
        return True
    if totalPower<0.0:
        return False
