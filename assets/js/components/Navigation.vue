<template>
    <div>
        <div id="nav" v-if="loaded">
            <ul>
                <li 
                    v-for="episode in episodes" 
                    v-bind:key="episode.number">
                    <a :href="'/' + episode.number">{{ episode.number }}- {{ episode.title }}</a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
module.exports = {
    data() {
        return {
        }
    },
    methods: {
    },
    computed: {
        episodes() {
            return this.$root.data.episodes;
        },
        currentEpisode() {
            return this.$root.data.current_episode;
        },
        loaded() {
            return this.$root.loaded;
        }
    },
    mounted() {
    }
}
</script>

<style>
</style>