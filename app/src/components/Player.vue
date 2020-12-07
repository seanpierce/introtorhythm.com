<template>
    <div id="player" 
        v-if="playing && !onNowPlaying"
        @click="goToNowPlaying()">
        <div class="player__image" 
            :style="{ backgroundImage: 'url(' + image + ')' }"></div>
        <div class="player__title_wrapper">
            <span class="player__content">
                <span class="player__title">Now Playing - {{ nowPlaying }}</span>
            </span>
        </div>
    </div>
</template>

<script>
export default {

    components: {
    },

    data() {
        return {
            mediaUrl: process.env.VUE_APP_MEDIA_URL,
            playButton: require('@/assets/images/play-circle-dark.png'),
            pauseButton: require('@/assets/images/pause-circle-dark.png')
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

        audioWasSelected() {
            return this.$store.state.live.audio
                || this.$store.state.episodes.audio
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
            if (this.isLive)
                return this.liveBgImage
            
            if (this.nowPlaying !== null && !this.isLive)
                return this.mediaUrl + this.$store.state.episodes.nowPlaying.image

            return null
        },

        playing() {
            if (this.isLive)
                return this.$store.state.live.playing
            
            if (this.nowPlaying !== null && !this.isLive)
                return this.$store.state.episodes.playing

            return false
        },

        liveBgImage() {
            return this.$store.state.content.bgImage?.active ?
                this.mediaUrl + this.$store.state.content.bgImage.image :
                require('@/assets/images/seanpierce-palabra.jpg')
        },

        isLive() {
            return this.nowPlaying === 'ITR Live'
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

        },

        togglePlay() {
            if (this.isLive) {
                this.$store.dispatch('toggleLive')
            } else {
                this.$store.dispatch('toggleEpisodePlaying', this.$store.state.episodes.nowPlaying.number)
            }
        }
    }
}
</script>