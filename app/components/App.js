import { Home } from './Home.js';
import { Archive } from './Archive.js';
import { Unsubscribe } from './Unsubscribe.js';

export var App = {
    components: {
        'Home': Home,
        'Archive': Archive,
        'Unsubscribe': Unsubscribe
    },
    data() {
        return {
        }
    },
    methods: {
        test() {
            console.log('ok');
        }
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
    },
    template: `
        <div v-if="loaded">
            <Home v-if="route === 'home'"/>
            <Archive v-if="route === 'archive'"/>
            <Unsubscribe v-if="route === 'unsubscribe'" />
        </div>
    `
}