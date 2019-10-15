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
        nums: null
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
            this.data = JSON.parse(elem.attributes.data.value);
            this.debug = elem.attributes.debug.value === 'true';
            this.nums = JSON.parse(elem.attributes.nums.value);
        }
    },
    template: `
        <App />
    `
  })