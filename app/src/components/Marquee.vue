<template>
    <div class="marquee-wrapper" v-if="loaded">
        <div id="live-marquee" class="marquee">
            {{ marqueeText }}
        </div>
    </div>
</template>

<script>
import nodeMarquee from 'node-marquee'

export default {
    computed: {
        marqueeText() {
            return this.$store.state.content.marqueeText
        },

        loaded() {
            return this.marqueeText?.length > 0 || false
        }
    },

    mounted() {
        nodeMarquee({
            parent: '#live-marquee'
        })
    }
}
</script>