<template>
    <div id="chat">
        <div id="chat-header">
            <span id="chat-close">x</span>
        </div>
        <div id="chat-body">
            <div class="chat-message" v-for="(message, index) in messages" :key="index">
                <span class="timestamp">[{{ message.time }}]</span> <span class="user">{{ message.user }}</span> - <span>{{ message.message }}</span>
            </div>
        </div>
        <div id="chat-footer">
            <input type="text" v-model="message" @keyup.enter="submitMessage" placeholder="Say something">
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: 'Sean',
            message: null,
            messages: [
                {
                    time: '10:00am',
                    user: 'Sean',
                    message: 'wow, this sucks'
                },
                {
                    time: '10:01am',
                    user: 'Lizi',
                    message: 'track ID? this is fire as hell'
                },
                {
                    time: '10:02am',
                    user: 'Charlie',
                    message: 'SOMEONE IS AT THE FRONT DOOR!!'
                },
                {
                    time: '10:02am',
                    user: 'Sean',
                    message: 'It\'s "Sutro" by Sean Pierce'
                },
            ]
        }
    },
    methods: {
        submitMessage() { 
            var message = {
                time: this.getTime(),
                user: this.user,
                message: this.message
            }
            this.messages.push(message);
            this.message = null;
        },
        getTime() {
            var time = new Date();
            return time.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
        },
    },
    computed: {
        toggleChat() {
            return this.$parent.toggleChat;
        }
    }
}
</script>