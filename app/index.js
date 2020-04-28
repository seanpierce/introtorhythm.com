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
        config: null,
        data: null
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
        getMVCData() {
            // Fetch the initial page data MVC style
            var elem = document.getElementById('mvcData');

            if (elem) {
                if (elem.attributes.mvcData.value)
                    this.data = JSON.parse(elem.attributes.mvcData.value);

                elem.parentNode.removeChild(elem);
            }
        },
    },
    computed: {
        page() {
            // If the MVC data is loaded and the page property is present 
            // on that object, return the page property.
            if (this.data && this.data.page)
                return this.data.page;
            else return null;
        }
    },
    mounted() {
        this.getMVCData();

        setInterval(() => {
            this.getLocalTime();
        }, 1000);

        this.loaded = true;
    },
    template: `
        <App />
    `
  })