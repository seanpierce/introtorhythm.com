<template>
    <div id="nav">
        <div class="top">
            <ul>
                <li><a href="/">ITR</a></li>
                <li><a href="/episodes">Episodes</a></li>
                <li><a href="/schedule">Schedule</a></li>
                <li><span class="pointer" @click="showModal('info')">Info</span></li>
                <li><span class="pointer">Subscribe</span></li>
            </ul>
        </div>
        <div class="bottom">
            <input type="text" placeholder="Search" v-model="search" @keydown="checkSubmit($event)">
            <img src="/assets/images/icons/search-icon.svg" class="icon">
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            search: null
        }
    },
    methods: {
        checkSubmit(event) {
            if (!this.search) return;
            if (event.key === 'Enter') this.submit();
        },
        submit() {
            axios.post('/api/episodes/search', { search: this.search })
                .then(response => {
                    this.showModal('search');
                    this.$parent.modalData = {
                        data: response.data,
                        search: this.search
                    }
                    this.search = null;
                })
        },
        showModal(name) {
            return this.$parent.showModal(name);
        }
    }
}
</script>