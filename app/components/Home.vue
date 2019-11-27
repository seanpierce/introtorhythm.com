<template>
    <div id="home">
        <Live />
    </div>
</template>

<script>
import Live from './Live.vue';

export default {
    components: {
        Live
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