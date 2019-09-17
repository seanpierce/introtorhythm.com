import { App } from './components/App.js';

export const vue = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    components: {
        'App': App
    },
    data: {
        data: null,
        debug: null,
        mediaUrl: 'https://s3.amazonaws.com/podcasts.introtorhythm.com/media/',
    },
    computed: {
        loaded() {
            return this.data != null;
        },
        staticUrl() {
            return this.debug ? 'assets' : 'static'
        }
    },
    mounted() {
        // Fetch the initial page data MVC style
        var elem = document.getElementById('data');

        if (elem) {
            var data = elem.attributes.data.value;
            this.data = JSON.parse(data);
            this.debug = elem.attributes.debug.value === 'true';
        }
    },
    template: `
        <App />
    `
  })