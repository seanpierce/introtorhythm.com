<template>
    <div id="live" class="content">

        <div class="background-container"></div>

        <div id="live-wrapper">
            <div id="circle" 
                class="spin">Listen to Intro To Rhythm Live - Streaming 24 hours a day - Always online - 
            </div>
        </div>

        <img v-if="!audioLoading"
            id="play-button"
            :src="playing ? pauseButton : playButton" 
            @click="toggleLive()"
            alt="Intro To Rhythm Live play button">

        <Spinner v-if="audioLoading" />

        <div class="title">
            Live
        </div>

        <Footer :position="'absolute'"/>
    </div>
</template>

<script>
import CircleType from 'circletype'
import Spinner from '@/components/Shared/Spinner'
import Footer from '@/components/Footer'

export default {

    components: {
        Spinner,
        Footer
    },

    data() {
        return {
            playButton: require('@/assets/images/play-circle.png'),
            pauseButton: require('@/assets/images/pause-circle.png'),
            audio: null,
            liveUrl: 'https://introtorhythm.com/stream',
            audioLoading: false
        }

    },

    methods: {

        toggleLive() {
            this.$store.dispatch('toggleLive')
        },

        async setAudio() {
            console.log('Setting audio...')
            var vm = this
            this.audioLoading = true

            this.audio?.pause()
            this.audio = new Audio()
            this.audio.src = this.liveUrl
            this.audio.preload = 'metadata'

            // indicates when the audio file is ready to be played
            this.audio.addEventListener('loadeddata', function() {
                if (this.readyState >= 2)
                    vm.audioLoading = false
                    // vm.audio.play()
            })

            // reset audio on error
            this.audio.addEventListener('error', function() { 
                console.log('audio error', new Date())
                vm.setAudio()
                    .then(() => {
                        vm.toggleLive()
                    })
            })

            return
        }
    },

    watch: {

        playing() {
            if (this.playing) {
                this.setAudio()
                    .then(() => {
                        this.audio.play()
                    })
            } else {
                this.audio.pause()
                this.audio = null
            }
        }

    },

    computed: {

        playing() {
            return this.$store.state.live.playing
        }
    },

    mounted() {
        new CircleType(document.getElementById('circle'))
    }
}
</script>