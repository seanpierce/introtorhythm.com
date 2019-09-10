<template>
  <div class="nav" v-if="loaded">
    <div id="play-button-container">
      <button 
        id="play-button" 
        v-bind:style="{ 
          backgroundImage: 'url(' + playButtonBackgroundUrl + ')', 
          backgroundColor: 'rgba(0,0,0,0)'
        }"
        @click="togglePlay()"></button>
    </div>
    <ul>
      <li><a href="/">Intro To Rhythm</a><li>
      <li>------</li>
      <li>Now Playing: Ep {{ currentEpisode.number }}</li>
      <li id="tracktime">{{ $parent.currentTime }} / {{ $parent.totalTime || '00:00:00' }}</li>
      <li>
        <span 
          class="red pointer"
          @click="showEpisodeInfoModal()">
          See Ep {{ currentEpisode.number }} Info &lt;
        </span>
      </li>
      <li>------</li>
      <li v-for="episode in episodes" :key="episode.number" :class="isCurrent(episode.number) ? 'red': ''">
        <a :href="'/' + episode.number">{{ episode.number }}- {{ episode.title }}</a>
      </li>
      <li>------</li>
      <li><span class="pointer">About ITR</span></li>
      <li><a href="/archive">Archive</a></li>
      <SubscriptionForm />
    </ul>
  </div>
</template>

<script>
import SubscriptionForm from './SubscriptionForm.vue';
export default {
  components: {
    SubscriptionForm
  },
  data() {
    return {
    }
  },
  methods: {
    isCurrent(number) {
      return this.currentEpisode.number === number;
    },
    togglePlay() {
      this.$parent.togglePlay();
    },
    showEpisodeInfoModal() {
      this.$parent.showEpisodeInfoModal = true;
    },
  }, 
  computed: {
    debug() {
      return this.$root.debug;
    },
    loaded() {
      return this.$root.loaded;
    },
    currentEpisode() {
      return this.$root.data.current_episode;
    },
    episodes() {
      return this.$root.data.episodes;
    },
    playing() {
      return this.$parent.playing;
    },
    playButtonBackgroundUrl() {
      var url = '';
      if (this.debug) {
        url += '/assets/images'
      } else {
        url += '/static/images'
      }
      if (this.playing) {
        url += '/pause.png'
      } else {
        url += '/play.png'
      }
      return url;
    }
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
#play-button-container {
	width: 200px;
	text-align: center;
	height: 200px;
	position: fixed;
	top:0;
	bottom: 0;
	left: 0;
	right: 0;
	margin: auto;
	z-index: 1;
}
#play-button {
	height:200px;
	width: 200px;
	border: none;
	background-size: 50% 50%;
	background-repeat: no-repeat;
	background-position: center;
	outline:none;
	cursor: pointer;
}
.play { 
  background: url('/static/images/play.png');
}
.pause {
  background: url('/static/images/pause.png');
}
@media (max-width: 750px) {
	.nav ul {
		margin-top: 200px;
	}
	#play-button-container {
		position: absolute;
		bottom: unset;
	}
}
@media (max-width: 500px) {
	.nav {
		width: 100%;
    background: rgba(255, 255, 255, 0.7)
	}
}
</style>
