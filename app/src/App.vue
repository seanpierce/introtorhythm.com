<template>
  <div id="app">
    <Nav />
    <div id="container">
      <router-view />
    </div>
    <Footer v-if="!showChat" />
    <Player />
    <InfoModal v-if="modal === 'info'" />
  </div>
</template>

<script>
import Nav from '@/components/Nav'
import Footer from '@/components/Footer'
import Player from '@/components/Player'
import InfoModal from '@/components/Modals/Info'

export default {

  components: {
    Nav,
    Footer,
    Player,
    InfoModal
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