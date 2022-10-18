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
    component: () => import('@/views/Live')
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
    path: '/chat',
    name: 'Chat',
    beforeEnter: (to, from, next) => {
      document.title = title + 'Chat'
      next()
    },
    component: () => import('@/views/Chat.vue')
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
  },
  {
    path: '/schedule',
    name: 'Schedule',
    beforeEnter: (to, from, next) => {
      document.title = title + 'Schedule'
      next()
    },
    component: () => import('@/views/Schedule.vue')
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
