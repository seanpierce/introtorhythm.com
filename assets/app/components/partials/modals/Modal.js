import { EpisodeInfo } from './EpisodeInfo.js';
import { About } from './About.js';

export var Modal = {
    components: {
        'EpisodeInfo': EpisodeInfo,
        'About': About
    },
    props : {
        type: String
    },
    data() {
        return {
        }
    },
    methods: {
        closeModal(event) {
            var target = event.target.id;
            if (target !== 'modal' && target !== 'close') return;

            if (this.type === "episodeInfo")
                this.$parent.showEpisodeInfoModal = false;

            if (this.type === "about")
                this.$parent.showAboutModal = false;
        }
    },
    computed: {
    },
    template: `
        <div id="modal" @click="closeModal($event)">
            <div class="modal-content">
                <img id="close" 
                    class="pointer" 
                    @click="closeModal($event)"
                    src="static/images/close.svg">
                <!-- content -->
                <EpisodeInfo v-if="type==='episodeInfo'" />
                <About v-if="type==='about'" />
            </div>
        </div>
    `
}