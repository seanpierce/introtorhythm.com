import App from './components/App.vue';

export const app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    components: {
        'App': App
    },
    data: {
        loaded: false,
        localTime: '00:00:00',
        mediaUrl: 'https://s3.amazonaws.com/podcasts.introtorhythm.com/media/',
        data: null,
        page: null
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
            output += am ? ' AM' : ' PM'
            return output;
        },
        pad(num, size) {
            var s = num + '';
            while (s.length < size) s = '0' + s;
            return s;
        },
        getdata() {
            // Fetch the initial page data MVC style
            var elem = document.getElementById('data');

            if (elem) {
                if (elem.attributes.page.value)
                    this.page = elem.attributes.page.value;

                if (elem.attributes.data.value)
                    this.data = JSON.parse(elem.attributes.data.value);

                elem.parentNode.removeChild(elem);
            }
        },
    },
    computed: {
    },
    mounted() {
        this.getdata();

        setInterval(() => {
            this.getLocalTime();
        }, 1000);

        this.loaded = true;
    },
    template: `
        <App />
    `
  })