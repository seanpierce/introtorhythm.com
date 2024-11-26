<template>
    <div id="volume">
        <img v-if="!muted" :src="volOnIcon" @click="mute()">
        <img v-if="muted" :src="volMuteIcon" @click="unMute()">
        <input id="vol-slider" type="range" min="0" max="100" value="80" i="slider" @input="updateVolume($event)" />
    </div>
</template>

<script>
export default {
    data() {
        return {
            volOnIcon: require('@/assets/images/orange-vol-icon-on.png'),
            volMuteIcon: require('@/assets/images/orange-vol-icon-mute.png'),
            tempVolume: 80
        }
    },

    computed: {
        muted() {
            return Math.round(this.$store.state.live.volume * 100) == 0;
        }
    },

    methods: {
        updateVolume(event) {
            const volume = event.target.value;
            this.tempVolume = volume;
            this.$store.dispatch('setVolume', volume);
        },

        mute() {
            this.$store.dispatch('setVolume', 0);
        },

        unMute() {
            this.$store.dispatch('setVolume', this.tempVolume);
        }
    },
}
</script>