import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

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
    path: '/admin',
    name: 'Admin',
    component: () => import('../views/Admin.vue'),
    children: [
      {
        path: 'store',
        name: 'store',
        component: () => import('../components/admin/AdminStore.vue')
      },
      {
        path: 'addstore',
        name: 'addstore',
        component: () => import('../components/admin/AdminStoreAdd.vue')
      },
      {
        path: 'user',
        name: 'user',
        component: () => import('../components/admin/AdminUser.vue')
      },
      {
        path: 'adduser',
        name: 'adduser',
        component: () => import('../components/admin/AdminUserAdd.vue')
      },
    ]
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
      },
      {
        path: 'write',
        name: 'write',
        component: () => import('../components/market/CommunityWrite.vue')
      },
      {
        path: 'reviewdetail',
        name: 'reviewdetail',
        component: () => import('../components/market/ReviewDetail.vue')
      },
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
