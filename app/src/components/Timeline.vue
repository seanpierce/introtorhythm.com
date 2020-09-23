<template>
    <div id="timeline" @click="timelineClickEvent($event)">
        <div id="playhead" 
            @mousedown="playheadMouseDown()"
            :style="{ marginLeft: playPercent + 'px' }"></div>
        <span class="timeline__time">{{ formatTime(currentTime) }} / {{ formatTime(duration) }}</span>
    </div>
</template>

<script>
import { formatTime } from '@/utilities'

export default {

    props: {
        active: Boolean
    },

    data() {
        return {
            timeline: null,
            playhead: null,
            playerWidth: null,
            onPlayhead: false,
            mounted: false,
            mouseDropLocation: null,
            formatTime: formatTime
        }
    },
    methods: {

        getPlayerWidth() {
            this.playerWidth = this.timeline.offsetWidth - this.playhead.offsetWidth
        },

        timelineClickEvent(event) {
            var percent = (event.pageX - this.timeline.offsetLeft) / this.playerWidth
            // set current time in episodes store
            this.$store.dispatch('setCurrentTime', this.audio.duration * percent)
        },

        playheadMouseDown() {
            this.onPlayhead = true
            window.addEventListener('mousemove', this.movePlayHead, true)
            window.addEventListener('mouseup', this.mouseUpEvent, false)
        },

        mouseUpEvent() {
            this.onplayhead = false
            window.removeEventListener('mousemove', this.movePlayHead, true)
            window.removeEventListener('mouseup', this.mouseUpEvent, true)

            this.setCurrentTime(this.mouseDropLocation)
        },

        movePlayHead(event) {
            if (!this.audio) return

            var margin = event.pageX - this.timeline.offsetLeft

            if (margin >= 0 && margin <= this.playerWidth)
                this.mouseDropLocation = margin

            if (margin < 0)
                this.mouseDropLocation = 0

            if (margin > this.playerWidth)
                this.mouseDropLocation = this.playerWidth
        },

        setCurrentTime(input) {
            this.$store.dispatch('setCurrentTime', input)
        }

    },

    computed: {
        audio() {
            return this.$store.state.episodes.audio
        },

        currentTime() {
            return this.$store.state.episodes.currentTime || 0
        },

        duration() {
            return this.$store.state.episodes.duration || 0
        },

        playPercent() {
            if (this.mouseDropLocation && this.onPlayhead)
                return this.mouseDropLocation

            try {
                return this.playerWidth * (this.currentTime / this.duration)
            } catch {
                return 0
            }
        },
    },

    mounted() {
        this.timeline = document.getElementById('timeline')
        this.playhead = document.getElementById('playhead')

        this.getPlayerWidth()

        if (!this.mounted)
            window.addEventListener('resize', this.getPlayerWidth())
        
        this.mounted = true
    },

    destroyed() {
        window.removeEventListener('resize', this.getPlayerWidth())
    },
}
</script>