<template>
    <div class="marquee-wrapper">
        <div id="live-marquee" class="marquee">
            {{ text }}
        </div>
    </div>
</template>

<script>
import nodeMarquee from 'node-marquee'

export default {
    props: {
        text: String
    },

    mounted() {
        nodeMarquee({
            parent: '#live-marquee'
        })
    }
}
</script>