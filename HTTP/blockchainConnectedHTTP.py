import sys
import random
from threading import Timer

from web3 import Web3, HTTPProvider
from solc import compile_source, compile_files
from web3.contract import ConciseContract

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

def deployAccountingContract():
    with open('../Contracts/BasicWallet.sol', 'r') as myfile:
        accountingContract_file = myfile.read()

    accountingContract_interface = compile_contract(accountingContract_file, 'StakeSimulator')
    (accountingContract_contract, accountingContract_address) = deploy_contract(accountingContract_interface, gas=6000000)
    print('Accounting Contract Address: ', accountingContract_address)
    return (accountingContract_interface, accountingContract_contract, accountingContract_address)



if __name__ == '__main__':
    print("run")
    (accountingContract_interface, accountingContract_contract, accountingContract_address) = deployAccountingContract()
