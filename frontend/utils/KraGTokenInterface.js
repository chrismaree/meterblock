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
    console.log("KragTokenConract Loaded")
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

const mintTokensTo = async (_amount, _recipient) => {
    return await contractInstance.mintTo(_amount, _recipient, {
        from: store.state.defaultEthWallet,
        gasPrice: 2000000000,
        gas: '2000000'
    })
}

const registerMeter = async (_meterAddress, _ownerAddress) => {
    return await contractInstance.enroleMeter(_meterAddress, _ownerAddress, {
        from: store.state.defaultEthWallet,
        gasPrice: 2000000000,
        gas: '2000000'
    })
}

const balanceOf = async (address) => {
    return await contractInstance.balanceOf(address)
}

const balanceOfCurrentAddress = async () => {
    return await contractInstance.balanceOf(store.state.defaultEthWallet)
}

const meterOwnerOf = async (address) => {
    return await contractInstance.meterToOwner(address)
}

const getMetersToOwner = async () => {
    console.log(store.state.defaultEthWallet)
    return await contractInstance.getAllMetersForOwner(store.state.defaultEthWallet)
}

const transfer = async (_address, _value) => {
    console.log(_address)
    return await contractInstance.transfer("0x20e8652108d73044bb765bbb7355a10d10c8ec64", _value, {
        from: store.state.defaultEthWallet,
        gasPrice: 2000000000,
        gas: '2000000'
    })
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
    balanceOfCurrentAddress,
    meterOwnerOf,
    getMetersToOwner,
    transfer
}