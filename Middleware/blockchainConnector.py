# blockchain imports
from web3 import Web3, HTTPProvider
from solc import compile_source, compile_files
from web3.contract import ConciseContract

# other imports
import json
import colours
import sys

#web3Provider = 'http://localhost:8545'
web3Provider = 'http://142.93.131.22:8545'

try:
    web3 = Web3(HTTPProvider(web3Provider))
    colours.printGreen(f"Connected to RPC blockchain endpoint on: {web3Provider}")
except:
    colours.printRed("Failed to connect to blockchain...closing")
    sys.exit()
address = Web3.toChecksumAddress('0x345ca3e014aaf5dca488057592ee47305d9b3e10')
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
    return web3.eth.accounts[0]


def getBalance():
    return tokenContract.balanceOf(web3.eth.accounts[0])


def getTotalSupply():
    return tokenContract.totalSupply()


def getSymbol():
    return tokenContract.symbol()


def getName():
    return tokenContract.name()


def transfer(address_to, ammount):
    return tokenContract.transfer(address_to, ammount, transact={'from': web3.eth.accounts[0]})


def mintToken(value):
    return tokenContract.mint(web3.eth.accounts[0], value, transact={'from': web3.eth.accounts[0]})


def burnToken(value):
    return tokenContract.burn(value, transact={'from': web3.eth.accounts[0]})
