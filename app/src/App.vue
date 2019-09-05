<template>
  <div>
    <Home v-if="route === 'home'"/>
    <Archive v-if="route === 'archive'"/>
  </div>
</template>

<script>
/*eslint no-console: ["error", { allow: ["log"] }] */
import Home from './components/Home';
import Archive from './components/Archive';

export default {
  name: 'App',
  components: {
    Home,
    Archive
  },
  data() {
    return {
    }
  },
  computed: {
    route() {
      var path = window.location.pathname;
      switch (path) {
        case '/archive':
          return 'archive';
        default:
          return 'home';
      }
    }
  },
  mounted() {
  }
};
</script>

<style>
/* Global application styles */
* {
	font-family: 'Droid Sans Mono';
	color: #222;
	box-sizing: border-box;
}
ul, li {
	list-style: none;
	padding: 0;
}
.pointer {
  cursor: pointer;
}
</style>
