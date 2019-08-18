<template>
    <div id="archive" v-if="loaded">
        <ul>
            <li><a href="/">Intro To Rhythm/</a></li>
            <li class="pad-2">archive/</li>
            <li class="pad-4">episodes/</li>
            <li class="pad-6" v-for="episode in episodes" :key="episode.number">
                <a :href="'/' + episode.number">{{ episode.number }}_{{ formatTitle(episode.title) }}</a>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    components: {
    },
    data() {
        return {
        }
    },
    methods: {
        formatTitle(title) {
            var lowerTitle = title.toLowerCase();
            return lowerTitle.replace(/[ -.!*:/]/g,'_');
        }
    },
    computed: {
        episodes() {
            return this.$root.data.episodes;
        },
        loaded() {
            return this.$root.loaded;
        }
    },
    mounted() {
    }
}
</script>