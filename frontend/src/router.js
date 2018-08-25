import Vue from 'vue'
import Router from 'vue-router'
import About from './views/About.vue'
import MeterManagement from './views/MeterManagement.vue'
import Admin from './views/Admin.vue'
import NetworkUtilization from './views/NetworkUtilization.vue'

Vue.use(Router)

export default new Router({
  routes: [{
      path: '/',
      name: 'home',
      component: About
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import ( /* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/metermanagement',
      name: 'metermanagement',
      component: MeterManagement
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin
    },
    {
      path: '/networkutilization',
      name: 'networkutilization',
      component: NetworkUtilization
    }
  ]
})