import App from './components/App.vue';

export const app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    components: {
        'App': App
    },
    data: {
        page: null,
        loaded: false,
        localTime: '00:00:00'
    },
    methods: {
        getLocalTime() {
            var date = new Date();
            this.localTime = this.printTime(date);
        },
        printTime(date) {
            var output = '';
            var am = date.getHours() < 12;
            output += am ? this.pad(date.getHours(), 2) + ':' :
                this.pad((date.getHours() === 12 ? date.getHours() : date.getHours() - 12), 2) + ':'
            output +=  this.pad(date.getMinutes(), 2) + ':';
            output += this.pad(date.getSeconds(), 2);
            return output;
        },
        pad(num, size) {
            var s = num + '';
            while (s.length < size) s = '0' + s;
            return s;
        },
    },
    computed: {
    },
    mounted() {
        // Fetch the initial page data MVC style
        var elem = document.getElementById('data');

        if (elem) {
            if (elem.attributes.page.value)
                this.page = elem.attributes.page.value;
        }

        setInterval(() => {
            this.getLocalTime();
        }, 1000);

        this.loaded = true;
    },
    template: `
        <App />
    `
  })