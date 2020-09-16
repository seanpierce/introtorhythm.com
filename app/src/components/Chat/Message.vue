<template>
    <div class="chat-message">
        <span class="chat-message__time">{{ formatTime(message.time) }}</span>
        <span class="chat-message__username">
            <span v-bind:class="{ 'my-username' : usernameIsMine }">{{ message.username }}</span>:
        </span>
        <span class="chat-message__message">{{ message.message }}</span>
    </div>
</template>

<script>
export default {

    props: {
        message: Object
    },

    computed: {
        usernameIsMine() {
            try {
                return this.$store.state.chat.username == this.message.username
            } catch {
                return false
            }
        }

    },

    methods: {
        formatTime(timestamp) {
            let time = new Date(timestamp)

            let hours = this.pad(time.getHours() > 12 ? 
                time.getHours() - 12 : time.getHours(), 2)

            let minutes = this.pad(time.getMinutes(), 2)

            let period = time.getHours() > 12 ? 
                'am' : 'pm'

            return `${hours}:${minutes}${period}`
        },

        pad(num, size) {
            var s = num + '';
            while (s.length < size) s = '0' + s;
            return s;
        },
    }
}
</script>