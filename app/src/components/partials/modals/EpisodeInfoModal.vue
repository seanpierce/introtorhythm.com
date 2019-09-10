<template>
    <div id="episode-info">
        <div v-html="content" style="color: white"></div>
    </div>
</template>

<script>
export default {
    computed: {
        content() {
            return this.$root.data.current_episode.content;
        }
    }
}
</script>

<style scoped>
</style>