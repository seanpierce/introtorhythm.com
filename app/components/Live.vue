<template>
    <div>
        <div id="live" class="content">
            <div class="cover-filter"></div>
            <div class="show-info">
                <div class="title">Listen Live</div>
                <div class="show-time">{{ $root.localTime }}</div>
            </div>
            <div class="play-button" @click="play()">
                <img :src="playing ? '/assets/images/icons/pause.png' : '/assets/images/icons/play.png'" alt="">
            </div>
            <img src="/assets/images/itr-logo.png" class="logo" alt="">
            <div id="scroll-down-cta"
                @click="scrollToRecent()">
                ⤺ Latest & Featured
            </div>
        </div>
        <div id="recent-episodes-container" class="sub-content">
            <div class="sub-header">Latest Episodes</div>
            <div v-if="latestEpisodes">
                <EpisodeGrid :episodes="latestEpisodes" :paginate="6" />
            </div>
            <div class="sub-header">Featured Episodes</div>
            <div v-if="featuredEpisodes">
                <EpisodeGrid :episodes="featuredEpisodes" />
            </div>
            <div class="show-more-button"><span @click="goToEpisodes()">See more episodes</span></div>
            <div>
                <img src="/assets/images/itr-text.png" class="itr-text">
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import EpisodeGrid from './partials/EpisodeGrid';

export default {
    components: {
        EpisodeGrid
    },
    data() {
        return {
            latestEpisodes: null,
            featuredEpisodes: null
        }
    },
    methods: {
        goToEpisodes() {
            window.location.href="/episodes"
        },
        play() {
            this.$parent.play();
        },
        getLatestEpisodes() {
            axios.get('/api/episodes/recent')
                .then(response => {
                    this.latestEpisodes = response.data;
                })
        },
        getFeaturedEpisodes() {
            axios.get('/api/episodes/featured')
                .then(response => {
                    this.featuredEpisodes = response.data;
                })
        },
        scrollToRecent() {
            var element = document.getElementById('recent-episodes-container');
            element.scrollIntoView({behavior: 'smooth'});
        }
    },
    computed: {
        playing() {
            return this.$parent.playing;
        }
    },
    mounted() {
        this.getLatestEpisodes();
        this.getFeaturedEpisodes();
    }
}
</script>