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

  created() {
    this.$store.dispatch('initialize');

    setInterval(() => {
      this.$store.dispatch('pollRefreshContent');
    }, 120000)
  }
}
</script>