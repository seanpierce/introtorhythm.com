import Vue from 'vue'
import VueRouter from 'vue-router'
import Live from '@/views/Live'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Live',
    beforeEnter: (to, from, next) => {
      document.title = 'Intro To Rhythm | Live'
      next()
    },
    component: Live
  },
  {
    path: '/episodes',
    name: 'Episodes',
    beforeEnter: (to, from, next) => {
      document.title = 'Intro To Rhythm | Episodes'
      next()
    },
    component: () => import('@/views/Episodes.vue')
  },
  {
    path: '/episodes/:number',
    name: 'Episode',
    beforeEnter: (to, from, next) => {
      document.title = 'Intro To Rhythm | ' + to.params.number
      next()
    },
    props: true,
    component: () => import('@/views/Episode.vue')
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
