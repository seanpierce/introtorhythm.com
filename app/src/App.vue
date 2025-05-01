<script setup lang="ts">
import { RouterView } from 'vue-router'
import Chat from './components/Chat.vue'
import Info from './components/Info.vue'
</script>

<template>
  <div id="app">
    <div id="container">
      <RouterView />
      <Chat />
      <Info />
    </div>
  </div>
</template>

<style scoped>
</style>
