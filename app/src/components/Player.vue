<template>
    <div id="player" 
        v-if="nowPlaying && !onNowPlaying"
        @click="goToNowPlaying()">
        <div class="player__image" :style="{ backgroundImage: 'url(' + image + ')' }"></div>
        <div class="player__title_wrapper">
            <span class="player__title">Now Playing - {{ nowPlaying }}</span>
            <AudioPlaying />
        </div>
    </div>
</template>

<script>
import AudioPlaying from '@/components/Animations/AudioPlaying'

export default {

    components: {
        AudioPlaying
    },

    data() {
        return {
            mediaUrl: process.env.VUE_APP_MEDIA_URL
        }
    },

    computed: {

        nowPlaying() {
            if (this.$store.state.live.playing)
                return 'ITR Live'

            if (this.$store.state.episodes.playing)
                return 'Ep ' + this.$store.state.episodes.nowPlaying.number

            return null
        },

        onNowPlaying() {
            if (this.$store.state.live.playing
                && this.$route.name === 'Live')
                return true

            if (this.$store.state.episodes.playing
                && this.$route.params?.number === this.$store.state.episodes.nowPlaying.number)
                return true

            return false
        },

        image() {
            if (this.nowPlaying === 'ITR Live')
                return require('@/assets/images/seanpierce-palabra.jpg')
            
            if (this.nowPlaying !== null && !(this.nowPlaying === 'ITR Live'))
                return this.mediaUrl + this.$store.state.episodes.nowPlaying.image

            return null
        }
    },

    methods: {

        goToNowPlaying() {
            if (this.$store.state.live.playing
                && this.$route.name !== 'Live')
                return this.$router.push('/')

            if (this.$store.state.episodes.playing
                && this.$route.params?.number !== this.$store.state.episodes.nowPlaying.number)
                return this.$router.push(`/episodes/${this.$store.state.episodes.nowPlaying.number}`)

        }
    }
}
</script>