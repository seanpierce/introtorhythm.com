<template>
    <div class="episodes-grid">
        <div v-if="!loaded" style="text-align:center">
            <em>LOADING</em>
        </div>
        <div v-if="loaded">
            <div v-for="episode in showEpisodes"
                :key="episode.id"
                class="episode-container"
                @click="goToEpisode(episode.number)">
                <div class="episode-wrapper">
                    <div class="episode"
                        :style="{ backgroundImage: 'url(' + $root.mediaUrl + episode.image + ')' }">
                        <div class="episode-content">
                            <div>{{ episode.number }}<br>{{ episode.title }}</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="show-more-button" v-if="showShowMore" @click="showMore()">
                Show more
            </div>
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