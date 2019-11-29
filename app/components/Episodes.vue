<template>
    <div id="episodes">
        <div class="content">
            <div class="cover-filter"></div>
            <div v-if="latestEpisode"
                id="latest-episode"
                :style="{ backgroundImage: 'url(' + $root.mediaUrl + latestEpisode.image + ')' }">
                <div class="show-info">
                    <div class="title">{{ latestEpisode.number }}- {{ latestEpisode.title }}</div>
                    <div class="show-time">{{ $root.localTime }}</div>
                </div>
                <div class="play-button" @click="play()">
                    <img :src="playing ? '/assets/images/pause.png' : '/assets/images/play.png'" alt="">
                </div>
            </div>
        </div>
        <div class="sub-content">
            <div v-if="episodes" class="section">
                <h1>Episodes</h1>
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

export default {
    components: {
        EpisodesGrid
    },
    data() {
        return {
            episodes: null,
            latestEpisode: null
        }
    },
    methods: {
        getEpisodes() {
            axios.get('/api/episodes')
                .then(response => {
                    this.latestEpisode = response.data.shift();
                    this.episodes = response.data;
                    this.setAudioSrouce();
                })
        },
        play() {
            this.$parent.play();
        },
        setAudioSrouce() {
            var audioSource = this.$root.mediaUrl + this.latestEpisode.audio;
            this.$parent.audio.src = audioSource;
        }
    },
    computed: {
        playing() {
            return this.$parent.playing;
        }
    },
    mounted() {
        this.getEpisodes();
    }
}
</script>