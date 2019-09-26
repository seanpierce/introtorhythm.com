import { SubscriptionForm } from './SubscriptionForm.js';

export var MobileNav = {
    components: {
        'SubscriptionForm': SubscriptionForm
    },
    data() {
        return {
            openMobileNav: false,
            toggleElements: true
        }
    },
    methods: {
        toggleMobileNav() {
            this.openMobileNav = !this.openMobileNav;
            this.toggleHideElements();
        },
        isCurrent(number) {
            return this.currentEpisode.number === number;
        },
        showEpisodeInfoModal() {
            return this.$parent.showEpisodeInfoModal();
        },
        showAboutModal() {
            return this.$parent.showAboutModal();
        },
        toggleHideElements() {
            this.toggleElements = !this.toggleElements;
            var home = this.$parent.$parent;
            home.showPlayButton = this.toggleElements;
            home.showPlayer = this.toggleElements;
        },
        resize() {
            var width = document.documentElement.clientWidth;  
            if (width > 750) {
                this.toggleElements = false;
                this.toggleHideElements();
            }
        }
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
        currentTime() {
            return this.$parent.$parent.currentTime;
        },
        mobile() {
            return this.$parent.$parent.mobile;
        }
    },
    mounted() {
        window.addEventListener('resize', this.resize);
    },
    template: `
        <div id="mobile-nav" :class="{ 'show-mobile-nav': openMobileNav }">
            <div id="menu-container" @click="toggleMobileNav()" :class="{ 'change': openMobileNav }">
                <div class="bar1"></div>
                <div class="bar2"></div>
                <div class="bar3"></div>
            </div>
            <div id="mobile-episode-info"
                class="red pointer" 
                @click="showEpisodeInfoModal()"
                v-if="!openMobileNav">
                {{ currentEpisode.number }} Info
            </div>
            <ul id="mobile-nav-episodes-list" v-if="openMobileNav">
                <li>{{ currentTime }}</li>
                <li>Now playing: Ep {{ currentEpisode.number  }}</li>
                <li class="red pointer" @click="showEpisodeInfoModal()">
                    See Ep {{ currentEpisode.number }} Info &lt;
                </li>
                <li>------</li>
                <li v-for="episode in episodes" :key="episode.id">
                    <a :href="'/' + episode.number">{{ episode.number }}- {{ episode.title }}</a>
                </li>
                <li>------</li>
                <li><span class="pointer" @click="showAboutModal()">About ITR</span></li>
                <li><a href="/archive">Archive</a></li>
                <li>------</li>
                <SubscriptionForm :mobile="mobile" />
            </ul>
        </div>
    `
}