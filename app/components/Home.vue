<template>
    <div id="home">
        <div id="live" class="content">
            <div class="cover-filter"></div>
            <div class="show-info">
                <div class="title">Listen Live</div>
                <div class="show-time">{{ $root.localTime }}</div>
            </div>
            <div class="play-button" @click="play()">
                <img :src="playing ? '/assets/images/pause.png' : '/assets/images/play.png'" alt="">
            </div>
            <img src="/assets/images/itr-logo.png" class="logo" alt="">
        </div>
        <div id="recent-episodes-container" class="sub-content">
            <RecentEpisodes />
            <div>
                <img src="/assets/images/itr-text.png" class="itr-text">
            </div>
        </div>
    </div>
</template>

<script>
import RecentEpisodes from './partials/RecentEpisodes.vue';

export default {
    components: {
        RecentEpisodes
    },
    data() {
        return {
            time: 0,
            playing: false,
            audio: null,
            liveUrl: 'https://introtorhythm.com/stream'
        }
    },
    methods: {
        play() {
            if (this.audio.paused) {
                this.playing = true;
                this.audio.play();
            } else {
                this.playing = false;
                this.audio.pause();
            }
        },
        onError(vm) {
            console.log('audio error');
            vm.audio.remove();
            vm.audio = new Audio();
            vm.audio.src = vm.liveUrl;
            vm.audio.preload = 'metadata';
            vm.audio.addEventListener('timeupdate', vm.timeUpdate);
            vm.audio.play();
            vm.audio.onerror = function() {
                vm.onError(vm);
            }
        },
        getRecentEpisodes() {
            axios.get('/api/episodes/recent')
                .then(response => {
                    console.log(response);
                })
        }
    },
    mounted() {
        var vm = this;
        this.audio = new Audio();
        this.audio.src = this.liveUrl;
        this.audio.preload = 'metadata';
        this.audio.addEventListener('timeupdate', this.timeUpdate);

        this.audio.onerror = function() {
            vm.onError(vm);
        }

        // this.getRecentEpisodes();
    }
}
</script>