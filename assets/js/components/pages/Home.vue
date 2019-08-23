<template>
    <div id='home' v-if="loaded">
        <Navigation />
        <div id='filter-overlay'></div>
        <div id='episode-image'
            v-bind:style="{backgroundImage:'url('+getBackgroundUrl()+')'}"></div>
    </div>
</template>

<script>
import Navigation from '../partials/Navigation.vue';

export default {
    components: {
        Navigation
    },
    data() {
        return {
        }
    },
    methods: {
        getBackgroundUrl() {
            return this.$root.mediaUrl + this.currentEpisode.image
        }
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