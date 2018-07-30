import requests
import colours
import sys
import os

ip = '10.0.0.5'
url = f"http://{ip}/cm?cmnd="


if(os.system(f"ping -c 1 {ip}  > /dev/null 2>&1")==0):
    colours.printGreen("Switch online and responding")
else:
    colours.printRed("Network error. Cant connect to switch...closing")
    sys.exit()


def runQuery(query):
    try:
        return requests.get(query)
    except:
        colours.printRed("Could not execute query...closing")
        sys.exit()

def queryPower():
    command = 'Status%208'
    response = runQuery(url + command)
    return (response.json()['StatusSNS']['ENERGY']["Power"])

def PowerOff():
    command = 'Power%20Off'
    response = runQuery(url + command)
    if response.json()["POWER"] == "OFF":
        return True
    return False


def PowerOn():
    command = 'Power%20On'
    response = runQuery(url + command)
    if response.json()["POWER"] == "ON":
        return True
    return False
