<template>
    <div id="chat" class="content">
        <div 
            class="new-user"
            v-if="!chat.username">

            <div class="new-user-form">
                Please enter a username
                <input 
                    type="text" 
                    autofocus
                    minlength="4"
                    maxlength="20"
                    @keyup.enter="setUser()"
                    v-model="newUser">
                <button @click="setUser()">Join</button>
            </div>
        </div>

        <div v-else>
            <div id="messages">
                <Message 
                    v-for="(message, index) in chat.messages" :key="index"
                    :message="message"
                    :myMessage="message.username === chat.username" />
            </div>

            <div id="message-input">
                <input 
                    type="text" 
                    maxlength="140"
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
    purgeOldMessages ,
    readUsers
} from '@/database/queries'
import Message from './Message'

export default {
    components: {
        Message
    },

    data() {
        return {
            message: null,
            user: null,
            newUser: null,
            errors: [],
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
            if (this.message.length > 140) return
            
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

            if (user) {
                if (user.length > 20) {
                    localStorage.removeItem('ITR_USER')
                    return
                }

                this.$store.dispatch('setUsername', user)
            }
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

            setTimeout(() => {
                this.scrollToBottom()
            }, 500)
        },

        scrollToBottom() {
            let elem = document.getElementById('chat')

            let options = {
                left: 0,
                top: elem.scrollHeight,
                behavior: 'smooth'
            }

            elem.scrollTo(options)
        }
    },

    created() {
        this.getExistingUser()
        readMessages()
        readUsers()
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