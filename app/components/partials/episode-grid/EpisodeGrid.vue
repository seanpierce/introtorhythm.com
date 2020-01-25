<template>
    <div>
        <!-- <div v-if="!loaded" style="text-align:center">
            <em>LOADING</em>
        </div> -->
        <div class="episodes-grid">
            <div class="episode-wrapper"
                v-for="episode in episodes"
                :key="episode.id">
                <div class="episode-inner-wrapper">
                    <div class="episode"
                        @click="goToEpisode(episode.number)">
                        <!-- <div class="episode-image blur" :style="{ backgroundImage: 'url(' + $root.mediaUrl + getThumbnail(episode.image) + ')' }"></div> -->
                        <FuzzyImage :thumbnail="getThumbnail(episode.image)" :image="episode.image" />
                        <svg class="play-button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600"><title>Play</title><g id="_x33_--Hidden-_x28_closing-up_x29_-" transform="translate(-772 -385)"><g id="Drawer" transform="translate(0 43)"><g id="_x32_" transform="translate(18)"><path id="play" d="M1260.4 651.3L882.8 861.2c-4.4 2.4-8.2 2.7-11.2 1-3.1-1.7-4.6-5.1-4.6-10.2V433.2c0-4.8 1.5-8.2 4.6-10.2 3.1-2 6.8-1.7 11.2 1l377.6 210c4.4 2.4 6.6 5.3 6.6 8.7 0 3.3-2.2 6.2-6.6 8.6z"></path></g></g></g></svg>
                    </div>
                    <div class="episode-content">
                        <div>
                            <span class="ep-grid-header"
                                @click="goToEpisode(episode.number)">
                                {{ episode.number }}- {{ episode.title }}
                            </span>
                        </div>
                        <div v-if="episode.tags" class="tags">
                            <span
                                v-for="(tag, index) in getEpisodeTags(episode.tags)"
                                :key='index'>
                                <span class="tag-pill" @click="searchTag(tag)">#{{ formatTag(tag) }}</span>
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <SearchModal v-if="modal === 'search-tags'"
            :tag-search="true"
            :modal-data="modalData" />
    </div>
</template>

<script>
import axios from 'axios';
import SearchModal from '../modals/SearchModal';
import FuzzyImage from './FuzzyImage';

export default {
    components: {
        SearchModal,
        FuzzyImage
    },
    props: {
        paginate: {
            type: Boolean,
            default: false
        },
        episodes: {
            type: Array,
            default: []
        }
    },
    data() {
        return {
            imageCount: 0,
            loadedImages: 0,
            modal: null,
            modalData: null,
            loadingMore: false,
            loadedAll: false
        }
    },
    methods: {
        // preloadImages() {
        //     var images = this.episodes.map(x => x.image);
        //     this.imageCount = images.length;
        //     images.forEach(img => {
        //         var image = new Image();
        //         image.onload = () => {
        //             this.loadedImages ++;
        //         }
        //         image.src = this.$root.mediaUrl + img;
        //     });
        // },
        getThumbnail(path) {
            var image = path.split('/')[2] 
            return 'episodes/images/thumbnails/' + image;
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
        getEpisodeTags(tags) {
            tags = tags.split(',').map(x => this.formatTag(x));
            return tags.sort((a, b) => {
                if (a < b) return -1;
                if (a > b) return 1;
                return 0;
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
        loadMore() {
            var vm = this;
            if (!this.episodes) return;
            this.loadingMore = true;
            axios.post('/api/episodes/paginate', { offset: this.episodes.length, take: 6 })
                .then(res => {
                    var eps = res.data;
                    if (eps.length === 0) {
                        this.loadedAll = true;
                        return;
                    }

                    eps.forEach(ep => {
                        this.episodes.push(ep);
                    })
                    this.loadingMore = false;
                })
        },
        setLazyLoad() {
            window.onscroll = () => {
                let bottomOfWindow = document.documentElement.scrollTop > this.$el.offsetHeight;
                if (bottomOfWindow && !this.loadingMore && !this.loadedAll) {
                    this.loadMore();
                }
            };
        }
    },
    computed: {
    },
    mounted() {
        if (this.paginate) {
            this.setLazyLoad();
        }
    }
}
</script>