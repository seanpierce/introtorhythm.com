<template>
    <div id="recent-episodes">

    </div>
</template>

<script>
export default {
    data() {
        return {
            recentEpisodes: null
        }
    },
    methods: {
        getRecentEpisodes() {
            axios.get('/api/episodes/recent')
                .then(response => {
                    console.log(response);
                })
        }
    },
    mounted() {
        // this.getRecentEpisodes();
    }
}
</script>