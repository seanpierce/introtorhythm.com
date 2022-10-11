<template>
    <div class="schedule-card">
        {{ date }} at {{ startTime }} - {{ show.title }}
    </div>
</template>

<script>
import moment from 'moment'

export default {
    props: {
        show: {
            type: Object
        }
    },

    computed: {
        date() {
            return moment(this.show.date, 'YYYY-MM-DD').format('MM/DD/YYYY')
        },

        startTime() {
            return moment(this.show.start_time, 'h').format('hh:mm a')
        }
    }
}
</script>