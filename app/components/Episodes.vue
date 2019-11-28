<template>
    <div id="episodes" class="content">
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
</template>

<script>
import axios from 'axios';

export default {
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
                    this.episodes = response.data;
                    this.latestEpisode = this.episodes[0];
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