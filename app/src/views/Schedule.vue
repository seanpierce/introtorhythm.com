<template>
    <div id="schedule">
       <div v-if="schedule">
            <ScheduleCard 
                v-for="show in schedule"
                :key="show.id" 
                :show="show" />
       </div>
    </div>
</template>

<script>
import ScheduleCard from '@/components/ScheduleCard'

export default {
    components: {
        ScheduleCard
    },

    computed: {
        schedule() {
            return this.$store.state.schedule.shows?.shows || null
        },

        startDate() {
            return this.$store.state.schedule.shows?.startDate || null
        },

        endDate() {
            return this.$store.state.schedule.shows?.endDate || null
        },
    },

    mounted() {
        if (!this.schedule)
            this.$store.dispatch('getSchedule')
    }
}
</script>