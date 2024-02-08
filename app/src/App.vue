<template>
  <div id="app">
    <div id="container">
      <router-view />
      
      <Chat />
    </div>
  </div>
</template>

<script>
import Chat from '@/components/Chat/Chat.vue';

export default {
  components: {
    Chat
  },
  
  computed: {
    showChat() {
      return this.$route.name === 'Chat'
    }
  },

  created() {
    this.$store.dispatch('initialize')
  }
}
</script>