<template>
    <div class="slider" v-if="episodes">
        <div class="slide"
            v-bind:class="{ selected: index === i }"
            v-for="(ep, i) in episodes"
            :key="i"
            :style="{ backgroundImage: 'url(' + $root.mediaUrl + ep.image + ')' }">
            <div class="show-info pointer" @click="goToEpisode(ep.number)">
                <div class="title"><h2>Latest Episodes</h2></div>
                <div class="show-time">{{ ep.number }}- {{ ep.title }}</div>
            </div>
            <div class="go-to-episode" @click="goToEpisode(ep.number)">
                Listen to episode {{ ep.number }}
            </div>
        </div>
        <div class="prev" @click="previous()"><span>&lt;</span></div>
        <div class="next" @click="next()"><span>&gt;</span></div>
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
        }, 3000);
    }
}
</script>