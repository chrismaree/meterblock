# Basic Implementation of HTTP connected blockchain wallet system toggles light state based on contract token ballance

import requests
import time

from web3 import Web3, HTTPProvider
from solc import compile_source, compile_files
from web3.contract import ConciseContract


# Define starting values and constants
ip = '10.0.0.5'
url = f"http://{ip}/cm?cmnd="
polingDelay = 1
print(url)
StartingBalance = 100
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


def PowerOn():
    command = 'Power%20On'
    response = requests.get(url + command)
    return (response.json())


web3 = Web3(HTTPProvider('http://localhost:8545'))


def compile_contract(contract_file, contract_name):
    contract_sol = compile_source(contract_file)  # Compiled source code
    interface = contract_sol['<stdin>:' + contract_name]
    return interface


def deploy_contract(interface, gas=4100000, arguments=None):
    # Instantiate and deploy contract
    contract = web3.eth.contract(abi=interface['abi'], bytecode=interface['bin'])

    # Get transaction hash from deployed contract
    tx_hash = contract.deploy(transaction={'from': web3.eth.accounts[0], 'gas': gas}, args=arguments)

    # Get tx receipt to get contract address
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)
    contract_address = tx_receipt['contractAddress']

    # Contract instance in concise mode
    contract_instance = web3.eth.contract(abi=interface['abi'], address=contract_address,
                                          ContractFactoryClass=ConciseContract)

    return (contract_instance, contract_address)


def deployBasicWallet():
    with open('BasicWallet.sol', 'r') as myfile:
        basicWallet_file = myfile.read()

    basicWallet_interface = compile_contract(basicWallet_file, 'BasicWallet')
    (basicWallet_contract, basicWallet_address) = deploy_contract(basicWallet_interface, gas=6000000)
    print('Accounting Contract Address: ', basicWallet_address)
    return (basicWallet_interface, basicWallet_contract, basicWallet_address)


if __name__ == '__main__':

    # Deploy contract and load wallet with starting tokens
    (basicWallet_interface, basicWallet_contract, basicWallet_address) = deployBasicWallet()
    basicWallet_contract.setWalletBalance(StartingBalance, transact={'from': web3.eth.coinbase})

    # infinite loop to monitor the state of the light
    while (True):
        powerQuery = queryPower() #get current power consumed by light
        endTime = time.time() #end time of previous consumption period
        if startTime != 0:
            elapsedTime = endTime - startTime
            energyConsumed = calcEnergy(powerQuery["Power"], elapsedTime)
            print(energyConsumed)

            #if the wallet ballance would be set to <0, make the token balance zero else decrement tokens
            if (basicWallet_contract.walletBalance() - energyConsumed <= 0):
                basicWallet_contract.setWalletBalance(0, transact={'from': web3.eth.coinbase})
            else:
                basicWallet_contract.decrementTokens(int(energyConsumed), transact={'from': web3.eth.coinbase})
            print(
                f"Power Consumed: {powerQuery['Power']}, elapsed Time {elapsedTime} Energy Consumed: {energyConsumed}, Wallet Balance {basicWallet_contract.walletBalance()}")

        startTime = time.time()


        #toggle light state based on ballance
        if (basicWallet_contract.walletBalance() > 0):
            if (PowerOn()["POWER"] != "ON"):
                print("Light Failed to turn On")
        else:
            if (PowerOff()["POWER"] == "OFF"):
                print("Tokens depleted, light turned off")
            else:
                print("Light Failed to turn off")

        time.sleep(polingDelay)
