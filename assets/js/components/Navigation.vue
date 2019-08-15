<template>
    <div>
        <div id="nav" v-if="loaded">
            <ul>
                <li><a href="/">Intro To Rhythm</a><li>
                <li>------</li>
                <li>Now Playing: Ep {{ currentEpisode.number }}</li>
                <li id="tracktime">00:00:00 / 00:00:00</li>
                <li>
                    <span class="see-info pointer">
                        See Ep {{ currentEpisode.number }} Info &lt;
                    </span>
                </li>
                <li>------</li>
                <li 
                    v-for="episode in episodes" 
                    v-bind:key="episode.number">
                    <a :href="'/' + episode.number" v-bind:class="{ active: episode.number === currentEpisode.number }">
                        {{ episode.number }}- {{ episode.title }}
                    </a>
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