<template>
    <div id="episode" class="content" v-if="episode">
        <div class="background-container" 
            :style="{ backgroundImage: 'url(' + mediaUrl + episode.image + ')' }">
        </div>

        <img v-if="!audioLoading"
            id="play-button"
            :src="playing ? pauseButton : playButton" 
            @click="toggleEpisode()"
            alt="Intro To Rhythm Live play button">

        <Spinner v-if="audioLoading" />

        <div class="title">
            {{ episode.number }}- {{ episode.title }}
        </div>
        
        <div class="episode-content__wraper">

            <div class="episode-content__inner-wraper">
                <h1>{{ episode.number }}</h1>
                <h2>{{ episode.title }}</h2>

                <div class="selected-episode-content__content" v-html="episode.content"></div>
            </div>
            <Footer position="absolute"/>
        </div>

    </div>
</template>

<script>
import Footer from '@/components/Footer'
import Spinner from '@/components/Shared/Spinner'

export default {

    components: {
        Footer,
        Spinner
    },

    props: {
        number: String
    },

    data() {
        return {
            mediaUrl: process.env.VUE_APP_MEDIA_URL,
            playButton: require('@/assets/images/play-circle.png'),
            pauseButton: require('@/assets/images/pause-circle.png'),
            audio: null,
            audioLoading: false
        }
    },

    methods: {

        toggleEpisode() {
            this.$store.dispatch('toggleEpisodePlaying')
        },

        setSelectedEpisode() {
            this.$store.dispatch('setSelectedEpisode', this.number)
        },

        async setAudio() {
            console.log('Setting audio...')

            if (this.audio) {
                this.audio.play()
                return
            }

            var vm = this
            this.audioLoading = true

            this.audio?.pause()
            this.audio = new Audio()
            this.audio.src = this.mediaUrl + this.episode.audio
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
                        vm.toggleEpisode()
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
            }
        }

    },

    computed: {

        episode() {
            let episode = this.$store.state.episodes.episodes.find(x => x.number === this.number)
            if (episode)
                this.$store.dispatch('setSelectedEpisode', episode)

            return episode
        },

        playing() {
            return this.$store.state.episodes.playing
        }
    },
}
</script>