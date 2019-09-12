<template>
  <div>
    <div id="mobile-nav-toggle" v-if="$parent.mobile">
      <div id="menu-container" @click="toggleMobileNav()" :class="{ 'change': $parent.showMobileNav }">
        <div class="bar1"></div>
        <div class="bar2"></div>
        <div class="bar3"></div>
      </div>
    </div>
    <div id="nav" v-if="loaded && showNav">
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
  </div>
</template>

<script>
/*eslint no-console: ["error", { allow: ["log"] }] */
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
    showEpisodeInfoModal() {
      this.$parent.showEpisodeInfoModal = true;
    },
    toggleMobileNav() {
      this.$parent.showMobileNav = !this.$parent.showMobileNav;
    },
    resize() {
      var width = document.documentElement.clientWidth;  
      if (width > 750)
        this.$parent.mobile = false;
      else
        this.$parent.mobile = true;
    }
  }, 
  computed: {
    showNav() {
      return this.$parent.mobile && this.$parent.showMobileNav || !this.$parent.mobile;
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
  },
  mounted() {
    window.addEventListener('resize', this.resize);
  }
}; 
</script>

<style scoped>
#nav {
	width: 320px;
	max-width: 100%;
	border-right: solid 1px #222;
	height: 100%;
	position: fixed;
	left: 0;
	top:0;
	background: rgba(255, 255, 255, 0.8);
	padding: 1em 1em;
	z-index: 11;
	overflow-y: scroll;
}

#nav ul {
	margin-bottom: 4em;
}
#nav ul li {
	margin: 0.5em 0;
}
#nav ul li a {
	text-decoration: none;
	color: inherit;
}
.red {
	color: red;
}
#mobile-nav-toggle {
  position: absolute;
  font-size: 3em;
  z-index: 12;
}
#menu-container {
  padding: 8px;
  display: inline-block;
  cursor: pointer;
}
.bar1, .bar2, .bar3 {
  width: 40px;
  height: 5px;
  background-color: black;
  margin: 6px 0;
  transition: 0.4s;
}
.change .bar1 {
  -webkit-transform: rotate(-45deg) translate(-9px, 6px);
  transform: rotate(-45deg) translate(-9px, 6px);
}
.change .bar2 {
  opacity: 0;
}
.change .bar3 {
  -webkit-transform: rotate(45deg) translate(-8px, -8px);
  transform: rotate(45deg) translate(-8px, -8px);
}
@media (max-width: 750px) {
  #nav {
    width: 100%;
    background: rgba(255, 255, 255, 0.6);
  }
  #nav ul {
    margin-top: 4em;
  }
}
</style>
