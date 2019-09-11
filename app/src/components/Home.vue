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
      showEpisodeInfoModal: false,
      currentTime: '00:00:00',
      totalTime: null,
      playPercent: 0,
      playerWidth: 0,
      onplayhead: false
    }
  },
  methods: {
    togglePlay() {
      if (this.audio.paused) {
        this.playing = true;
        this.audio.play();
      } else {
        this.playing = false; 
        this.audio.pause();
      }
    },
    formatTime(input) {
      var sec_num = parseInt(input, 10);
      var hours   = Math.floor(sec_num / 3600);
      var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
      var seconds = sec_num - (hours * 3600) - (minutes * 60);
      if (hours   < 10) { hours   = "0" + hours; }
      if (minutes < 10) { minutes = "0" + minutes; }
      if (seconds < 10) { seconds = "0" + seconds; }
      return hours + ':' + minutes + ':' + seconds;
    },
    timeUpdate() {
      if (!this.totalTime)
        this.totalTime = this.formatTime(this.audio.duration);

      this.currentTime = this.formatTime(this.audio.currentTime);
      if (!this.onplayhead)
        this.playPercent = this.playerWidth * (this.audio.currentTime / this.audio.duration);
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
    this.audio.addEventListener('timeupdate', this.timeUpdate);
  }
}; 
</script>

<style scoped>
</style>
