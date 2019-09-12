import { SubscriptionForm } from './SubscriptionForm.js';

export var Navigation = {
    components: {
        'SubscriptionForm': SubscriptionForm
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
        resize() {
            var width = document.documentElement.clientWidth;  
            if (width > 750)
                this.$parent.mobile = false;
            else
              this.$parent.mobile = true;
        }
    },
    computed: {
        showNav() {
            return this.$parent.mobile && this.$parent.showMobileNav || !this.$parent.mobile;
        },
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
        window.addEventListener('resize', this.resize);
    },
    template: `
        <div>
            <div id="mobile-nav-toggle" v-if="$parent.mobile">
                <div id="menu-container" @click="toggleMobileNav()" :class="{ 'change': $parent.showMobileNav }">
                    <div class="bar1"></div>
                    <div class="bar2"></div>
                    <div class="bar3"></div>
                </div>
            </div>
            <div id="nav" v-if="loaded && showNav">
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
                    <SubscriptionForm />
                </ul>
            </div>
        </div>
    `
}