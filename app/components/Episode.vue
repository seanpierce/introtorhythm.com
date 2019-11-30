<template>
    <div id="episodes" class="content">
        <div class="cover-filter"></div>
        <div v-if="episode"
            id="current-episode"
            :style="{ backgroundImage: 'url(' + $root.mediaUrl + episode.image + ')' }">
            <div class="show-info">
                <div class="title">{{ episode.number }}- {{ episode.title }}</div>
                <div class="show-time">{{ $root.localTime }}</div>
            </div>
            <div class="play-button" @click="play()">
                <img :src="playing ? '/assets/images/pause.png' : '/assets/images/play.png'" alt="">
            </div>
            <img src="/assets/images/itr-logo.png" class="logo" alt="">
            <AudioTimeline />
        </div>
        <div class="sub-content" v-if="episode">
            <div class="episode-info">
                <h2>{{ episode.number }}</h2>
                <h1>{{ episode.title }}</h1>
                <div v-html="episode.content"></div>
            </div>
            <div>
                <img src="/assets/images/itr-text.png" class="itr-text">
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import AudioTimeline from './partials/AudioTimeline';

export default {
    components: {
        AudioTimeline
    },
    data() {
        return {
            episode: null
        }
    },
    methods: {
        getEpisode() {
            var number = window.location.pathname.replace('/episodes/', '');
            var url = '/api/episodes/' + number;
            axios.get(url)
                .then(response => {
                    this.episode = response.data;
                    this.setAudioSrouce();
                })
        },
        play() {
            this.$parent.play();
        },
        setAudioSrouce() {
            var audioSource = this.$root.mediaUrl + this.episode.audio;
            this.$parent.audio.src = audioSource;
        }
    },
    computed: {
        playing() {
            return this.$parent.playing;
        }
    },
    mounted() {
        this.getEpisode();
    }
}
</script>