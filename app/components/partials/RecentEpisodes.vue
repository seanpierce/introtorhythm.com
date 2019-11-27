<template>
    <div id="recent-episodes">
        <h3>Recent Episodes</h3>
        <div v-if="recentEpisodes" id="recent-episodes-list">
            <EpisodeGrid :episodes="recentEpisodes" />
        </div>
        <div id="all-episodes-button">
            <a href="/episodes">See all episodes</a>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import EpisodeGrid from './EpisodeGrid.vue';

export default {
    components: {
        EpisodeGrid
    },
    data() {
        return {
            recentEpisodes: null
        }
    },
    methods: {
        getRecentEpisodes() {
            axios.get('/api/episodes/recent')
                .then(response => {
                    this.recentEpisodes = response.data;
                })
        }
    },
    mounted() {
        this.getRecentEpisodes();
    }
}
</script>