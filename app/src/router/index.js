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
