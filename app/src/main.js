/*eslint no-console: ["error", { allow: ["log"] }] */

import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  data: () => ({
    data: null
  }),
  methods: {
  },
  mounted() {
    var elem = document.getElementById('data');
    var data = elem.attributes.data.value;
    this.data = JSON.parse(data);
  }
}).$mount('#app')
