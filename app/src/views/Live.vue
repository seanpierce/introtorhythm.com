<template>
    <div id="live" class="content clearfix">

        <img id="logo" 
            class="flip"
            :src="require('@/assets/images/itr-logo.png')" alt="Intro To Rhythm logo" />

        <div class="background-container"
            :style="{ backgroundImage: 'url(' + bgImage + ')' }">
        </div>

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
        
        <div class="marquee-wrapper">
            <Marquee />
        </div>
    </div>
</template>

<script>
import CircleType from 'circletype'
import Spinner from '@/components/Animations/Spinner'
import Marquee from '@/components/Marquee'

export default {

    components: {
        Spinner,
        Marquee
    },

    data() {
        return {
            playButton: require('@/assets/images/play-circle.png'),
            pauseButton: require('@/assets/images/pause-circle.png'),
            liveUrl: 'https://introtorhythm.com/stream',
            mediaUrl: process.env.VUE_APP_MEDIA_URL,
            defaultBg: require('@/assets/images/seanpierce-palabra.jpg')
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
        },

        bgImage() {
            return this.$store.state.content.bgImage?.active ?
                this.mediaUrl + this.$store.state.content.bgImage.image :
                this.defaultBg
        }
    },

    mounted() {
        new CircleType(document.getElementById('circle'))
    }
}
</script>