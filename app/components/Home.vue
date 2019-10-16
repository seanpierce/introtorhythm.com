<template>
    <div id="home" v-if="$root.loaded">
        <Navigation />
        <BackgroundImage />
        <Modal v-if="showEpisodeInfoModal" type="episodeInfo"/>
        <Modal v-if="showAboutModal" type="about"/>
        <Modal v-if="showEpisodesModal" type="episodes"/>
        <Modal v-if="showSubscribeModal" type="subscribe"/>
        <Player />
        <Ticker />
    </div>
</template>

<script>
import Navigation from './partials/Navigation.vue';
import BackgroundImage from './partials/BackgroundImage.vue';
import Modal from './partials/modals/Modal.vue';
import Player from './partials/Player.vue';
import Success from './partials/modals/SubscriptionConfirmation/Success.vue';
import Failure from './partials/modals/SubscriptionConfirmation/Failure.vue';
import Ticker from './partials/Ticker.vue';

export default {
    components: {
        Navigation,
        BackgroundImage,
        Modal,
        Player,
        Success,
        Failure,
        Ticker
    },
    data() {
        return {
            playing: false,
            audio: new Audio(),
            showEpisodeInfoModal: false,
            showAboutModal: false,
            showEpisodesModal: false,
            showSubscribeModal: false,
            currentTime: '00:00:00',
            totalTime: null,
            playPercent: 0,
            playerWidth: 0,
            onplayHead: false,
            showConfirmationSuccess: false,
            showConfirmationFailure: false,
            showPlayButton: true,
            showPlayer: true,
        }
    },
    methods: {
        togglePlay() {
            if (this.audio.paused) {
                this.playing = true;
                this.audio.play();
            } else {
                this.playing = false;
                this.audio.pause();
            }
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
        scrubConfirmationUrl() {
            window.history.replaceState({}, document.title, '/');
        },
        checkForConfirmationUrl() {
            var url = new URL(window.location.href);
            var param = url.searchParams.get("success");
            if (param) {
                if (param === 'true') this.showConfirmationSuccess = true;
                else this.showConfirmationFailure = true;
                this.scrubConfirmationUrl();
            }
        },
    },
    computed: {
        currentEpisode() {
            return this.$root.data;
        },
    },
    mounted() {
        this.checkForConfirmationUrl();
        this.audio.src = this.$root.mediaUrl + this.currentEpisode.audio;
        this.audio.addEventListener('timeupdate', this.timeUpdate);
    },
}
</script>