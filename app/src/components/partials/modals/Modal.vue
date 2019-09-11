<template>
    <div id="modal" @click="closeModal($event)">
        <div class="modal-content">
            <img id="close" 
                class="pointer" 
                @click="closeModal($event)"
                src="../../../assets/close.svg">
            <!-- content -->
            <EpisodeInfoModal />
        </div>
    </div>
</template>

<script>
/*eslint no-console: ["error", { allow: ["log"] }] */
import EpisodeInfoModal from './EpisodeInfoModal.vue';

export default {
    props : {
        type: String
    },
    components: {
        EpisodeInfoModal
    },
    methods: {
        closeModal(event) {
            var target = event.target.id;
            if (target !== 'modal' && target !== 'close') return;

            if (this.type === "episodeInfo")
                this.$parent.showEpisodeInfoModal = false;
        }
    }
}
</script>

<style>
#modal {
	width: 100%;
	height: 100%;
	position: fixed;
	top: 0;
	left: 0;
	background: rgba(0, 0, 0, 0.7);
	z-index: 15;
	overflow-y: scroll;
}
.modal-content {
	width: 96%;
	max-width: 900px;
	display: block;
	margin: 4em auto 8em auto;
	border: solid 1px white;
	padding: 2em;
	background: rgba(0, 0, 0, 0.5);
}
.modal-content * {
	color: white !important;
}
#close {
    height: 1.5em;
}
</style>