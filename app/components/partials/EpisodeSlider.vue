<template>
    <div class="slider" v-if="episodes">
        <div class="slide"
            v-bind:class="{ selected: index === i }"
            v-for="(ep, i) in episodes"
            :key="i"
            :style="{ backgroundImage: 'url(' + $root.mediaUrl + ep.image + ')' }">
            <div class="show-info pointer">
                <div @click="goToEpisode(ep.number)">
                    <div class="title"><h2>Latest Episodes</h2></div>
                    <div class="show-time">{{ ep.number }}- {{ ep.title }}</div>
                </div>
                <div class="slider-circles">
                    <span v-for="(ep, i) in episodes" :key="i" 
                        v-bind:class="{ selected: index === i }"
                        @click="jumpTo(i)"></span>
                </div>
            </div>
            <div class="go-to-episode" @click="goToEpisode(ep.number)">
                <img src="/assets/images/icons/play-arrow.svg" /> Listen to episode {{ ep.number }}
            </div>
        </div>
        <div class="prev" @click="previous()"><img src="/assets/images/icons/left.svg"></div>
        <div class="next" @click="next()"><img src="/assets/images/icons/right.svg"></div>
	</div>
</template>

<script>
export default {
    props: [
        'episodes'
    ],
    data() {
        return {
            index: 0,
            interval: null
        }
    },
    methods: {
        next() {
            clearInterval(this.interval);
            var next = this.index + 1;
            if (next === this.episodes.length)
                next = 0;
            this.index = next;
            this.cycle();
        },
        previous() {
            clearInterval(this.interval);
            var previous = this.index - 1;
            if (previous < 0)
                previous = this.episodes.length - 1;
            this.index = previous;
            this.cycle();
        },
        jumpTo(index) {
            clearInterval(this.interval);
            this.index = index;
            this.cycle(); 
        },
        goToEpisode(number) {
            window.location.href = "/episodes/" + number;
        },
        cycle() {
            this.interval = setInterval(() => {
                this.next();
            }, 4000)
        }
    },
    mounted() {
        setTimeout(() => {
            this.cycle();
        }, 1000);
    }
}
</script>