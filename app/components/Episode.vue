<template>
    <div id="episodes" class="content">
        <div class="cover-filter"></div>
        <div v-if="episode"
            id="current-episode"
            :style="{ backgroundImage: 'url(' + $root.mediaUrl + episode.image + ')' }">
            <div class="show-info">
                <div class="title">{{ episode.number }}- {{ episode.title }}</div>
                <div class="show-time">{{ currentTime || '00:00:00' }} / {{ totalTime || '00:00:00' }}</div>
            </div>
            <div class="play-button" @click="play()">
                <img :src="playing ? '/assets/images/icons/pause.png' : '/assets/images/icons/play.png'" alt="">
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
            episode: null,
            time: 0,
            playing: false,
            audio: null,
            currentTime: null,
            totalTime: null,
            playPercent: 0,
            playerWidth: 0,
            onplayHead: false,
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
            if (this.audio.paused) {
                this.playing = true;
                this.audio.play();
            } else {
                this.playing = false;
                this.audio.pause();
            }
        },
        setAudioSrouce() {
            var audioSource = this.$root.mediaUrl + this.episode.audio;
            this.audio = new Audio();
            this.audio.src = audioSource;
            this.audio.addEventListener('timeupdate', this.timeUpdate);
        },
        formatTime(input) {
            var sec_num = parseInt(input, 10);
            var hours   = Math.floor(sec_num / 3600);
            var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
            var seconds = sec_num - (hours * 3600) - (minutes * 60);
            if (hours   < 10) { hours   = "0" + hours; }
            if (minutes < 10) { minutes = "0" + minutes; }
            if (seconds < 10) { seconds = "0" + seconds; }
            return hours + ':' + minutes + ':' + seconds;
        },
        timeUpdate() {
            if (!this.totalTime)
                this.totalTime = this.formatTime(this.audio.duration);

            this.currentTime = this.formatTime(this.audio.currentTime);
            if (!this.onplayHead)
                this.playPercent = this.playerWidth * (this.audio.currentTime / this.audio.duration);
        },
    },
    computed: {
    },
    mounted() {
        this.getEpisode();
    }
}
</script>