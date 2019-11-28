<template>
    <div v-if="loaded" id="container">
        <Navigation />
        <InfoModal v-if="modal === 'info'" />
        <SearchModal v-if="modal === 'search'" />
        <Home v-if="route === 'index'" />
    </div>
</template>

<script>
import Navigation from './partials/Navigation.vue';
import Home from './Home.vue';
import InfoModal from './partials/modals/InfoModal.vue';
import SearchModal from './partials/modals/SearchModal.vue';

export default {
    name: 'App',
    components: {
        Navigation,
        Home,
        InfoModal,
        SearchModal
    },
    data() {
        return {
            modal: null
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
        }
    },
    computed: {
        route() {
            return this.$root.page;
        },
        loaded() {
            return this.$root.loaded;
        }
    },
}
</script>