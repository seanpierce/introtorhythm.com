<template>
    <div id="nav">
        <h1><a href="/">Intro To Rhythm</a></h1>
        <ul>
            <li>
                <span class="red"
                    @click="showEpisodeInfoModal()">Ep {{ currentEpisode.number }} - {{ currentEpisode.title }} &lt;
                </span>
            </li>
            <li>
                <span>{{ $parent.currentTime }} / {{ $parent.totalTime || "00:00:00" }}</span>
            </li>
            <li>------</li>
            <li>
                <span v-if="nums.prev">
                    <a :href="'/' + nums.prev">&lt; {{ nums.prev }}</a>
                </span>
                <span v-if="nums.prev && nums.next"> - </span>
                <span v-if="nums.next">
                    <a :href="'/' + nums.next">{{ nums.next }} ></a>
                </span>
            </li>
            <li>
                <span @click="showEpisodesModal()">Episodes</span>
            </li>
            <li>
                <span @click="showAboutModal()">ITR Info</span>
            </li>
            <li>
                <span @click="showSubscribeModal()">Subscribe</span>
            </li>
            <li>------</li>
            <li>
                <span>
                    <a href="live" id="live">ITR Live</a>
                </span>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    methods: {
        showEpisodeInfoModal() {
            this.$parent.showEpisodeInfoModal = true;
        },
        showAboutModal() {
            this.$parent.showAboutModal = true;
        },
        showEpisodesModal() {
            this.$parent.showEpisodesModal = true;
        },
        showSubscribeModal() {
            this.$parent.showSubscribeModal = true;
        }
    },
    computed: {
        loaded() {
            return this.$root.loaded;
        },
        currentEpisode() {
            return this.$root.data;
        },
        nums() {
            return this.$root.nums;
        }
    },
    mounted() {
        window.addEventListener('resize', this.resize);
    }
}
</script>