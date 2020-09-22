import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import VueLazyload from 'vue-lazyload'
import '@/styles/index.scss'

Vue.use(VueLazyload, {
  // preLoad: 1.3,
  // error: 'dist/error.png',
  // loading: 'dist/loading.gif',
  attempt: 1
})

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
