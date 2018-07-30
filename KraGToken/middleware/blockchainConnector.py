from web3 import Web3, HTTPProvider
from solc import compile_source, compile_files
from web3.contract import ConciseContract
import json


web3 = Web3(HTTPProvider('http://localhost:8545'))
address = Web3.toChecksumAddress('0x345ca3e014aaf5dca488057592ee47305d9b3e10')


def loadTokenContract(address):
    with open('abi.json') as f:
        abi = json.load(f)
    return web3.eth.contract(abi=abi, address=address,
                             ContractFactoryClass=ConciseContract)




if __name__ == '__main__':

    tokenContract = loadTokenContract(address)

    print(address)

    print(tokenContract.symbol())

    print(tokenContract.totalSupply())

    print(tokenContract.burn(100, transact={'from': web3.eth.coinbase}))

    print(tokenContract.totalSupply())
