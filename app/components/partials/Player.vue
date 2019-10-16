<template>
    <div id="player" v-if="loaded">
        <div>
            <div id="controls" @click="$parent.togglePlay()">
                <img :src="$parent.playing ? '/assets/images/pause-icon.png' : '/assets/images/play-icon.png'">
            </div>
            <div id="timeline">
                <div id="playHead" :style="{ marginLeft: $parent.playPercent + 'px' }"></div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
        }
    },
    methods: {
        getPlayerWidth() {
            var player = document.getElementById('timeline');
            var playHead = document.getElementById('playHead');
            var playerWidth = player.offsetWidth - playHead.offsetWidth;
            this.$parent.playerWidth = playerWidth;
        },
        clickEvent(event) {
            var player = document.getElementById('timeline');
            var percent = (event.pageX - player.offsetLeft) / this.$parent.playerWidth;
            this.$parent.audio.currentTime = this.$parent.audio.duration * percent;
        },
        mouseDownEvent() {
            this.$parent.onplayHead = true;
            window.addEventListener('mousemove', this.movePlayHead, true);
            window.addEventListener('mouseup', this.mouseUpEvent, false);
            this.$parent.audio.removeEventListener('timeupdate', this.$parent.timeUpdate, false);
        },
        mouseUpEvent() {
            this.$parent.onplayHead = false;
            this.$parent.audio.addEventListener('timeupdate', this.$parent.timeUpdate, true);
            window.removeEventListener('mousemove', this.movePlayHead, true);
            window.removeEventListener('mouseup', this.mouseUpEvent, true);
        },
        movePlayHead(event) {
            var player = document.getElementById('timeline');
            var playHead = document.getElementById('playHead');
            var margin = event.pageX - player.offsetLeft;

            if (margin >= 0 && margin <= this.$parent.playerWidth)
                playHead.style.marginLeft = margin + "px";

            if (margin < 0)
                  playHead.style.marginLeft = "0px";

            if (margin > this.$parent.playerWidth)
                playHead.style.marginLeft = this.$parent.playerWidth + "px"
        },
    },
    computed: {
        loaded() {
            return this.$root.loaded;
        }
    },
    mounted() {
        var player = document.getElementById('timeline');
        var playHead = document.getElementById('playHead');

        this.getPlayerWidth();

        player.addEventListener('click', (event) => {
            this.clickEvent(event);
        });

        playHead.addEventListener('mousedown', this.mouseDownEvent, false);
        window.addEventListener('resize', this.getPlayerWidth);
    },
}
</script>