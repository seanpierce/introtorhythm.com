<template>
    <div class="slider" v-if="episodes">
        <div class="cover-filter"></div>
        <div class="slide"
            v-bind:class="{ selected: index === i }"
            v-for="(ep, i) in episodes"
            :key="i"
            :style="{ backgroundImage: 'url(' + $root.mediaUrl + ep.image + ')' }">
            <div class="show-info pointer" @click="goToEpisode(ep.number)">
                <div class="title">Episode {{ ep.number }}</div>
                <div class="show-time">{{ ep.title }}</div>
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
            index: 0
        }
    },
    methods: {
        next() {
            var next = this.index + 1;
            if (next === this.episodes.length)
                next = 0;
            this.index = next;
        },
        previous() {
            var previous = this.index - 1;
            if (previous < 0)
                previous = this.episodes.length - 1;
            this.index = previous;
        },
        goToEpisode(number) {
            window.location.href = "/episodes/" + number;
        },
        cycle() {
            setInterval(() => {
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