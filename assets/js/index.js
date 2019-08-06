window.$ = window.jQuery = require('jquery');
require('bootstrap-sass');

import Vue from 'vue';
import Navigation from "./components/Navigation.vue";

window.Vue = Vue;
const app = new Vue({
    el: '#app',
    components: {
        Navigation
    },
    data() {
        return {
            episodeList: null
        }
    },
    methods: {
    },
    mounted() {
        this.episodeList = JSON.parse(this.$el.attributes.episodes.value);
    }
});