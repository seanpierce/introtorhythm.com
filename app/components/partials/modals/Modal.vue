<template>
    <div id="modal" @click="closeModal($event)">
        <div class="modal-content">
            <img id="close"
                class="pointer"
                @click="closeModal($event)"
                :src="$root.staticUrl + '/images/close.svg'">
            <!-- content -->
            <EpisodeInfo v-if="type==='episodeInfo'" />
            <About v-if="type==='about'" />
            <Episodes v-if="type==='episodes'" />
            <Subscribe v-if="type==='subscribe'" />
        </div>
    </div>
</template>

<script>
import EpisodeInfo from './EpisodeInfo.vue';
import About from './About.vue';
import Episodes from './Episodes.vue';
import Subscribe from './Subscribe.vue';

export default {
    components: {
        EpisodeInfo,
        About,
        Episodes,
        Subscribe
    },
    props : {
        type: String
    },
    methods: {
        closeModal(event) {
            var target = event.target.id;
            if (target !== 'modal' && target !== 'close') return;

            if (this.type === "episodeInfo")
                this.$parent.showEpisodeInfoModal = false;

            if (this.type === "about")
                this.$parent.showAboutModal = false;

            if (this.type === "episodes")
                this.$parent.showEpisodesModal = false;

            if (this.type === "subscribe")
                this.$parent.showSubscribeModal = false;
        }
    },
}
</script>

// import { EpisodeInfo } from './EpisodeInfo.js';
// import { About } from './About.js';
// import { Episodes } from './Episodes.js';
// import { Subscribe } from './Subscribe.js';

// export var Modal = {
//     components: {
//         'EpisodeInfo': EpisodeInfo,
//         'About': About,
//         'Episodes': Episodes,
//         'Subscribe': Subscribe,
//     },
//     props : {
//         type: String
//     },
//     data() {
//         return {
//         }
//     },
//     methods: {
//         closeModal(event) {
//             var target = event.target.id;
//             if (target !== 'modal' && target !== 'close') return;

//             if (this.type === "episodeInfo")
//                 this.$parent.showEpisodeInfoModal = false;

//             if (this.type === "about")
//                 this.$parent.showAboutModal = false;

//             if (this.type === "episodes")
//                 this.$parent.showEpisodesModal = false;

//             if (this.type === "subscribe")
//                 this.$parent.showSubscribeModal = false;
//         }
//     },
//     computed: {
//     },
//     template: `
//         <div id="modal" @click="closeModal($event)">
//             <div class="modal-content">
//                 <img id="close"
//                     class="pointer"
//                     @click="closeModal($event)"
//                     :src="$root.staticUrl + '/images/close.svg'">
//                 <!-- content -->
//                 <EpisodeInfo v-if="type==='episodeInfo'" />
//                 <About v-if="type==='about'" />
//                 <Episodes v-if="type==='episodes'" />
//                 <Subscribe v-if="type==='subscribe'" />
//             </div>
//         </div>
//     `
// }