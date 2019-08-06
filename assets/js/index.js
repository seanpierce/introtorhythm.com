window.$ = window.jQuery = require('jquery');
require('bootstrap-sass');

import Vue from 'vue';
import Navigation from "./components/Navigation.vue";

window.Vue = Vue;
const app = new Vue({
    el: '#app',
    components: {
        Navigation
    }
});