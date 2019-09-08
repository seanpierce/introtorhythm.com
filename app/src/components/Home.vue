<template>
  <div id="home">
    <Navigation />
    <Player />
  </div>
</template>

<script>
/*eslint no-console: ["error", { allow: ["log"] }] */
import Navigation from './partials/Navigation';
import Player from './partials/Player';

export default {
  components: {
    Navigation,
    Player,
  },
  data() {
    return {
      playing: false,
      audio: new Audio()
    }
  },
  computed: {
    currentEpisode() {
      return this.$root.data.current_episode;
    },
    episodes() {
      return this.$root.data.episodes;
    },
  },
  mounted() {
    this.audio.src = this.currentEpisode.audio;
  }
}; 
</script>

<style scoped>
</style>
