import requests
import colours
import sys
import os
import blockchainConnector as bc
import time
import json

ip = '10.0.0.206'
url = "http://"+ip+":3000/"

try:
    if(os.system("ping -c 1 "+ip+" > /dev/null 2>&1")==0):
        colours.printGreen("Switch online and responding")
    else:
        colours.printRed("Network error. Cant connect to gundb...closing")
        sys.exit()
except:
    colours.printRed("Network error. Cant test gundb...")
    sys.exit()

address = ''
try:
    address = bc.getNodeAddress()
    colours.printGreen("Retreived Node Address")
except:
    colours.printRed("Could Not get node address")
    sys.exit()

def createPost(extension, payload):
    r = requests.post(url + extension, json=payload)

def createEntry(power, tokens):
    payload = {
        "key":address.lower(),
        "value": 
        {
            "power": power,
            "tokens": tokens,
        },
        "time": int(time.time()) 
    }
    createPost("addEntry", payload)
    
