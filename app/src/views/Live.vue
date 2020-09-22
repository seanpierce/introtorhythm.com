<template>
    <div id="live" class="content clearfix">

        <img id="logo" 
            class="flip"
            :src="require('@/assets/images/itr-logo.png')" alt="Intro To Rhythm logo" />

        <div class="background-container"></div>

        <div id="live-wrapper">
            <div id="circle" 
                class="spin">Listen to Intro To Rhythm Live - Streaming 24 hours a day - Always online - 
            </div>
        </div>

        <img v-if="!loading"
            id="play-button"
            :src="playing ? pauseButton : playButton" 
            @click="toggleLive()"
            alt="Intro To Rhythm Live play button">

        <Spinner v-if="loading" />

        <div class="title">
            Live
        </div>

        <!-- <Footer :position="'absolute'"/> -->
    </div>
</template>

<script>
import CircleType from 'circletype'
import Spinner from '@/components/Animations/Spinner'
// import Footer from '@/components/Footer'

export default {

    components: {
        Spinner,
        // Footer
    },

    data() {
        return {
            playButton: require('@/assets/images/play-circle.png'),
            pauseButton: require('@/assets/images/pause-circle.png'),
            liveUrl: 'https://introtorhythm.com/stream'
        }

    },

    methods: {

        toggleLive() {
            this.$store.dispatch('toggleLive')
        },
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

    mounted() {
        new CircleType(document.getElementById('circle'))
    }
}
</script>