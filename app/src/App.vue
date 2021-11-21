<template>
  <div id="app">
    <Nav />
    <div id="container">
      <router-view v-if="!showChat" />
      <Chat v-show="showChat" />
    </div>
    <Footer v-if="!showChat" />
    <Player />
    <InfoModal v-if="modal === 'info'" />
  </div>
</template>

<script>
import Nav from '@/components/Nav'
import Chat from '@/components/Chat/Chat'
import Footer from '@/components/Footer'
import Player from '@/components/Player'
import InfoModal from '@/components/Modals/Info'

export default {

  components: {
    Nav,
    Chat,
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
      let options = ['Episode', 'Live']
      return options.indexOf(this.$route.name) > -1
    },

    showChat() {
      return this.$store.state.chat.showChat
    }
  },

  created() {
    this.$store.dispatch('initialize')
    setInterval(() => {
      // poll for new background images
      this.$store.dispatch('pollBgImage')
    }, 120000) // two minutes
  }
}
</script>