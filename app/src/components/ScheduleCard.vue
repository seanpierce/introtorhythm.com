<template>
    <div class="schedule-card">
        {{ show.title }}<br>
        <span class="show-date">{{ dayOfWeek }} {{ date }}, {{ startTime }} - {{ endTime }}</span>

        <div v-if="image">
            <img class="show-image" :src="image" :alt="show.title">
        </div>
    </div>
</template>

<script>
import moment from 'moment'
const mediaUrl = process.env.VUE_APP_MEDIA_URL
const dateTimeFormat = 'YYYY-MM-DD hh:mm:ss'
const dateFormat = 'MM/DD/YYYY'
const timeFormat = 'hh:mma'
const datOfWeekFormat = 'dddd'

export default {
    props: {
        show: {
            type: Object
        }
    },

    computed: {
        date() {
            return moment(this.show.start_date_time, dateTimeFormat).format(dateFormat)
        },

        startTime() {
            return moment(this.show.start_date_time, dateTimeFormat).format(timeFormat)
        },

        endTime() {
            return moment(this.show.end_date_time, dateTimeFormat).format(timeFormat)
        },

        dayOfWeek() {
            return moment(this.show.start_date_time, dateTimeFormat).format(datOfWeekFormat)
        },

        image() {
            if (!this.show.show_image)
                return null
            
            return `${mediaUrl}${this.show.show_image}`
        }
    }
}
</script>