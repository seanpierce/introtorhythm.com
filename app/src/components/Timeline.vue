<template>
    <div id="timeline">
        <div id="playhead" :style="{ marginLeft: playPercent + 'px' }"></div>
    </div>
</template>

<script>
export default {

    data() {
        return {
            playerWidth: null,
            onplayHead: false,
            playPercent: 0
        }
    },
    methods: {

        getPlayerWidth() {
            var player = document.getElementById('timeline')
            var playHead = document.getElementById('playhead')
            var playerWidth = player.offsetWidth - playHead.offsetWidth
            this.playerWidth = playerWidth
        },

        clickEvent(event) {
            var player = document.getElementById('timeline')
            var percent = (event.pageX - player.offsetLeft) / this.playerWidth
            console.log(percent)
            // set current time in episodes store
            // this.$parent.audio.currentTime = this.audio.duration * percent
        },

        mouseDownEvent() {
            this.onplayHead = true
            window.addEventListener('mousemove', this.movePlayHead, true)
            window.addEventListener('mouseup', this.mouseUpEvent, false)
            // dispatch store event to REMOVE event listener from audio
            // this.$parent.audio.removeEventListener('timeupdate', this.$parent.timeUpdate, false)
        },

        mouseUpEvent() {
            this.onplayHead = false
            // dispatch store event to ADD event listener to audio
            // this.$parent.audio.addEventListener('timeupdate', this.$parent.timeUpdate, true)
            window.removeEventListener('mousemove', this.movePlayHead, true)
            window.removeEventListener('mouseup', this.mouseUpEvent, true)
        },

        movePlayHead(event) {
            if (!this.audio) return

            var player = document.getElementById('timeline')
            var margin = event.pageX - player.offsetLeft

            if (margin >= 0 && margin <= this.playerWidth) {
                this.playPercent = margin
            }

            if (margin < 0)
                this.playPercent = 0

            if (margin > this.playerWidth)
                this.playPercent = this.playerWidth
        },

    },

    computed: {
        audio() {
            return this.$store.state.episodes.audio
        },

        currentTime() {
            return this.audio?.currentTime
        }
    },

    mounted() {

        var player = document.getElementById('timeline');
        var playhead = document.getElementById('playhead');

        this.getPlayerWidth();

        player.addEventListener('click', (event) => {
            this.clickEvent(event);
        });

        playhead.addEventListener('mousedown', this.mouseDownEvent, false);
        window.addEventListener('resize', this.getPlayerWidth);
    },
}
</script>