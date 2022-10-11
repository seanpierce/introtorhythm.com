<template>
    <div id="schedule">
        <div id="schedule-wrapper">
            <h1>Schedule</h1>

            <h2>{{ startDate }} - {{ endDate }}</h2>

            <div 
                id="schedule-card-list"
                v-if="schedule">
                <ScheduleCard 
                    v-for="show in schedule"
                    :key="show.id" 
                    :show="show" />
            </div>
        </div>
    </div>
</template>

<script>
import moment from 'moment'
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
            let startDate = this.$store.state.schedule.shows?.startDate || null
            if (!startDate)
                return null
            else
                return moment(startDate, 'YYYY-MM-DD').format('MM/DD/YYYY')
        },

        endDate() {
            let endDate = this.$store.state.schedule.shows?.endDate || null
            if (!endDate)
                return null
            else
                return moment(endDate, 'YYYY-MM-DD').format('MM/DD/YYYY')
        },
    },

    mounted() {
        if (!this.schedule)
            this.$store.dispatch('getSchedule')
    }
}
</script>