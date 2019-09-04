<template>
  <div class="nav" v-if="loaded">
    <div id="play-button-container">
      <!-- <button id="play-button" class="play" onclick="play()"></button> -->
    </div>
    <ul>
      <li><a href="/">Intro To Rhythm</a><li>
      <li>------</li>
      <li>Now Playing: Ep {{ currentEpisode.number }}</li>
      <li id="tracktime">00:00:00 / 00:00:00</li>
      <li>
        <span 
          class="red pointer"
          onclick="openModal('info-modal')">
          See Ep {{ currentEpisode.number }} Info &lt;
        </span>
      </li>
      <li>------</li>
      <li v-for="episode in episodes" :key="episode.number" :class="isCurrent(episode.number) ? 'red': ''">
        <a :href="'/' + episode.number">{{ episode.number }}- {{ episode.title }}</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
    }
  },
  methods: {
    isCurrent(number) {
      return this.currentEpisode.number === number;
    }
  }, 
  computed: {
    loaded() {
      return this.$root.loaded;
    },
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
.nav {
	width: 320px;
	max-width: 100%;
	border-right: solid 1px #222;
	height: 100%;
	position: fixed;
	left: 0;
	top:0;
	background: rgba(255, 255, 255, 0.8);
	padding: 1em 1em;
	z-index: 3;
	overflow-y: scroll;
}

.nav ul {
	margin-bottom: 4em;
}
.nav ul li {
	margin: 0.5em 0;
}
.nav ul li a {
	text-decoration: none;
	color: inherit;
}
.red {
	color: red;
}
</style>
