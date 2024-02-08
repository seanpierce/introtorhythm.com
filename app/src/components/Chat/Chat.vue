<template>
<div id="chat">
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

            <div 
                class="helper" 
                v-bind:class="{ warning: newUserError }">
                Usernames may only contain letters, numbers, underscores, or hyphens
            </div>
        </div>
    </div>

    <div v-else id="chat-wrapper">
        <div id="messages">
            <Message 
                v-for="(message, index) in chat.messages" :key="index"
                :message="message"
                :myMessage="message.username === chat.username" />
        </div>

        <div id="message-input">
            <span></span>

            <input 
                type="text" 
                maxlength="140"
                @keyup.enter="submit()"
                v-model="message"
                placeholder="Say something">

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
    purgeOldMessages,
    purgeOldUsers,
    readUsers
} from '@/database/queries'
import Message from '@/components/Chat/Message'

export default {
    components: {
        Message
    },

    data() {
        return {
            message: null,
            messageStyle: {
                size: null,
                itallic: false,
                bold: false,
                color: null,
                font: null
            },
            user: null,
            newUser: null,
            newUserError: false
        }
    },
    
    computed: {
        chat() {
            return this.$store.state.chat || {}
        }
    },
    methods: {
        submit() {
            if (!this.message) return
            if (this.message.length > 140) return
            
            let payload = {
                username: this.chat.username,
                message: this.message,
                time: moment.utc().valueOf()
            }

            // dispatch message to store
            insertMessage(payload, true)
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
            this.newUserError = false

            if (!this.newUser) return
            if (this.newUser.length > 20) return

            if (!this.newUser.match(/^[0-9a-z-_]+$/i)) {
                this.newUserError = true
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
        purgeOldUsers()

        // scroll to bottom on initial view
        setTimeout(() => { 
            this.scrollToBottom()
        }, 500)
    }
}
</script>