<template>
  <div id="app">
    <Nav />
    <div id="container">
      <router-view v-if="!showChat" />
      <NewChat v-if="showChat" />
    </div>
    <Footer v-if="!showChat" />
    <!-- <Chat v-bind:class="{ 'show-chat': showChat }" /> -->
    <Player />
    <InfoModal v-if="modal === 'info'" />
  </div>
</template>

<script>
import Nav from '@/components/Nav'
// import Chat from '@/components/Chat/Chat'
import NewChat from '@/components/Chat/_Chat'
import Footer from '@/components/Footer'
import Player from '@/components/Player'
import InfoModal from '@/components/Modals/Info'

export default {

  components: {
    Nav,
    // Chat,
    NewChat,
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
  }
}
</script>