<template>
  <div>
    <Home />
  </div>
</template>

<script>
/*eslint no-console: ["error", { allow: ["log"] }] */

import Home from './components/Home';

export default {
  name: 'App',
  components: {
    Home,
  },
  data: () => ({
    data: null
  }),
  mounted() {
    // var app = document.getElementById('app')
    console.log(document)
  }
};
</script>
