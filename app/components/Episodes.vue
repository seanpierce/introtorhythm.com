<template>
    <div id="episodes">
        <div class="content">
        <div class="cover-filter"></div>
            <EpisodeSlider v-if="mostRecent" :episodes="mostRecent" />
        </div>
        <div class="sub-content">
            <div v-if="episodes" class="section">
                <EpisodesGrid :episodes="episodes"
                    :paginate="12" />
            </div>
            <div>
                <img src="/assets/images/itr-text.png" class="itr-text">
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import EpisodesGrid from './partials/EpisodeGrid.vue';
import EpisodeSlider from './partials/EpisodeSlider.vue';

export default {
    components: {
        EpisodesGrid,
        EpisodeSlider
    },
    data() {
        return {
            episodes: null,
            mostRecent: null
        }
    },
    methods: {
        getEpisodes() {
            axios.get('/api/episodes')
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