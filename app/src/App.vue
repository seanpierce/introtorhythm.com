<template>
  <div id="app">
    <div id="container">
      <router-view />
    </div>
  </div>
</template>

<script>

export default {
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