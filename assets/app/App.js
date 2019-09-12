import { Home } from './components/Home.js';
import { Archive } from './components/Archive.js';

export var App = {
    components: {
        'Home': Home,
        'Archive': Archive
    },
    data() {
        return {
        }
    },
    methods: {
    },
    computed: {
        route() {
            var path = window.location.pathname;
            switch (path) {
                case '/archive':
                    return 'archive';
                default:
                    return 'home';
            }
        },
        loaded() {
            return this.$root.loaded;
        },
    },
    template: `
        <div v-if="loaded">
            <Home v-if="route === 'home'"/>
            <Archive v-if="route === 'archive'"/>
        </div>
    `
}