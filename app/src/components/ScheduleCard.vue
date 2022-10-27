<template>
    <div class="schedule-card">
        {{ show.title }}<br>
        <span class="show-date">{{ date }} at {{ startTime }}</span>

        <div v-if="image">
            <img class="show-image" :src="image" :alt="show.title">
        </div>
    </div>
</template>

<script>
import moment from 'moment'
const mediaUrl = process.env.VUE_APP_MEDIA_URL

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
        },

        image() {
            if (!this.show.show_image)
                return null
            
            return `${mediaUrl}${this.show.show_image}`
        }
    }
}
</script>