import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const title = 'ITR | '

const routes = [
  {
    path: '/',
    name: 'Live',
    beforeEnter: (to, from, next) => {
      document.title = title + 'Live'
      next()
    },
    component: () => import('@/views/Home')
  },
  {
    path: '/call-in',
    name: 'Call-In',
    beforeEnter: (to, from, next) => {
      document.title = title + 'Call-In'
      next()
    },
    component: () => import('@/views/Call-In.vue')
  },
  {
    path: '/booking',
    name: 'Booking',
    beforeEnter: (to, from, next) => {
      document.title = title + 'Booking'
      next()
    },
    component: () => import('@/views/Booking.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    return { x: 0, y: 0 }
  }
})

export default router
