import locale from 'element-ui/lib/locale/lang/en'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-theme-chalk';

import VueGun from 'vue-gun';
try {
  Vue.use(VueGun, {
    peers: [store.state.gunDBNetworkAddress]
  });
  console.log("GunDB connected")
  store.commit('setgunDBNetworkState', true)
} catch (e) {
  console.error("error connecting to gundb")
}


import {
  setWalletStatus
} from '../utils/web3Service.js'

//Set wallet variables from web3 every second(if changed)
setInterval(function () {
  (async () => {
    setWalletStatus()
  })()
}, 1000);

Vue.use(ElementUI, {
  locale
})

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')