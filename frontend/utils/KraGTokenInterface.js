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
    let totalSupply = await contractInstance.totalSupply()
    return totalSupply['c'][0] //need to do this to deal with big number returned from web3
}

const getDecimals = async () => {
    let decimals = await contractInstance.decimals()
    return decimals['c'][0] //need to do this to deal with big number returned from web3
}

const getAllMeters = async () => {
    return await contractInstance.getAllMeters()
}

const mintTokensTo = async (amount, recipient) => {
    return await contractInstance.mintTo(amount, recipient, {
        from: store.state.defaultEthWallet,
        gasPrice: 2000000000,
        gas: '2000000'
    })
}

const registerMeter = async (meterAddress, ownerAddress) => {
    return await contractInstance.enroleMeter(meterAddress, ownerAddress, {
        from: store.state.defaultEthWallet,
        gasPrice: 2000000000,
        gas: '2000000'
    })
}

const balanceOf = async (address) => {
    return await contractInstance.balanceOf(address)
}

const meterOwnerOf = async (address) => {
    return await contractInstance.meterToOwner(address)
}

loadKragToken()

export {
    loadKragToken,
    getOwnerAddress,
    getName,
    getSymbol,
    getTotalSupply,
    getDecimals,
    getAllMeters,
    mintTokensTo,
    registerMeter,
    balanceOf,
    meterOwnerOf
}