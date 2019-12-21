<template>
    <div>
        <div id="nav">
            <div class="top">
                <ul>
                    <li><a href="/">ITR-Live</a></li>
                    <li><a href="/episodes" class="desktop-nav-item">Episodes</a></li>
                    <li><span class="pointer desktop-nav-item" @click="showInfo()">Info</span></li>
                    <li><span class="pointer desktop-nav-item" @click="showModal('subscribe')">Subscribe</span></li>
                    <li id="mobile-trigger">
                        <span class="pointer" @click="toggleMobileNav()">
                            <svg class="header__menu-toggle__icon header__menu-toggle__icon--cross" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600">
                                <path d="M107,143H507v64H107Zm0,128H507v64H107Zm0,128H507v64H107Z" fill="#ffffff"></path>
                            </svg>
                        </span>
                    </li>
                </ul>
            </div>
            <div class="bottom">
                <input type="text" placeholder="Search" v-model="search" @keydown="checkSubmit($event)">
                <img src="/assets/images/icons/search-icon.svg" class="icon">
            </div>
        </div>
        <ul v-if="showMobileNav && smallScreen" id="mobile-nav">
            <li><img @click="toggleMobileNav()" src="/assets/images/icons/close-but-in-white.svg" id="icon-close" /></li>
            <li><a href="/">ITR-Live</a></li>
            <li><a href="/episodes">Episodes</a></li>
            <li><span class="pointer" @click="showInfo()">Info</span></li>
            <li><span class="pointer" @click="showModal('subscribe')">Subscribe</span></li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            search: null,
            showMobileNav: false,
            smallScreen: false
        }
    },
    methods: {
        toggleMobileNav() {
            if (this.showMobileNav) {
                this.showMobileNav = false;
                document.body.style.overflow = 'inherit';
            } else {
                this.showMobileNav = true;
                document.body.style.overflow = 'hidden';
            }
        },
        checkSubmit(event) {
            if (!this.search) return;
            if (event.key === 'Enter') this.submit();
        },
        submit() {
            axios.post('/api/episodes/search', { search: this.search })
                .then(response => {
                    this.showModal('search');
                    this.$parent.modalData = {
                        data: response.data,
                        search: this.search
                    }
                    this.search = null;
                })
        },
        showInfo() {
            axios.get('/api/content/info')
                .then(response => {
                    this.showModal('info');
                    this.$parent.modalData = response.data.info;
                })
        },
        showModal(name) {
            return this.$parent.showModal(name);
        },
        checkWindow() {
            if (window.innerWidth > 500 && this.smallScreen) {
                this.smallScreen = false;
                this.showMobileNav = false;
                document.body.style.overflow = 'inherit';
            }

            if (window.innerWidth <= 500 && !this.smallScreen)
                this.smallScreen = true;
        },
    },
    mounted() {
        if (window.innerWidth <= 500) this.smallScreen = true;
        window.addEventListener('resize', this.checkWindow);
    }
}
</script>