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
                <div id="tags">
                    <span v-for="(tag, index) in episode.tags" :key="index">
                        <span class="tag" @click="searchTag(tag)">#{{ tag }}</span>
                    </span>
                </div>
            </div>
        </div>
        <SearchModal v-if="modal === 'search-tags'"
            :tag-search="true"
            :modal-data="modalData" />
    </div>
</template>

<script>
import axios from 'axios';
import AudioTimeline from './partials/AudioTimeline';
import SearchModal from './partials/modals/SearchModal';

export default {
    components: {
        AudioTimeline,
        SearchModal
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
            modal: null,
            modalData: null
        }
    },
    methods: {
        getEpisode() {
            var number = window.location.pathname.replace('/episodes/', '');
            var url = '/api/episodes/' + number;
            axios.get(url)
                .then(response => {
                    this.episode = response.data;
                    this.episode.tags = this.getEpisodeTags(this.episode.tags);
                    this.setAudioSrouce();
                })
        },
        getEpisodeTags(tags) {
            if (tags && tags !== '')
                return tags.split(',').map(x => this.formatTag(x));
            else return []
        },
        formatTag(tag) {
            if (tag[0] === ' ')
                tag = tag.slice(1);

            if (tag[tag.length -1] === ' ')
                tag = tag.slice(0, -1);

            return tag;
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
        searchTag(tag) {
            tag = this.formatTag(tag);
            axios.post('/api/episodes/search/tag', { tag: tag })
                .then(response => {
                    this.modalData = {
                        data: response.data,
                        tag: tag
                    }
                    this.showModal('search-tags');
                })
        },
        showModal(name) {
            this.modal = name;
            document.body.style.overflow = 'hidden';
        },
        hideModal() {;
            this.modal = null;
            document.body.style.overflow = 'inherit';
        },
    },
    computed: {
    },
    mounted() {
        this.getEpisode();
    }
}
</script>