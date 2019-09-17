import { App } from './App.js';

export const vue = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    components: {
        'App': App
    },
    data: {
        data: null,
        mediaUrl: 'https://s3.amazonaws.com/podcasts.introtorhythm.com/media/',
        staticUrl: 'static'
    },
    computed: {
        loaded() {
            return this.data != null;
        }
    },
    mounted() {
        // Fetch the initial page data MVC style
        var elem = document.getElementById('data');

        if (elem) {
            var data = elem.attributes.data.value;
            this.data = JSON.parse(data);
        }
    },
    template: `
        <App />
    `
  })