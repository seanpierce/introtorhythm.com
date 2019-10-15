export var Navigation = {
    template: `
        <div id="nav">
            <h1><a href="/">Intro To Rhythm</a></h1>
            <ul>
                <li>
                    <span class="red"
                        @click="showEpisodeInfoModal()">Ep {{ currentEpisode.number }} - {{ currentEpisode.title }} <
                    </span>
                </li>
                <li>
                    <span>{{ $parent.currentTime }} / {{ $parent.totalTime || "00:00:00" }}</span>
                </li>
                <li>------</li>
                <li>
                    <span v-if="nums.prev">
                        <a :href="'/' + nums.prev">< {{ nums.prev }}</a>
                    </span>
                    <span v-if="nums.prev && nums.next"> - </span>
                    <span v-if="nums.next">
                        <a :href="'/' + nums.next">{{ nums.next }} ></a>
                    </span>
                </li>
                <li>
                    <span @click="showEpisodesModal()">See all episodes</span>
                </li>
                <li>
                    <span @click="showAboutModal()">ITR info</span>
                </li>
                <li>
                    <span @click="showSubscribeModal()">Subscribe</span>
                </li>
            </ul>
        </div>
    `,
    components: {
    },
    data() {
        return {
        }
    },
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