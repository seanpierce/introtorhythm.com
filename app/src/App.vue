<template>
  <div id="app">
    <div id="container">
      <router-view />
    </div>
    <Player />
  </div>
</template>

<script>
import Player from '@/components/Player'

export default {

  components: {
    Player
  },

  data() {
    return {
      modal: null
    }
  },

  computed: {

    showLogo() {
      const options = ['Episode', 'Live']
      return options.includes(this.$route.name)
    },

    showChat() {
      return this.$route.name === 'Chat'
    }
  },

  created() {
    this.$store.dispatch('initialize')
    setInterval(() => {
      // poll for new background images
      this.$store.dispatch('pollRefreshContent')
    }, 120000) // two minutes
  }
}
</script>