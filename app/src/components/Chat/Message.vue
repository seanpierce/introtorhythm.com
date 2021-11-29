<template>
    <div 
        class="message"
        v-bind:class="{ 'itr' : message.itr }">
        <span class="time-stamp">
            {{ formatTime(message.time) }}
        </span> 
        <span 
            class="username" 
            v-bind:class="{ 'me' : myMessage }">
            {{ message.username }}
        </span>:
        <span class="message-content">
            {{ message.message }}
        </span>
    </div>
</template>

<script>
import moment from 'moment'

export default {
    props: {
        message: {
            type: Object
        },
        myMessage: {
            type: Boolean,
            default: false
        }
    },

    methods: {
        formatTime(input) {
            return moment(input).format('hh:mm:ss')
        }
    }
}
</script>