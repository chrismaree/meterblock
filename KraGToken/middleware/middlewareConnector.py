import time
import blockchainConnector as bc
import switchController as sc

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

    # Infinite loop to poll status of the meter
    while True:
        # If meter set up for producer
        if isProducer:
            pass

        # If meter set up for consumer
        else:
            powerDraw = sc.queryPower()
            endTime = time.time()  # end time of previous consumption period
            if startTime != 0:
                elapsedTime = endTime - startTime
                energyConsumed = calcEnergy(powerDraw["Power"], elapsedTime)
                print(energyConsumed)

                # if the wallet ballance would be set to <0, make the token balance zero else decrement tokens
                if (bc.getBalance()- energyConsumed <= 0):
                    bc.burnToken(bc.getBalance())
                else:
                    bc.burnToken(int(energyConsumed))
                print(
                    f"Power Consumed: {powerDraw['Power']}, elapsed Time {elapsedTime} Energy Consumed: {energyConsumed}, Wallet Balance {bc.getBalance()}")

            startTime = time.time()

            # toggle light state based on ballance
            if bc.getBalance() > 0:
                if sc.PowerOn() == False:
                    print("Light Failed to turn On")
            else:
                if sc.PowerOff():
                    print("Tokens depleted, light turned off")
                else:
                    print("Light Failed to turn off")

            time.sleep(polingDelay)





