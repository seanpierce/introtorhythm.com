<template>
  <div id="home">
    <Navigation />
  </div>
</template>

<script>
/*eslint no-console: ["error", { allow: ["log"] }] */
import Navigation from './partials/Navigation';

export default {
  components: {
    Navigation
  },
  data() {
    return {
      test: null
    }
  },
  computed: {
    currentEpisode() {
      return this.$root.data.current_episode;
    },
    episodes() {
      return this.$root.data.episodes;
    },
  }
}; 
</script>

<style scoped>
</style>
