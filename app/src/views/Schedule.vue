<template>
    <div id="schedule">
       
    </div>
</template>

<script>
export default {
    computed: {
        schedule() {
            return this.$store.state.schedule.shows || null
        }
    },

    mounted() {
        if (!this.schedule)
            this.$store.dispatch('getSchedule')
    }
}
</script>