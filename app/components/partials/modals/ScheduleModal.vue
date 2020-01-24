<template>
    <div id="schedule-modal" class="modal" @click="hideModal($event)">
        <div class="content">
            <img @click="hideModal($event)" src="/assets/images/icons/close.svg" id="icon-close" />
            <div v-if="schedule">
                <h2>ITR Schedule</h2>
                <br>
                <div v-for="day in schedule" :key="day.id">
                    <strong>{{ day.name }}:</strong><br>
                    <ul class="show-schedule">
                        <li v-for="(show, index) in day.shows" :key="index">
                            {{ formatStartTime(show.start_time) }} - {{ show.title }}
                        </li>
                        <li v-if="day.shows.length === 0">All day - Selections from ITR resident DJs</li>
                    </ul>
                    <br>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: [
        'modalData'
    ],
    data() {
        return {
            schedule: null
        }
    },
    methods: {
        hideModal(event) {
            var target = event.target.id;
            if (target !== 'schedule-modal' && target !== 'icon-close') return;
            this.$parent.hideModal();
        },
        formatStartTime(start_time) {
            if (start_time < 12)
                return start_time + ' AM';

            if (start_time === 12)
                return '12 PM';

            return (start_time - 12) + ' PM'
        },
        formatSchedule(data) {
            var date = new Date();
            var day = date.getDay();
            var days = [
                {
                    id: 0,
                    name: 'Sunday',
                    shows: data.filter(x => x.day == 6)
                },
                {
                    id: 1,
                    name: 'Monday',
                    shows: data.filter(x => x.day == 0)
                },
                {
                    id: 2,
                    name: 'Tuesday',
                    shows: data.filter(x => x.day == 1)
                },
                {
                    id: 3,
                    name: 'Wednesday',
                    shows: data.filter(x => x.day == 2)
                },
                {
                    id: 4,
                    name: 'Thursday',
                    shows: data.filter(x => x.day == 3)
                },
                {
                    id: 5,
                    name: 'Friday',
                    shows: data.filter(x => x.day == 4)
                },
                {
                    id: 6,
                    name: 'Saturday',
                    shows: data.filter(x => x.day == 5)
                },
            ]
            var sortedDays = days.splice(day);
            sortedDays = sortedDays.concat(days.splice(day * -1));
            this.schedule = sortedDays;
        }
    },
    mounted() {
        if (this.$parent.schedule)
            this.formatSchedule(this.$parent.schedule);
    }
}
</script>