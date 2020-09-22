<template>
    <div class="episode-image" v-bind:class="{ blur: !loaded }" :style="{ backgroundImage: 'url(' + mediaUrl  + (loaded ? image : thumbnail) + ')' }"></div>
</template>

<script>
export default {
    props: [
        'thumbnail',
        'image'
    ],
    data() {
        return {
            loaded: false,
            mediaUrl: process.env.VUE_APP_MEDIA_URL 
        }
    },
    methods: {
        preloadImage() {
            var image = new Image();
            image.onload = () => {
                this.loaded = true;
            }
            image.src = this.mediaUrl + this.image;
        },
    },
    mounted() {
        this.preloadImage();
    }
}
</script>