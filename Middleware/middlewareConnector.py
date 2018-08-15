import sys
sys.path.insert(0,'../CustomMeter/PythonControllerScript')
import time
import blockchainConnector as bc
import databaseLogger as dl
import loadControllerInterface as lci
import display

# returns current mWh power consumption/production
def calcEnergy(power, time):
    return ((power * time) / 3600) * 1000

if __name__ == '__main__':
    isProducer = False
    polingDelay = 1
    StartingBalance = 100
    startTime = 0
    energyConsumed = 0
    bc.loadTokenContract()
    showDisplay = True
    # Infinite loop to poll status of the meter
    while True:
        # If meter set up for producer
        if isProducer:
            pass

        # If meter set up for consumer
        else:
            #powerDraw = sc.queryPower()
            powerDraw = lci.queryPower()
            endTime = time.time()  # end time of previous consumption period
            if startTime != 0:
                elapsedTime = endTime - startTime
                energyConsumed = calcEnergy(powerDraw, elapsedTime)

                # if the wallet ballance would be set to <0, make the token balance zero else decrement tokens
                if (bc.getBalance()- energyConsumed <= 0):
                    bc.burnToken(bc.getBalance())
                else:
                    bc.burnToken(int(energyConsumed))
                if showDisplay:
                    display.addRow([powerDraw,round(elapsedTime,5),round(energyConsumed,5),bc.getBalance()])
                    display.displayTable()
                dl.createEntry(powerDraw,bc.getBalance,True)

            startTime = time.time()

            # toggle light state based on ballance
            if bc.getBalance() > 0:
                lci.powerOn()
                
            else:
                lci.powerOff()

            time.sleep(polingDelay)