import { SubscriptionForm } from './SubscriptionForm.js';
import { MobileNav } from './MobileNav.js';

export var Navigation = {
    components: {
        'SubscriptionForm': SubscriptionForm,
        'MobileNav': MobileNav
    },
    data() {
        return {
        }
    },
    methods: {
        isCurrent(number) {
            return this.currentEpisode.number === number;
        },
        showEpisodeInfoModal() {
            this.$parent.showEpisodeInfoModal = true;
        },
        showAboutModal() {
            this.$parent.showAboutModal = true;
        },
        toggleMobileNav() {
            this.$parent.showMobileNav = !this.$parent.showMobileNav;
        },
    },
    computed: {
        loaded() {
            return this.$root.loaded;
        },
        currentEpisode() {
            return this.$root.data.current_episode;
        },
        episodes() {
            return this.$root.data.episodes;
        },
    },
    mounted() {
    },
    template: `
        <div>
            <MobileNav v-if="$parent.mobile" />
            <div id="nav" v-if="loaded && !$parent.mobile">
                <ul>
                    <li><a href="/">Intro To Rhythm</a><li>
                    <li>------</li>
                    <li>Now Playing: Ep {{ currentEpisode.number }}</li>
                    <li id="tracktime">{{ $parent.currentTime }} / {{ $parent.totalTime || '00:00:00' }}</li>
                    <li>
                    <span 
                        class="red pointer"
                        @click="showEpisodeInfoModal()">
                        See Ep {{ currentEpisode.number }} Info &lt;
                    </span>
                    </li>
                    <li>------</li>
                    <li v-for="episode in episodes" :key="episode.number" :class="isCurrent(episode.number) ? 'red': ''">
                    <a :href="'/' + episode.number">{{ episode.number }}- {{ episode.title }}</a>
                    </li>
                    <li>------</li>
                    <li><span class="pointer" @click="showAboutModal()">About ITR</span></li>
                    <li><a href="/archive">Archive</a></li>
                    <li>------</li>
                    <SubscriptionForm />
                </ul>
            </div>
        </div>
    `
}