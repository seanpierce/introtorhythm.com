<template>
    <div>
        <div id="live" class="content">
            <div class="cover-filter"></div>
            <div class="show-info">
                <div class="title">Listen Live</div>
                <div class="show-time">{{ $root.localTime }}</div>
            </div>
            <div class="play-button" @click="play()">
                <img :src="playing ? '/assets/images/pause.png' : '/assets/images/play.png'" alt="">
            </div>
            <img src="/assets/images/itr-logo.png" class="logo" alt="">
        </div>
        <div id="recent-episodes-container" class="sub-content">
            <h1 class="skew">Latest Episodes</h1>
            <div class="latest-episodes">
                <EpisodeSlider v-if="latestEpisodes" :episodes="latestEpisodes" />
            </div>
            <div>
                <img src="/assets/images/itr-text.png" class="itr-text">
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import EpisodeSlider from './partials/EpisodeSlider';

export default {
    components: {
        EpisodeSlider
    },
    data() {
        return {
            latestEpisodes: null
        }
    },
    methods: {
        play() {
            this.$parent.play();
        },
        getLatestEpisodes() {
            axios.get('/api/episodes/recent')
                .then(response => {
                    this.latestEpisodes = response.data;
                })
        }
    },
    computed: {
        playing() {
            return this.$parent.playing;
        }
    },
    mounted() {
        this.getLatestEpisodes();
    }
}
</script>