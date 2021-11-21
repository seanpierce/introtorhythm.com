import { deleteOldestXMessages, insertMessage } from '@/database/queries'
import moment from 'moment'

const chatStore = {
    state: () => ({
        showChat: false,
        users: [],
        username: null,
        messages: []
    }),

    mutations: {
        CHAT_OFF: (state) => {
            state.showChat = false
        },

        CHAT_ON: (state) => {
            state.showChat = true
        },

        SET_USERNAME: (state, username) => {
            state.username = username

            let payload = {
                username: 'ITR',
                message: `${username} has entered the chat`,
                time: moment.utc().valueOf(),
                itr: true
            }

            insertMessage(payload)

            window.addEventListener('beforeunload', () => {
                let payload = {
                    username: 'ITR',
                    message: `${username} has left the chat`,
                    time: moment.utc().valueOf(),
                    itr: true
                }

                insertMessage(payload)
            })
        },

        SET_MESSAGES: (state, messages) => {
            // purge messages if too many
            if (messages.length > 200) {
                deleteOldestXMessages(50)
                console.log('REMOVING 300 MESSAGES')
                return
            }

            state.messages = messages
        },

        ADD_USER: (state, username) => {
            state.users.push(username)
            // username has entered the chat
        },

        REMOVE_USER: (state, username) => {
            state.users.splice(state.users.indexOf(username), 1)
            // username has left the chat
        },
    },

    actions: {
        chatOff({ commit }) {
            commit('CHAT_OFF')
        },

        chatOn({ commit }) {
            commit('CHAT_ON')
        },

        setUsername({ commit }, username) {
            commit('SET_USERNAME', username)
        },

        setMessages({ commit }, messages) {
            commit('SET_MESSAGES', messages)
        },

        addUser({ commit }, username) {
            commit('ADD_USER', username)
        },

        removeUser({ commit }, username) {
            commit('REMOVE_USER', username)
        }
    }
}
  
  export default chatStore