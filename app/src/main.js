/*eslint no-console: ["error", { allow: ["log"] }] */

import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  data: () => ({
    data: null,
    debug: null
  }),
  methods: {
  },
  computed: {
    loaded() {
      return this.data != null;
    }
  },
  mounted() {
    // Fetch the initial page data MVC style
    var elem = document.getElementById('data');
    var data = elem.attributes.data.value;
    var debug = elem.attributes.debug.value;
    this.data = JSON.parse(data);
    this.debug = debug === 'True';
  }
}).$mount('#app')
