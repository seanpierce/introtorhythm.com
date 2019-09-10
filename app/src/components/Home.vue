<template>
  <div id="home">
    <Navigation />
    <BackgroundImage />
    <Modal v-if="showEpisodeInfoModal" type="episodeInfo"/>
    <Player />
  </div>
</template>

<script>
/*eslint no-console: ["error", { allow: ["log"] }] */
import Navigation from './partials/Navigation';
import BackgroundImage from './partials/BackgroundImage';
import Modal from './partials/modals/Modal';
import Player from './partials/Player';

export default {
  components: {
    Navigation,
    BackgroundImage,
    Modal,
    Player,
  },
  data() {
    return {
      playing: false,
      audio: new Audio(),
      showEpisodeInfoModal: false
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
    this.audio.src = this.$root.mediaUrl + this.currentEpisode.audio;
  }
}; 
</script>

<style scoped>
</style>
