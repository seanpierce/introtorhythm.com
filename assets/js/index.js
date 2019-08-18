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
            data: null
        }
    },
    methods: {
    },
    computed: {
        loaded() {
            return this.data !== null
        }
    },
    mounted() {
        var data = this.$el.attributes.data.value
        this.data = JSON.parse(data)
    }
});