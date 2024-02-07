<template>
    <div>
        <img v-if="!loading"
            id="play-button"
            :src="playing ? pauseButton : playButton" 
            @click="toggleLive()"
            alt="Intro To Rhythm Live play button">

        <Spinner v-if="loading" />
    </div>
</template>

<script>
import Spinner from '@/components/Animations/Spinner'

export default {
    components: {
        Spinner
    },

    data() {
        return {
            playButton: require('@/assets/images/play-circle-orange.png'),
            pauseButton: require('@/assets/images/pause-circle-orange.png'),
            liveUrl: 'https://introtorhythm.com/stream'
        }
    },

    methods: {
        toggleLive() {
            this.$store.dispatch('toggleLive')
        },
    },

    computed: {
        playing() {
            return this.$store.state.live.playing
        },

        audio() {
            return this.$store.state.live.audio
        },

        loading() {
            return this.$store.state.live.loading
        }
    },

    watch: {
        playing() {
            if (this.playing) {
                this.$store.dispatch('setLiveAudio', this.liveUrl)
                    .then(() => {
                        this.$store.dispatch('playLiveAudio')
                    })
            } else {
                this.$store.dispatch('stopLiveAudio')
            }
        }
    }
}
</script>