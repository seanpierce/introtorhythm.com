import Vue from 'vue'
import VueRouter from 'vue-router'
import CallIn from '@/views/CallIn'

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
    component: CallIn
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
