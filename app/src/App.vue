<template>
  <div id="app">
    <Nav />
    <div id="container">
      <router-view/>
    </div>
    <Footer />
    <Chat v-bind:class="{ 'show-chat': showChat }" />
    <Player />
    <InfoModal v-if="modal === 'info'" />
    <SupportModal v-if="modal === 'support'" />
  </div>
</template>

<script>
import Nav from '@/components/Nav'
import Chat from '@/components/Chat/Chat'
import Footer from '@/components/Footer'
import Player from '@/components/Player'
import InfoModal from '@/components/Modals/Info'
import SupportModal from '@/components/Modals/Support'

export default {

  components: {
    Nav,
    Chat,
    Footer,
    Player,
    InfoModal,
    SupportModal
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