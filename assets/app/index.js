import { App } from './App.js';

export const vue = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    components: {
        'App': App
    },
    data: {
        data: null,
        debug: null,
        mediaUrl: 'https://s3.amazonaws.com/podcasts.introtorhythm.com/media/'
    },
    computed: {
        loaded() {
            return this.data != null;
        }
    },
    mounted() {
        // Fetch the initial page data MVC style
        var elem = document.getElementById('data');
        var data = elem.attributes.data.value;
        var debug = elem.attributes.debug.value;
        this.data = JSON.parse(data);
        this.debug = debug === 'True';
    },
    template: `
        <App />
    `
  })