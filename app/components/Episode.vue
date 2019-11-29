<template>
    <div id="episodes" class="content">
        <div class="cover-filter"></div>
        <div v-if="episode"
            id="episode"
            :style="{ backgroundImage: 'url(' + $root.mediaUrl + episode.image + ')' }">
            <div class="show-info">
                <div class="title">{{ episode.number }}- {{ episode.title }}</div>
                <div class="show-time">00:00:00 / 00:00:00</div>
            </div>
            <div class="play-button" @click="play()">
                <img :src="playing ? '/assets/images/pause.png' : '/assets/images/play.png'" alt="">
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
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