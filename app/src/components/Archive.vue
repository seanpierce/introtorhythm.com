<template>
  <div id="archive">
    <div><a href="/">Intro To Rhythm/</a></div>
    <div class="tab-1">archive/</div>
    <div class="tab-2">episodes/</div>
    <div class="tab-3">
      <li v-for="episode in episodes" :key="episode.number">
        <a :href="'/' + episode.number">{{ formatFileName(episode.number, episode.title) }}</a>
      </li>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
    }
  },
  methods: {
    formatFileName(number, title) {
      var formattedTitle = title.replace(/[-,./ !*:]/g, '_');
      return '/' + number + '_' + formattedTitle;
    } 
  },
  computed: {
    episodes() {
      return this.$root.data.episodes;
    }
  }
}; 
</script>

<style>
#archive {
  margin: 2em 1em;
}
#archive a {
  text-decoration: none;
}
#archive a:hover {
  text-decoration: underline;
}
.tab-1 {
  margin-left: 2em;
}
.tab-2 {
  margin-left: 4em;
}
.tab-3 {
  margin-left: 6em;
}
#archive div,
#archive li {
  margin-bottom: 8px;
}
</style>
