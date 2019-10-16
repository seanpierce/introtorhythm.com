<template>
    <div v-if="loaded">
        <Home v-if="route === 'home'"/>
        <Archive v-if="route === 'archive'"/>
        <Unsubscribe v-if="route === 'unsubscribe'" />
    </div>
</template>

<script>
import Home from './Home.vue';
import Archive from './Archive.vue';
import Unsubscribe from './Unsubscribe.vue';

export default {
    name: 'App',
    components: {
        Home,
        Archive,
        Unsubscribe
    },
    computed: {
        route() {
            var path = window.location.pathname;
            switch (path) {
                case '/archive':
                    return 'archive';
                case '/unsubscribe':
                    return 'unsubscribe';
                default:
                    return 'home';
            }
        },
        loaded() {
            return this.$root.loaded;
        },
    }
}
</script>