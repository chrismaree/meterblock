import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import MeterUsage from './views/MeterUsage.vue'
import Admin from './views/Admin.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/meterusage',
      name: 'meterusage',
      component: MeterUsage
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin
    }
  ]
})
