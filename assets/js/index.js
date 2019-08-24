window.$ = window.jQuery = require('jquery');
require('bootstrap-sass');

import Vue from 'vue';
import Home from "./components/pages/Home.vue";
import Archive from "./components/pages/Archive.vue";

window.Vue = Vue;
const app = new Vue({
    el: '#app',
    components: {
        Home,
        Archive
    },
    data() {
        return {
            data: null,
            mediaUrl: 'https://s3.amazonaws.com/podcasts.introtorhythm.com/media/',
            audio: new Audio(),
            playState: false
        }
    },
    methods: {
        togglePlayState() {
            if (this.playState) {
                this.playState = false;
                this.audio.pause();
            } else {
                this.playState = true;
                this.audio.play();
            }
        },
        setStringToTime(string) {
            var sec_num = parseInt(string, 10);
            var hours   = Math.floor(sec_num / 3600);
            var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
            var seconds = sec_num - (hours * 3600) - (minutes * 60);
            if (hours   < 10) { hours   = "0" + hours; }
            if (minutes < 10) { minutes = "0" + minutes; }
            if (seconds < 10) { seconds = "0" + seconds; }
            return hours + ':' + minutes + ':' + seconds;
        }
    },
    computed: {
        loaded() {
            return this.data !== null
        },
        currentTime() {
            return '00:00:00'
        },
        totalTime() {
            return '00:00:00'
        },
    },
    mounted() {
        var data = this.$el.attributes.data.value
        this.data = JSON.parse(data)
    }
});