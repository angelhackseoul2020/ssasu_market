import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Main.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/market',
    name: 'Market',
    component: () => import('../views/Market.vue'),
    children: [
      {
        path: 'home',
        name: 'home',
        component: () => import('../components/market/MarketHome.vue')
      },
      {
        path: 'store',
        name: 'store',
        component: () => import('../components/market/MarketStore.vue')
      },
      {
        path: 'community',
        name: 'community',
        component: () => import('../components/market/MarketCommunity.vue')
      }
    ]
  },
  {
    path:'/maps',
    name:'maps',
    component: () => import('../views/Maps.vue')
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
