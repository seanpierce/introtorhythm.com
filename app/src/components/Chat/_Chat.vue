<template>
    <div id="new-chat" class="content">

        <div 
            class="new-user"
            v-if="!chat.username">

            <div class="new-user-form">
                Please enter a username
                <input 
                    type="text" 
                    autofocus
                    @keyup.enter="setUser()"
                    v-model="newUser">
                <button @click="setUser()">Join</button>
            </div>
        </div>

        <div v-else>
            <div id="messages">
                <div class="message" v-for="(message, index) in chat.messages" :key="index">
                    <span class="time-stamp">{{ formatTime(message.time) }}</span> 
                    <span class="username" v-bind:class="{ 'me' : message.username === chat.username }">{{ message.username }}</span>:
                    <span class="message-content" v-html="message.message"></span>
                </div>
            </div>

            <div id="message-input">
                <input 
                    type="text" 
                    @keyup.enter="submit()"
                    v-model="message">

                <button @click="submit()">Submit</button>
            </div>
        </div>
    </div>
</template>

<script>
import moment from 'moment'
import { 
    insertMessage, 
    readMessages, 
    purgeOldMessages 
} from '@/database/queries'

export default {
    data() {
        return {
            message: null,
            user: null,
            newUser: null,
            errors: []
        }
    },
    
    computed: {
        chat() {
            return this.$store.state.chat || {}
        }
    },
    methods: {
        submit() {
            this.errors = []

            if (!this.message) return

            if (this.message.length > 140) {
                this.errors.push('Messages must be less than 140 characters')
                return
            }
            
            let payload = {
                username: this.chat.username,
                message: this.message,
                time: moment.utc().valueOf()
            }

            // dispatch message to store
            insertMessage(payload)
            this.message = null

            this.scrollToBottom()
        },

        getExistingUser() {
            let user = localStorage.getItem('ITR_USER')
            if (user)
                this.$store.dispatch('setUsername', user)
        },

        setUser() {
            this.errors = []

            if (!this.newUser) return

            if (this.newUser.length > 20) {
                this.errors.push('Username must be between 4 and 20 characters')
                return
            }
            
            this.$store.dispatch('setUsername', this.newUser)
            localStorage.setItem('ITR_USER', this.newUser)

            this.newUser = null
        },

        scrollToBottom() {
            let elem = document.getElementById('new-chat')

            let options = {
                left: 0,
                top: elem.scrollHeight,
                behavior: 'smooth'
            }

            elem.scrollTo(options)
        },

        formatTime(input) {
            return moment(input).format('hh:mm:ss')
        }
    },

    created() {
        this.getExistingUser()
        readMessages()
    },

    mounted() {
        purgeOldMessages()
        // scroll to bottom on initial view
        setTimeout(() => { 
            this.scrollToBottom()
        }, 500)
    }
}
</script>