<template>
    <div id="episodes" class="content" v-if="episodes">
        <div id="episode-search">
            <input type="text" id="episode-search-input" v-model="search" placeholder="Search">
            <img id="search-icon" :src="require('@/assets/images/search-icon.svg')">
        </div>

        <div id="episodes-grid">
            <EpisodeCard v-for="episode in searchEpisodes" :key="episode.id" :episode="episode" />
        </div>
        <Footer :position="searchEpisodes.length === 0 ? 'absolute' : ''"/>
    </div>
</template>

<script>
import EpisodeCard from '@/components/EpisodeCard'
import Footer from '@/components/Footer'

export default {

    components: {
        EpisodeCard,
        Footer
    },

    data() {
        return {
            search: null
        }
    },

    computed: {

        searchEpisodes() {
            if (!this.search || this.search.length < 3) return this.episodes
            else return this.filterEpisodes()
        },

        episodes() {
            return this.$store.state.episodes.episodes || null
        }
    },

    methods: {

        focusSearch() {
            let elem = document.getElementById('episode-search-input')
            elem.focus()
        },

        filterEpisodes() {
            let term = this.search.toLowerCase()
            let output = []

            this.episodes.forEach(episode => {
                if (episode.number.toLowerCase().indexOf(term) > -1)
                    add(episode)

                if (episode.title.toLowerCase().indexOf(term) > -1)
                    add(episode)

                if (episode.tags.toLowerCase().indexOf(term) > -1)
                    add(episode)

                if (episode.content.toLowerCase().indexOf(term) > -1)
                    add(episode)
            })

            function add(episode) {
                if (output.indexOf(episode) === -1)
                    output.push(episode)
            }

            return output
        }
    },

    mounted() {
        this.focusSearch()
    }
}
</script>