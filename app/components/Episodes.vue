<template>
    <div id="episodes">
        <div class="content">
        <div class="cover-filter"></div>
            <EpisodeSlider v-if="mostRecent" :episodes="mostRecent" />
        </div>
        <div class="sub-content">
            <div v-if="episodes" class="section">
                <EpisodesGrid :episodes="episodes"
                    :paginate="true" />
            </div>
            <Footer />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import EpisodesGrid from './partials/episode-grid/EpisodeGrid.vue';
import EpisodeSlider from './partials/EpisodeSlider.vue';
import Footer from './partials/Footer';

export default {
    components: {
        EpisodesGrid,
        EpisodeSlider,
        Footer
    },
    data() {
        return {
            episodes: null,
            mostRecent: null
        }
    },
    methods: {
        getEpisodes() {
            axios.post('/api/episodes/paginate', { offset: 0, take: 12 })
                .then(response => {
                    this.mostRecent = response.data.slice(0,6);
                    this.episodes = response.data;
                })
        },
    },
    mounted() {
        this.getEpisodes();
    }
}
</script>