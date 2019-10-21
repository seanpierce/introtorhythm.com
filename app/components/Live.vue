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
        <!-- <audio :src="liveUrl" controls></audio> -->
    </div>
</template>

<script>
export default {
    data() {
        return {
            liveUrl: 'https://introtorhythm.com/stream',
            audio: null,
            playing: false,
            seconds: 0
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
        }
    },
    mounted() {
        this.audio = new Audio();
        this.audio.src = this.liveUrl;
        this.audio.addEventListener('timeupdate', this.timeUpdate);
    }
}
</script>