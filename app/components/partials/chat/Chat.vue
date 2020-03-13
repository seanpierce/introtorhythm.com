<template>
    <div id="chat-wrapper">
        <div id="chat">
            <div id="chat-header">
                <span id="chat-close" @click="close()">x</span>
            </div>
            <div id="chat-enter-username" v-if="!username">
                Please enter a username:<br>
                <input type="text" maxlength="20" v-model="requestedUsername" @keyup.enter="setUsername">
                <span v-if="showUsernameExists" class="red">Username already exists</span>
            </div>
            <div id="chat-body" v-if="username">
                <div class="chat-message" v-for="(message, index) in messages" :key="index">
                    <span class="timestamp">[{{ getTime(message.timestamp) }}]</span> <span class="user" v-bind:class="{ highlight : message.username == username }">{{ message.username }}</span> - <span>{{ message.message }}</span>
                </div>
                <div v-if="!messages || messages.length == 0" class="end-of-messages">No one has said anything...</div>
                <div v-if="messages && messages.length > 0" class="end-of-messages">End of conversation</div>
            </div>
            <div id="chat-footer" v-if="username">
                <input type="text" v-model="message" @keyup.enter="submitMessage" placeholder="Say something">
            </div>
        </div>
    </div>
</template>

<script>
import firebase from 'firebase';

export default {
    data() {
        return {
            requestedUsername: null,
            showUsernameExists: false,
            username: null,
            message: null,
            messages: null,
        }
    },
    methods: {
        close() {
            this.$parent.toggleChat = false;
        },
        submitMessage() { 
            var message = {
                timestamp: Date.now(),
                username: this.username,
                message: this.message
            }
            firebase.database().ref('messages').push(message);
            this.message = null;
            this.$parent.scrollToChatBottom();
        },
        getTime(time) {
            var date = new Date(time);
            return date.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
        },
        checkForUsername() {
            var username = localStorage.getItem('chat-username');
            this.username = username || null;
        },
        setUsername() {
            this.showUsernameExists = false;
            var usernames = this.messages.map(x => x.username.toLowerCase());

            if (usernames.indexOf(this.requestedUsername.toLowerCase()) > -1) {
                this.showUsernameExists = true;
                return;
            }

            localStorage.setItem('chat-username', this.requestedUsername);
            this.username = this.requestedUsername;
        },
    },
    computed: {
        toggleChat() {
            return this.$parent.toggleChat;
        }
    },
    mounted() {
        let vm = this;
        vm.checkForUsername();

        // create and connect firebase chat
        var config = JSON.parse(atob(vm.$root.config));
        firebase.initializeApp(config);
        const ref = firebase.database().ref('messages');
        ref.on('value', snapshot => {
            let messages = [];
            let data = snapshot.val();

            if (data) {
                Object.keys(data)
                    .forEach(key => {
                        messages.push({
                            id: key,
                            username: data[key].username,
                            message: data[key].message,
                            timestamp: data[key].timestamp
                        });
                    });
                vm.messages = messages || [];
                var now = Date.now();
                var onHourAgo = now - 1 * 60 * 60 * 1000;
                var oldMessages = ref.orderByChild('timestamp').endAt(onHourAgo).limitToLast(1);
                oldMessages.on('child_added', snapshot => {
                    snapshot.ref.remove();
                });
            } else {
                vm.messages = [];
            }
        });
    }
}
</script>