import requests
import colours
import sys
import os
import blockchainConnector as bc
import time

ip = '10.0.0.206'
url = "http://"+ip+":3000/"

if(os.system("ping -c 1 "+ip+" > /dev/null 2>&1")==0):
    colours.printGreen("Switch online and responding")
else:
    colours.printRed("Network error. Cant connect to switch...closing")
    sys.exit()

address = ''
try:
    address = bc.getNodeAddress
    colours.printGreen("Retreived Node Address")
except:
    colours.printRed("Could Not get node address")
    sys.exit()

def createPost(extension, payload):
    r = requests.post(url + extension, json=payload)
    print(r.json())
    return (r.json())

def createEntry(power, tokens, isConsuming):
    payload = {
        "key":address,
        "value": 
        {
            "power": power,
            "tokens": tokens,
            "isConsuming": isConsuming
        },
        "time": int(time.time()) 
    }
    createPost("addEntry", payload)
    
