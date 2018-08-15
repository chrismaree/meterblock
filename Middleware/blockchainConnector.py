# blockchain imports
from web3 import Web3, HTTPProvider
from solc import compile_source, compile_files
from web3.contract import ConciseContract

# other imports
import json
import colours
import sys
import os


try:
    meterID = int(os.environ['METERID'])
    colours.printGreen("Enviroment Variable included! Using MeterID: " + str(meterID))

except:
    colours.printRed("Could not find meterID...please set the enviroment var")
    sys.exit()


#web3Provider = 'http://localhost:8545'
web3Provider = 'http://142.93.131.22:8545'

try:
    web3 = Web3(HTTPProvider(web3Provider))
    colours.printGreen("Connected to RPC blockchain endpoint on: "+web3Provider)
except:
    colours.printRed("Failed to connect to blockchain...closing")
    sys.exit()
address = Web3.toChecksumAddress('0xce9479ff82b69bea0b06a9867bc646e4259aa7e8')
tokenContract = ''

def loadTokenContract(address=address):
    global tokenContract
    if tokenContract == '':
        with open('abi.json') as f:
            abi = json.load(f)
        try:
            tokenContract = web3.eth.contract(abi=abi, address=address,
                                              ContractFactoryClass=ConciseContract)
            colours.printGreen("Token contract loaded!")
        except:
            colours.printRed("Token contract loading failed...closing")
            sys.exit()


def getTokenContractAddress():
    return address


def getNodeAddress():
    return web3.eth.accounts[meterID]


def getBalance():
    return tokenContract.balanceOf(web3.eth.accounts[meterID])


def getTotalSupply():
    return tokenContract.totalSupply()


def getSymbol():
    return tokenContract.symbol()


def getName():
    return tokenContract.name()


def transfer(address_to, ammount):
    return tokenContract.transfer(address_to, ammount, transact={'from': web3.eth.accounts[meterID]})


def mintToken(value):
    return tokenContract.mint(web3.eth.accounts[meterID], value, transact={'from': web3.eth.accounts[meterID]})


def burnToken(value):
    return tokenContract.burn(value, transact={'from': web3.eth.accounts[meterID]})
