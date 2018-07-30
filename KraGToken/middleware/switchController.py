import requests

ip = '10.0.0.5'
url = f"http://{ip}/cm?cmnd="

def queryPower():
    command = 'Status%208'
    response = requests.get(url + command)
    return (response.json()['StatusSNS']['ENERGY'])

def PowerOff():
    command = 'Power%20Off'
    response = requests.get(url + command)
    if response.json()["POWER"] == "OFF":
        return True
    return False


def PowerOn():
    command = 'Power%20On'
    response = requests.get(url + command)
    if response.json()["POWER"] == "ON":
        return True
    return False
