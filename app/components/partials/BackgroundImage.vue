<template>
    <div>
        <div id="brighten"></div>
        <div id="background-image" :style="{ backgroundImage: 'url(' + imageUrl + ')' }"></div>
    </div>
</template>

<script>
export default {
    computed: {
        imageUrl() {
            return this.$root.mediaUrl + this.$parent.currentEpisode.image;
        }
    },
}
</script>