# basic script to retrieve power consumed by sonoff POW from HTTP
import requests
import time

ip = '10.0.0.5'
url = f"http://{ip}/cm?cmnd="
polingDelay = 1
print(url)
wallet = 500
startTime = 0
energyConsumed = 0


def queryPower():
    command = 'Status%208'
    response = requests.get(url + command)
    return (response.json()['StatusSNS']['ENERGY'])


def calcEnergy(power, time):
    return ((power * time) / 3600) * 1000


def PowerOff():
    command = 'Power%20Off'
    response = requests.get(url + command)
    return (response.json())


if __name__ == '__main__':
    while (True):

        powerQuery = queryPower()

        endTime = time.time()

        if startTime != 0:
            elapsedTime = endTime - startTime
            energyConsumed = calcEnergy(powerQuery["Power"], elapsedTime)
            wallet -= energyConsumed
            print(
                f"Power Consumed: {powerQuery['Power']}, elapsed Time {elapsedTime} Energy Consumed: {energyConsumed}, Wallet Ballance {wallet}")

        startTime = time.time()

        if (wallet < energyConsumed):
            if (PowerOff()["POWER"] == "OFF"):
                print("Tokens depleted, light turned off")
            else:
                print("Light Failed to turn off")

        time.sleep(polingDelay)
