<template>
    <div id="archive">
        <h1 class="pointer" @click="goHome()">ITR/</h1>
        <h2 class="tab-1">Archive/</h2>
        <ul v-if="episodes" class="tab-2">
            <li v-for="episode in episodes" :key="episode.id">
                <a :href="'/episode/' + episode.number">{{ episode.number }}- {{ episode.title }}</a>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            episodes: null
        }
    },
    methods: {
        getEpisodes() {
            axios.get('/api/episodes')
                .then(response => { 
                    this.episodes = response.data;
                })
        },
        goHome() {
            window.location.href="/";
        }
    },
    mounted() {
        this.getEpisodes();
    }
}
</script>