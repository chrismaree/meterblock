import sys
import os
sys.path.insert(0,'../CustomMeter/PythonControllerScript')
import time
import blockchainConnector as bc
import databaseLogger as dl
import loadControllerInterface as lci
import display
import colours

# returns current mWh power consumption/production
def calcEnergy(power, time):
    return ((power * time) / 3600) * 1000

if __name__ == '__main__':
    try:
        meterProducerMode = int(os.environ['METERMODE'])
        colours.printGreen("Enviroment Variable included! Using meterProducerMode: " + str(meterProducerMode))
        if meterProducerMode != 0 and meterProducerMode != 1:
            colours.printRed("invalid meter meterProducerMode! closing...")
            sys.exit()
    except:
        colours.printYellow("Enviroment Variable NOT included! Using meterProducerMode=False")
        meterProducerMode=0
        
    polingDelay = 1
    StartingBalance = 100
    startTime = 0
    energyConsumed = 0
    bc.loadTokenContract()
    showDisplay = True
    # Infinite loop to poll status of the meter
    while True:
        endTime = time.time()  # end time of previous consumption period
        #We dont decrement on the initial sample as this has not end time so the value would be incorrect for
        #sample duration
        if startTime != 0:
            elapsedTime = endTime - startTime
            powerValue = lci.queryPower()
            isConsuming = lci.isConsuming()
            if(meterProducerMode):
                isConsuming = not isConsuming
            energyValue = int(calcEnergy(powerValue, elapsedTime))
            if (isConsuming):
                # if the wallet ballance would be set to <0, make the token balance zero else decrement tokens
                if (bc.getBalance()- energyConsumed <= 0):
                    bc.burnToken(bc.getBalance())
                else:
                    bc.burnToken(int(energyValue))
                dl.createEntry(int(powerValue),bc.getBalance())
            else: #if the meter is not consuming, it is producing so mint
                bc.mintToken(int(energyValue))
                dl.createEntry(-int(powerValue),bc.getBalance())
            if showDisplay:
                display.addRow([powerValue,round(elapsedTime,5),round(energyValue,5),bc.getBalance()])
                display.displayTable()
        startTime = time.time()
        # toggle light state based on ballance
        if bc.getBalance() > 0:
            lci.powerOn()
            
        else:
            lci.powerOff()
        time.sleep(polingDelay)
