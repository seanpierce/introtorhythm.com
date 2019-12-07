<template>
    <div>
        <div v-if="!loaded" style="text-align:center">
            <em>LOADING</em>
        </div>
        <div class="episodes-grid" v-if="loaded">
            <div class="episode-wrapper"
                v-for="episode in showEpisodes"
                :key="episode.id"
                @click="goToEpisode(episode.number)">
                <div class="episode-inner-wrapper">
                    <div class="episode-image"
                        :style="{ backgroundImage: 'url(' + $root.mediaUrl + episode.image + ')' }">
                        <svg class="play-button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600"><title>Play</title><g id="_x33_--Hidden-_x28_closing-up_x29_-" transform="translate(-772 -385)"><g id="Drawer" transform="translate(0 43)"><g id="_x32_" transform="translate(18)"><path id="play" d="M1260.4 651.3L882.8 861.2c-4.4 2.4-8.2 2.7-11.2 1-3.1-1.7-4.6-5.1-4.6-10.2V433.2c0-4.8 1.5-8.2 4.6-10.2 3.1-2 6.8-1.7 11.2 1l377.6 210c4.4 2.4 6.6 5.3 6.6 8.7 0 3.3-2.2 6.2-6.6 8.6z"></path></g></g></g></svg>
                    </div>
                    <div class="episode-content">
                        {{ episode.number }}- {{ episode.title }}
                    </div>
                </div>
            </div>
        </div>
        <div class="show-more-button" v-if="showShowMore && loaded" @click="showMore()">
            <span>Load more</span>
        </div>
    </div>
</template>

<script>
export default {
    props: [
        'episodes',
        'paginate'
    ],
    data() {
        return {
            imageCount: 0,
            loadedImages: 0,
            showEpisodes: []
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
        }
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