<template>
  <div id="archive">
    <h1>Archive</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
    }
  },
  computed: {
    episodes() {
      return this.$root.data.episodes;
    }
  }
}; 
</script>

<style scoped>
</style>
