<template>
    <div class="episode-wrapper" v-bind:class="{ 'show': inView }">
        <div class="episode-inner-wrapper">
            <div class="episode"
                @click="goToEpisode(episode)">
                <FuzzyImage :thumbnail="getThumbnail(episode.image)" :image="episode.image" />
                <svg class="play-button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600"><title>Play</title><g id="_x33_--Hidden-_x28_closing-up_x29_-" transform="translate(-772 -385)"><g id="Drawer" transform="translate(0 43)"><g id="_x32_" transform="translate(18)"><path id="play" d="M1260.4 651.3L882.8 861.2c-4.4 2.4-8.2 2.7-11.2 1-3.1-1.7-4.6-5.1-4.6-10.2V433.2c0-4.8 1.5-8.2 4.6-10.2 3.1-2 6.8-1.7 11.2 1l377.6 210c4.4 2.4 6.6 5.3 6.6 8.7 0 3.3-2.2 6.2-6.6 8.6z"></path></g></g></g></svg>
            </div>
            <div class="episode-content">
                <div>
                    <span class="ep-grid-header"
                        @click="goToEpisode(episode)">
                        {{ episode.number }}- {{ episode.title }}
                    </span>
                </div>
                <div v-if="episode.tags" class="tags">
                    <span v-for="(tag, index) in getEpisodeTags(episode.tags)"
                        :key='index'>
                        <span class="tag-pill" @click="searchTag(tag)">#{{ formatTag(tag) }}</span>
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import FuzzyImage from '@/components/FuzzyImage'

export default {
    components: {
        FuzzyImage
    },

    props: {
        episode: Object
    },

    data() {
        return {
            inView: false
        }
    },

    methods: {

        goToEpisode(episode) {
            this.$router.push(`/episodes/${episode.number}`)
        },

        getThumbnail(path) {
            let image = path.split('/')[2] 
            return 'episodes/images/thumbnails/' + image;
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

        searchTag(tag) {
            let options = {
                left: 0,
                top: 0,
                behavior: 'smooth'
            }
            window.scrollTo(options)
            this.$router.push('/episodes?search=' + encodeURIComponent(tag))
            this.$parent.search = tag
        },

        scrollIntoView() {
            let element = this.$el
            let elementHeight = element.clientHeight
            let windowHeight = window.innerHeight
            let scrollY = window.scrollY || window.pageYOffset
            let scrollPosition = scrollY + windowHeight
            let elementPosition = element.getBoundingClientRect().top + scrollY + elementHeight
            let offset = scrollPosition + (elementHeight * 0.75)

            this.inView = offset > elementPosition ? true : false
        }
    },

    watch: {
        inView() {
            if (this.inView === true)
                window.removeEventListener('scroll', this.scrollIntoView)
        }
    },

    mounted() {
        this.scrollIntoView()
    },

    created() {
        window.addEventListener('scroll', this.scrollIntoView)
    },

    beforeDestroy() {
        window.removeEventListener('scroll', this.scrollIntoView)
    }
}
</script>