<template>
    <div id="live">
        <div id="live-text">You are listening to ITR, Live</div>
        <div id="live-player" @click="togglePlay()">
            <span id="arrow-span">⤷ </span>
            <span v-if="!playing">Play</span>
            <span v-if="playing">Pause</span>
            <span id="seconds">{{ seconds }}</span>
        </div>
        <div id="logo-spinner">
            <img :src="$root.staticUrl + '/images/itr-logo.png'">
        </div>
        <img id="twisterman" :src="$root.staticUrl + '/images/twisterman-red.png'" />
        <div id="links">
            <a href="/">ITR</a>
            <span class="pointer"
                @click="showAboutModal = true">
                <u>Info</u>
            </span>
            <span class="pointer"
                @click="showSubscribeModal = true">
                <u>Subscribe</u>
            </span>
            <span class="pointer"
                @click="showEpisodesModal = true">
                <u>Episodes</u>
            </span>
        </div>
        <Modal v-if="showAboutModal" type="about"/>
        <Modal v-if="showEpisodesModal" type="episodes"/>
        <Modal v-if="showSubscribeModal" type="subscribe"/>
    </div>
</template>

<script>
import Modal from './partials/modals/Modal.vue';

export default {
    components: {
        Modal
    },
    data() {
        return {
            liveUrl: 'https://introtorhythm.com/stream',
            audio: null,
            playing: false,
            seconds: 0,
            showAboutModal: false,
            showEpisodesModal: false,
            showSubscribeModal: false
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
        timeUpdate() {
            this.seconds = parseInt(this.audio.currentTime, 10);
        },
        onError(vm) {
            console.log('audio error')
            vm.audio.remove();
            vm.audio = new Audio();
            vm.audio.src = vm.liveUrl;
            vm.audio.preload = 'metadata';
            vm.audio.addEventListener('timeupdate', vm.timeUpdate);
            vm.audio.play();
            vm.audio.onerror = function() {
                vm.onError(vm);
            }
        }
    },
    mounted() {
        var vm = this;
        this.audio = new Audio();
        this.audio.src = this.liveUrl;
        this.audio.preload = 'metadata';
        this.audio.addEventListener('timeupdate', this.timeUpdate);

        this.audio.onerror = function() {
            vm.onError(vm);
        }
    }
}
</script>