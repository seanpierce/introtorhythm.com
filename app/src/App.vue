<template>
  <div id="app">
    <div id="container">
      <router-view />
      <Chat />
      <Info />
    </div>
  </div>
</template>

<script>
import Chat from '@/components/Chat/Chat.vue';
import Info from './components/Info.vue';

export default {
  components: {
    Chat,
    Info
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