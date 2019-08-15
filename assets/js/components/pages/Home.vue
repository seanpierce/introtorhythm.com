<template>
    <div id="home">
        <Navigation />
    </div>
</template>

<script>
import Navigation from "../partials/Navigation.vue";

export default {
    components: {
        Navigation
    },
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