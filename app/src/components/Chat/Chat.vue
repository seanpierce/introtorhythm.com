<template>
    <div id="chat">

        <div id="chat-header">
            <span @click="toggleChat()" id="close-chat">
                <img :src="require('@/assets/images/close.svg')" alt="Close icon">
            </span>
        </div>

        <div id="chat-body">

            <div v-if="!chat.username" id="chat-enter-username">
                <div>
                    Enter your username to join in the chat
                </div>
                <input type="text" 
                    placeholder="username"
                    v-model="newUsername"
                    @keydown="keyDown($event, setNewUsername)">

                <div id="chat-errors" v-if="errors">
                    <span v-for="(error, index) in errors" :key="index" class="chat__error">{{ error }}. </span>
                </div>
            </div>

            <div id="chat-messages" v-if="chat.username">
                <Message v-for="(message, index) in chat.messages" :key="index"  :message="message" />
            </div>

            <div v-if="chat.username">
                <div id="chat-input">
                    <input type="text" 
                        placeholder="Say something"
                        v-model="message"
                        @keydown="keyDown($event, submit)">
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import { mapActions } from 'vuex'
import { insertMessage, readMessages, purgeOldMessages } from '@/database/queries'
import Message from './Message'

export default {

    components: {
        Message
    },
    
    data() {
        return {
            message: null,
            newUsername: null,
            errors: [],
            purgeData: null
        }
    },

    watch: {

        showChat() {
            if (this.showChat)
                this.scrollToBottom()
        }
    },

    computed: {

        chat() {
            return this.$store.state.chat || {}
        },

        showChat() {
            return this.chat.showChat
        },

        users() {
            let messages = this.chat?.messages

            if (messages) 
                return messages.map(x => x.username)
                    .filter((username, i, array) => array.indexOf(username) === i)
            else return []
        }
    },

    methods: {

        ...mapActions(['toggleChat']),

        submit() {
            if (this.messageIsNotValid(this.message)) return

            let payload = {
                username: this.chat.username,
                message: this.message,
                time: Date.now()
            }
            // dispatch message to store
            insertMessage(payload)
            this.message = null

            this.scrollToBottom()
        },

        scrollToBottom() {
            var elem = document.getElementById('chat-messages')

            if (!elem) return 

            var options = {
                left: 0,
                top: elem.scrollHeight,
                behavior: 'smooth'
            }

            elem.scrollTo(options);
        },

        keyDown(event, method) {
            if (event.key === 'Enter')
                method()
        },

        getUsernameFromSession() {
            sessionStorage.getItem('username') &&
                this.$store.dispatch('setUsername', sessionStorage.getItem('username'))
        },

        setNewUsername() {
            // validate
            if (this.usernameHasErrors(this.newUsername)) return

            // persist in store
            this.$store.dispatch('setUsername', this.newUsername)

            // persist in session
            sessionStorage.setItem('username', this.newUsername)

            // reset
            this.newUsername = null
        },

        usernameHasErrors(username) {
            this.errors = []

            if (!username) 
                this.errors.push('Username required')

            if (username.length < 2
                || username.length > 20)
                this.errors.push('Username must be between 2 and 20 characters')

            if (username.search(/^[a-zA-Z0-9-_]+$/) === -1)
                this.errors.push('Username can only contain letters, numbers, hyphens and undersocres')

            if (this.users.indexOf(username) > -1)
                this.errors.push('Username is already taken')

            return this.errors.length > 0
        },

        messageIsNotValid(message) {
            if (!message) return true

            if (message.length > 200) return true

            return false
        } 
    },

    created() {
        this.getUsernameFromSession()
        readMessages()

        // if not already purging, 
        // set purge to occur every 60 seconds
        if (!this.purgeData) {
            this.purgeData = setInterval(() => {
                purgeOldMessages()
            }, 60000)
        }
    },

    mounted() {
        // scroll to bottom on initial view
        setTimeout(() => { 
            this.scrollToBottom()
        }, 1000)
    }
}
</script>