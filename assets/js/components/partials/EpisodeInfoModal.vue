<template>
    <div>
        <div id="info-modal" class="modal" v-if="loaded && show">
           <div class="modal-content">
                <img 
                    class="close pointer" 
                    src="assets/images/close.svg"
                    @click="hideInfoModal()">
                <div>{{ episodeHeadding }}</div>
                <div v-html="episodeInfo"></div>
                <div>------------</div>
                <br>
                <div>
                    Share this podcast on:<br>
                    facebook / twitter<br>
                    <br>
                    info@introtorhythm.com
                </div>
           </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {

        }
    },
    methods: {
        hideInfoModal() {
            this.$parent.showEpsisodeInfoModal = false;
        }
    },
    computed: {
        episodeInfo() {
            return this.$root.data.current_episode.content;
        },
        episodeHeadding() {
            return this.$root.data.current_episode.number 
                + '- '
                + this.$root.data.current_episode.title
        },
        loaded() {
            return this.$root.loaded;
        },
        show() {
            return this.$parent.showEpsisodeInfoModal;
        }
    },
    mounted() {
    }
}
</script>