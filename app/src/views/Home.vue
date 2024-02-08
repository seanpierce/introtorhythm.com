<template>
    <div id="live" class="content clearfix">

        <div class="background-container">
            <img id="bg" :src="bg" alt="">
            <img id="intro" :src="intro" alt="">
        </div>

        <PlayButton />

        <div id="info">
            <a href="mailto:hello@introtorhythm.com">hello@introtorhythm.com</a><br>
            <a href="tel:9718018007">971-801-8007</a><br>
            <a href="#chat" @click.prevent="goDown()">Chat</a>
        </div>
        
        <Marquee v-if="loaded" :text="marqueeText" />
    </div>
</template>

<script>
import PlayButton from '@/components/PlayButton'
import Marquee from '@/components/Marquee'

export default {
    components: {
        PlayButton,
        Marquee
    },

    data() {
        return {
            bg: require('@/assets/images/i2r-bg-big-tall.png'),
            intro: require('@/assets/images/introtorhythm-orange.png')
        }
    },

    methods: {
        goDown() {
            window.scrollTo(0, document.body.scrollHeight);
        }
    },

    computed: {
        marqueeText() {
            return this.$store.state.content.marqueeText
        },

        loaded() {
            return this.marqueeText?.length > 0 || false
        }
    }
}
</script>