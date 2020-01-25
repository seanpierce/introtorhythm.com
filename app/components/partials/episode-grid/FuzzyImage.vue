<template>
    <div class="episode-image" v-bind:class="{ blur: !loaded }" :style="{ backgroundImage: 'url(' + $root.mediaUrl + (loaded ? image : thumbnail) + ')' }"></div>
</template>

<script>
export default {
    props: [
        'thumbnail',
        'image'
    ],
    data() {
        return {
            loaded: false
        }
    },
    methods: {
        preloadImage() {
            var image = new Image();
            image.onload = () => {
                this.loaded = true;
            }
            image.src = this.$root.mediaUrl + this.image;
        },
    },
    mounted() {
        this.preloadImage();
    }
}
</script>