<template>
    <div id="live" class="content clearfix">

        <div class="background-container">
            <img id="bg" :src="bg" alt="">
            <img id="intro" :src="intro" alt="">
        </div>

        <PlayButton />

        <div id="actions">
            <a href="mailto:hello@introtorhythm.com">hello@introtorhythm.com</a><br>
            <a href="tel:9718018007">971-801-8007</a><br>
            <a href="#chat" @click.prevent="goDown()">Chat</a>
        </div>
        
        <Marquee v-if="loaded && showMarquee" :text="marqueeText" />
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
            intro: require('@/assets/images/introtorhythm-orange.png'),
            showMarquee: true,
            compareMarqueeText: '',
        }
    },

    methods: {
        goDown() {
            document.getElementById('chat-wrapper').scrollIntoView({ block: 'end',  behavior: 'smooth' });
        },

        forceRemount() {
            this.showMarquee = false;
            this.$nextTick(() => {
                this.showMarquee = true;
            });
            this.compareMarqueeText = this.marqueeText;
        },
    },


    watch: {
        marqueeText() {
            if (this.compareMarqueeText != this.marqueeText)
                this.forceRemount();
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