<template>
    <div class="marquee-wrapper">
        <div id="live-marquee" class="marquee">
            {{ text }}
        </div>
    </div>
</template>

<script>
// Check out https://github.com/ezekielaquino/Marquee3000
import nodeMarquee from 'node-marquee'

export default {
    props: {
        text: String
    },

    mounted() {
        nodeMarquee({
            parent: '#live-marquee',
            pauseOnHover: true,
            speed: 4
        })
    }
}
</script>