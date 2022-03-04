import Vue from 'vue'
import VueRouter from 'vue-router'
import Live from '@/views/Live'

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
    component: Live
  },
  {
    path: '/episodes',
    name: 'Episodes',
    beforeEnter: (to, from, next) => {
      document.title = title + 'Episodes'
      next()
    },
    component: () => import('@/views/Episodes.vue')
  },
  {
    path: '/episodes/:number',
    name: 'Episode',
    beforeEnter: (to, from, next) => {
      document.title = title + to.params.number
      next()
    },
    props: true,
    component: () => import('@/views/Episode.vue')
  },
  {
    path: '/call-in',
    name: 'Cann-In',
    component: () => import('@/views/Call-In.vue')
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
