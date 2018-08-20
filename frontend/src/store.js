import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    netIdString: '',
    walletBalance: '',
    defaultEthWallet: '',
    isWalletUnlocked: false,
    isInjected: false,
    kraGTokenAddress: "0xc2d4a7b3024479a6b2b50864c04cbb5f52cb8700",
    gunDBNetworkState: false,
    gunDBNetworkAddress: 'http://127.0.0.1:8080/gun'
  },
  getters: {},
  mutations: {
    setNetworkId(state, netIdString) {
      state.netIdString = netIdString
    },
    setDefaultEthWallet(state, walletAddress) {
      state.defaultEthWallet = walletAddress
    },
    setUnlockedAccounts(state, unlockedAccounts) {
      state.unlockedAccounts = unlockedAccounts
    },
    setWalletBalance(state, walletBalance) {
      state.walletBalance = walletBalance
    },
    setgunDBNetworkState(state, gunDBNetworkState) {
      state.gunDBNetworkState = gunDBNetworkState
    },
    setisInjected(state, isInjected) {
      state.isInjected = isInjected
    },
    setisWalletUnlocked(state, isWalletUnlocked) {
      state.isWalletUnlocked = isWalletUnlocked
    }
  },
  actions: {}
})

export default store