<template>
    <div id="episode-info">
        <div id="episode-heading">{{ currentEpisode.number }}- {{ currentEpisode.title }}</div>
        <div v-html="currentEpisode.content"></div>
        <div>
            ------------<br>
            <br>
            Share this episode on:<br>
            facebook / twitter<br>
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
#episode-heading {
    margin-top: 1em;
}
</style>