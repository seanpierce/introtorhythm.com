<template>
  <div id="app">
    <Nav />
    <router-view/>
    <img id="logo" 
      v-show="showLogo"
      class="flip"
      :src="require('@/assets/images/itr-logo.png')" alt="Intro To Rhythm logo" />
    <Chat v-bind:class="{ 'show-chat': showChat }" />
  </div>
</template>

<script>
import Nav from '@/components/Nav'
import Chat from '@/components/Chat/Chat'

export default {

  components: {
    Nav,
    Chat
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