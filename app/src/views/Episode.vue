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

        <Timeline v-if="active" />

        <div class="episode-content__wraper">
            <div id="episode-time">
                03:43:01
            </div>
            <div class="episode-content__inner-wraper">
                <h1>{{ episode.number }}</h1>
                <h2>{{ episode.title }}</h2>
                <div class="selected-episode-content__content" v-html="episode.content"></div>
                <div class="selected-episode-content__tags">
                    <span v-for="(tag, index) in getEpisodeTags(episode.tags)" 
                        :key="index">
                        <router-link :to="'/episodes?tag=' + encode(tag)">#{{ tag }}</router-link>
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Spinner from '@/components/Animations/Spinner'
import Timeline from '@/components/Timeline'

export default {

    components: {
        Spinner,
        Timeline
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

        getEpisodeTags(tags) {
            tags = tags.split(',').map(x => this.formatTag(x));
            return tags.sort((a, b) => {
                if (a < b) return -1;
                if (a > b) return 1;
                return 0;
            })
        },

        formatTag(tag) {
            if (tag[0] === ' ')
                tag = tag.slice(1);
            if (tag[tag.length -1] === ' ')
                tag = tag.slice(0, -1);
            return tag;
        },

        encode(input) {
            return encodeURIComponent(input)
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
            return this.$store.state.episodes.playing && this.active
        },

        active() {
            return this.$store.state.episodes.nowPlaying?.number == this.episode.number
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