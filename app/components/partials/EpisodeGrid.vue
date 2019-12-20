<template>
    <div>
        <div v-if="!loaded" style="text-align:center">
            <em>LOADING</em>
        </div>
        <div class="episodes-grid" v-if="loaded">
            <div class="episode-wrapper"
                v-for="episode in showEpisodes"
                :key="episode.id">
                <div class="episode-inner-wrapper">
                    <div class="episode-image"
                        @click="goToEpisode(episode.number)"
                        :style="{ backgroundImage: 'url(' + $root.mediaUrl + episode.image + ')' }">
                        <svg class="play-button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600"><title>Play</title><g id="_x33_--Hidden-_x28_closing-up_x29_-" transform="translate(-772 -385)"><g id="Drawer" transform="translate(0 43)"><g id="_x32_" transform="translate(18)"><path id="play" d="M1260.4 651.3L882.8 861.2c-4.4 2.4-8.2 2.7-11.2 1-3.1-1.7-4.6-5.1-4.6-10.2V433.2c0-4.8 1.5-8.2 4.6-10.2 3.1-2 6.8-1.7 11.2 1l377.6 210c4.4 2.4 6.6 5.3 6.6 8.7 0 3.3-2.2 6.2-6.6 8.6z"></path></g></g></g></svg>
                    </div>
                    <div class="episode-content">
                        <div @click="goToEpisode(episode.number)">{{ episode.number }}- {{ episode.title }}</div>
                        <div v-if="episode.tags" class="tags">
                            <span
                                v-for="(tag, index) in episode.tags.split(',')"
                                :key='index'>
                                <span class="tag-pill" @click="searchTag(tag)">#{{ formatTag(tag) }}</span>
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="show-more-button" v-if="showShowMore && loaded" @click="showMore()">
            <span>Load more</span>
        </div>
        <SearchModal v-if="modal === 'search-tags'"
            :tag-search="true"
            :modal-data="modalData" />
    </div>
</template>

<script>
import axios from 'axios';
import SearchModal from './modals/SearchModal.vue';

export default {
    components: {
        SearchModal
    },
    props: [
        'episodes',
        'paginate'
    ],
    data() {
        return {
            imageCount: 0,
            loadedImages: 0,
            showEpisodes: [],
            modal: null,
            modalData: null
        }
    },
    methods: {
        preloadImages() {
            var images = this.episodes.map(x => x.image);
            this.imageCount = images.length;
            images.forEach(img => {
                var image = new Image();
                image.onload = () => {
                    this.loadedImages ++;
                }
                image.src = this.$root.mediaUrl + img;
            });
        },
        initialShowEpisodes() {
            if (!this.paginate) this.showEpisodes = this.episodes;
            else {
                this.showEpisodes = this.episodes.slice(0, this.paginate);
            }
        },
        showMore() {
            var startAt = this.showEpisodes.length;
            var take = this.paginate + startAt;
            var add = this.episodes.slice(startAt, take);
            this.showEpisodes = this.showEpisodes.concat(add);
        },
        goToEpisode(number) {
            window.location.href = '/episodes/' + number;
        },
        formatTag(tag) {
            if (tag[0] === ' ')
                tag = tag.slice(1);

            if (tag[tag.length -1] === ' ')
                tag = tag.slice(0, -1);

            return tag;
        },
        searchTag(tag) {
            tag = this.formatTag(tag);
            axios.post('/api/episodes/search/tag', { tag: tag })
                .then(response => {
                    this.modalData = {
                        data: response.data,
                        tag: tag
                    }
                    this.showModal('search-tags');
                })
        },
        showModal(name) {
            this.modal = name;
            document.body.style.overflow = 'hidden';
        },
        hideModal() {;
            this.modal = null;
            document.body.style.overflow = 'inherit';
        },
    },
    computed: {
        loaded() {
            if (this.imageCount === 0) return false;
            if (this.imageCount === this.loadedImages)
                return true;
            else return false;
        },
        showShowMore() {
            return this.episodes.length !== this.showEpisodes.length;
        }
    },
    mounted() {
        this.initialShowEpisodes();
        this.preloadImages();
    }
}
</script>