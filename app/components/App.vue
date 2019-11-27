<template>
    <div v-if="loaded" id="container">
        <Navigation />
        <Home v-if="route === 'index'" />
    </div>
</template>

<script>
import Navigation from './partials/Navigation.vue';
import Home from './Home.vue';

export default {
    name: 'App',
    components: {
        Navigation,
        Home,
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