import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-theme-chalk';

import VueGun from 'vue-gun';
Vue.use(VueGun, {
  peers: ['http://127.0.0.1:8080/gun']
});

Vue.use(ElementUI)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
