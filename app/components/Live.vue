<template>
    <div>
        <div id="live" 
            class="content"
            :style="{ backgroundImage: 'url(' + backgroundImage + ')' }">
            <div class="cover-filter"></div>
            <div class="show-info">
                <div class="title">Listen Live</div>
                <div class="show-time">{{ $root.localTime }}</div>
                <div class="call-in">CALL (503) 877-9051‬</div>
            </div>
            <div class="play-button" @click="play()">
                <img :src="playing ? '/assets/images/icons/pause.png' : '/assets/images/icons/play.png'" alt="">
            </div>
            <img src="/assets/images/itr-logo.png" class="logo" alt="">
            <div id="donations-cta" v-if="liveCallout && liveCallout.active">
                <span id="down-arrow">&darr;</span>
                <div v-html="liveCallout.info"></div>
            </div>
            <div id="scroll-down-cta"
                @click="scrollToRecent()">
                ⤺ Latest & Featured
            </div>
        </div>
        <div id="recent-episodes-container" class="sub-content">
            <div class="sub-header">Latest Episodes</div>
            <div v-if="latestEpisodes">
                <EpisodeGrid :episodes="latestEpisodes" />
            </div>
            <div class="sub-header">Featured Episodes</div>
            <div v-if="featuredEpisodes">
                <EpisodeGrid :episodes="featuredEpisodes" />
            </div>
            <div class="show-more-button"><span @click="goToEpisodes()">More Episodes</span></div> 
            <Footer />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import EpisodeGrid from './partials/episode-grid/EpisodeGrid';
import Footer from './partials/Footer';

export default {
    components: {
        EpisodeGrid,
        Footer
    },
    data() {
        return {
            latestEpisodes: null,
            featuredEpisodes: null,
            liveCallout: null,
            liveBackgroundImage: null
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
        },
        getLiveCallout() {
            axios.get('/api/content/live%20callout')
                .then(response => {
                    this.liveCallout = response.data;
                })
        },
        getLiveBackgroundImage() {
            axios.get('/api/content/backgroundimage')
                .then(response => {
                    this.liveBackgroundImage = response.data.image;
                })
        }
    },
    computed: {
        playing() {
            return this.$parent.playing;
        },
        backgroundImage() {
            if (this.liveBackgroundImage)
                return this.$root.mediaUrl + this.liveBackgroundImage;
            else return '/assets/images/palabra.png';
        }
    },
    mounted() {
        this.getLatestEpisodes();
        this.getFeaturedEpisodes();
        this.getLiveCallout();
        this.getLiveBackgroundImage();
    }
}
</script>