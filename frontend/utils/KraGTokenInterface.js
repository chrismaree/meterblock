import store from '../src/store'
import Web3 from 'web3'
import contract from 'truffle-contract'
import contractJSON from '../../KraGToken/build/contracts/KraGToken.json'
const Contract = contract(contractJSON)

if (typeof web3 !== 'undefined') {
    web3 = new Web3(web3.currentProvider)
    Contract.setProvider(web3.currentProvider)
} else {
    web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'))
    Contract.setProvider(new Web3.providers.HttpProvider('http://localhost:8545'))
}

let contractInstance

const loadKragToken = async () => {
    contractInstance = await Contract.at(store.state.kraGTokenAddress)
}

const getOwnerAddress = async () => {
    return await contractInstance.owner()
}

const getName = async () => {
    return await contractInstance.name()
}

const getSymbol = async () => {
    return await contractInstance.symbol()
}

const getTotalSupply = async () => {
    return await contractInstance.totalSupply()
}

const getDecimals = async () => {
    return await contractInstance.decimals()
}

loadKragToken()

export {
    loadKragToken,
    getOwnerAddress,
    getName,
    getSymbol,
    getTotalSupply,
    getDecimals
}