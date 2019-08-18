<template>
    <div>
        <div id="info-modal" class="modal" v-if="loaded && show">
           <div class="modal-content">
                <div v-html="episodeInfo"></div>
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
    },
    computed: {
        episodeInfo() {
            return this.$root.data.current_episode.content;
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