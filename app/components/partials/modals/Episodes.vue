<template>
    <div id="episodes-list" class="content">
        <div v-for="episode in episodes"
            :key="episode.number"
            class="episode-list-item">
            <a :href="'/' + episode.number">{{ episode.number }}- {{ episode.title }}</a>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            episodes: [],
            imagesLoaded: false
        }
    },
    methods: {
        getEpisodes() {
            axios.get('api/episodes/')
                .then(response => {
                    this.episodes = response.data.data.episodes;
                })
        },
        goTo(number) {
            window.location.href="/" + number;
        },
    },
    mounted() {
        this.getEpisodes();
    }
}
</script>