import Web3 from 'web3'
import store from '../src/store'


try {
    if (typeof web3 !== 'undefined') {
        web3 = new Web3(web3.currentProvider)
    } else {
        web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'))
    }
    store.commit('setisInjected', true)
} catch (e) {
    console.log("Web3 not found!")
    store.commit('setisInjected', false)
}


const NETWORKS = {
    '1': 'Main Net',
    '2': 'Deprecated Morden test network',
    '3': 'Ropsten test network',
    '4': 'Rinkeby test network',
    '42': 'Kovan test network'
}

const getNetIdString = async () => {
    const id = await web3.eth.net.getId()
    if (typeof id === 'number') {
        return NETWORKS[id] || 'Truffle Test Network'
    } else {
        return ''
    }
}

const getWalletBalance = async () => {
    const walletBalance = await web3.eth.getBalance(store.state.defaultEthWallet)
    return walletBalance
}

const getEthWallets = () =>
    new Promise((resolve, reject) => {
        web3.eth.getAccounts((err, res) => {
            if (!err) return resolve(res)
            reject(err)
        })
    })

const setWalletStatus = async () => {
    if (store.state.isInjected == true) {
        try {
            const ethWallets = await getEthWallets()
            if (store.state.defaultEthWallet != ethWallets[0]) {
                store.commit('setDefaultEthWallet', ethWallets[0])
            }
        } catch (e) {
            console.error('Could not set wallet address: ' + e)
        }

        //Get Wallet balance
        try {
            const walletBalance = await getWalletBalance()
            if (store.state.walletBalance != walletBalance) {
                store.commit('setWalletBalance', walletBalance)
                store.commit('setisWalletUnlocked', true)
            }
        } catch (e) {
            if (store.state.walletBalance != -1) {
                store.commit('setWalletBalance', -1)
            }
        }

        //Get network ID string
        try {
            const netIdString = await getNetIdString()
            if (store.state.netIdString != netIdString) {
                store.commit('setNetworkId', netIdString)
            }

        } catch (e) {
            console.error('Could not set network ID: ' + e)
        }

        //Check if wallet is unlocked
        if (store.state.walletBalance == -1 && store.state.defaultEthWallet != '') {
            if (store.state.isWalletUnlocked != false) {
                store.commit('setisWalletUnlocked', false)
            }
        }
    }
}

export {
    web3,
    getEthWallets,
    getWalletBalance,
    getNetIdString,
    setWalletStatus
}