<template>
    <div id="live-marquee" class="marquee">
        {{ text }}
    </div>
</template>

<script>
import nodeMarquee from 'node-marquee'

export default {
    props: {
        text: {
            type: String
        }
    },

    mounted() {
        nodeMarquee({
            parent: '#live-marquee'
        })
    }
}
</script>