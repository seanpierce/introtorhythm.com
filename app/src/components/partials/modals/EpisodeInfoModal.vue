<template>
    <div id="episode-info" class="content">
        <div id="episode-heading">{{ currentEpisode.number }}- {{ currentEpisode.title }}</div>
        <div v-html="currentEpisode.content"></div>
        <div>
            ------------<br>
            <br>
            Share this episode on:<br>
            <a :href="'https://www.facebook.com/sharer/sharer.php?u=https://introtorhythm.com/' + currentEpisode.number" target="_blank">facebook</a> / <a :href="'https://twitter.com/home?status=https://introtorhythm.com/' + currentEpisode.number">twitter</a><br>
            <br>
            info@introtorhythm.com
        </div>
    </div>
</template>

<script>
export default {
    computed: {
        currentEpisode() {
            return this.$root.data.current_episode;
        }
    }
}
</script>

<style scoped>
</style>