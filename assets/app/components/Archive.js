export var Archive = {
    data() {
        return {
        }
    },
    methods: {
        formatFileName(number, title) {
            var formattedTitle = title.replace(/[-,./ !*:]/g, '_');
            return '/' + number + '_' + formattedTitle;
        } 
    },
    computed: {
        episodes() {
            return this.$root.data.episodes;
        }
    },
    template: `
        <div id="archive">
            <div><a href="/">Intro To Rhythm/</a></div>
            <div class="tab-1">archive/</div>
            <div class="tab-2">episodes/</div>
            <div class="tab-3">
                <li v-for="episode in episodes" :key="episode.number">
                    <a :href="'/' + episode.number">{{ formatFileName(episode.number, episode.title) }}</a>
                </li>
            </div>
        </div>
    `
}