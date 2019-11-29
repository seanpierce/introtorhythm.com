<template>
    <div v-if="loaded" id="container">
        <Navigation />
        <InfoModal v-if="modal === 'info'" />
        <SearchModal v-if="modal === 'search'" 
            :modal-data="modalData" />
        <Live v-if="route === 'index'" />
        <Episodes v-if="route === 'episodes'" />
        <Episode v-if="route === 'episode'" />
    </div>
</template>

<script>
import Navigation from './partials/Navigation.vue';
import Live from './Live.vue';
import Episodes from './Episodes.vue';
import Episode from './Episode.vue';
import InfoModal from './partials/modals/InfoModal.vue';
import SearchModal from './partials/modals/SearchModal.vue';

export default {
    name: 'App',
    components: {
        Navigation,
        Live,
        Episodes,
        Episode,
        InfoModal,
        SearchModal
    },
    data() {
        return {
            modal: null,
            modalData: null,
            time: 0,
            playing: false,
            audio: null,
            liveUrl: 'https://introtorhythm.com/stream'
        }
    },
    methods: {
        showModal(name) {
            this.modal = name;
            document.body.style.overflow = 'hidden';
        },
        hideModal() {
            this.modal = null;
            document.body.style.overflow = 'inherit';
        },
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
    },
    computed: {
        route() {
            return this.$root.page;
        },
        loaded() {
            return this.$root.loaded;
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
    }
}
</script>