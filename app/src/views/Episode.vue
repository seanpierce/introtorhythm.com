<template>
    <div id="episode" class="content" v-if="episode">

        <div class="episode__wrapper">
            <div class="episode__background-container" 
                :style="{ backgroundImage: 'url(' + mediaUrl + episode.image + ')' }">
            </div>

            <img v-if="!loading"
                id="play-button"
                :src="playing ? pauseButton : playButton" 
                @click="toggleEpisode()"
                alt="Intro To Rhythm Live play button">

            <Spinner v-if="loading" />

            <div class="title">
                {{ episode.number }}- {{ episode.title }}
            </div>

        </div>

        <div class="episode-content__wraper">
            <div class="episode-content__inner-wraper">
                <h1>{{ episode.number }}</h1>
                <h2>{{ episode.title }}</h2>
                <div class="selected-episode-content__content" v-html="episode.content"></div>
            </div>
        </div>
    </div>
</template>

<script>
import Spinner from '@/components/Animations/Spinner'

export default {

    components: {
        Spinner
    },

    props: {
        number: String
    },

    data() {
        return {
            mediaUrl: process.env.VUE_APP_MEDIA_URL,
            playButton: require('@/assets/images/play-circle.png'),
            pauseButton: require('@/assets/images/pause-circle.png')
        }
    },

    methods: {

        toggleEpisode() {
            this.$store.dispatch('toggleEpisodePlaying', this.episode)
        },
    },


    watch: {

        playing() {
            if (this.playing) {
                if (this.audio) {
                    this.$store.dispatch('playEpisodeAudio')
                } else {
                    this.$store.dispatch('setEpisodeAudio', this.mediaUrl + this.episode.audio)
                        .then(() => {
                            this.$store.dispatch('playEpisodeAudio')
                        })
                }
            } else {
                this.$store.dispatch('pauseEpisodeAudio')
            }
        }

    },

    computed: {

        episode() {
            let episode = this.$store.state.episodes.episodes
                .find(x => x.number === this.number)

            if (episode)
                this.$store.dispatch('setSelectedEpisode', episode)

            return episode
        },

        playing() {
            return this.$store.state.episodes.playing && 
                (this.$store.state.episodes.nowPlaying?.number == this.episode.number)
        },

        audio() {
            return this.$store.state.episodes.audio
        },

        loading() {
           return this.$store.state.episodes.loading 
        }
    },
}
</script>