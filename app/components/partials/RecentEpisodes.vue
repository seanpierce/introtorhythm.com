<template>
    <div id="recent-episodes">
        <h3>Recent Episodes</h3>
        <div v-if="recentEpisodes" id="recent-episodes-list">
            <div v-for="episode in recentEpisodes"
                :key="episode.id"
                class="recent-episode-container">
                <div class="recent-episode-wrapper">
                    <div class="recent-episode"
                        :style="{ backgroundImage: 'url(' + $root.mediaUrl + episode.image + ')' }">
                        <div class="recent-episode-content">
                            <div>{{ episode.number }}<br>{{ episode.title }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
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