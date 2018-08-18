import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    meterData:[]
  },
    getters: {},

  mutations: {
    pushToMeterData(state, _meterData){
      state.meterData.push(_meterData);
    }
  },
  actions: {}
})
