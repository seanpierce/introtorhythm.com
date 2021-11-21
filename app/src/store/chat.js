import {
    addUser,
    deleteOldestXMessages,
    insertMessage,
    removeUser
} from '@/database/queries'
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
                message: `<em>${username}</em> has entered the chat`,
                time: moment.utc().valueOf(),
                itr: true
            }

            insertMessage(payload)
            addUser(username)

            window.addEventListener('beforeunload', () => {
                if (state.users.some(u => u.username === username)) {
                    let payload = {
                        username: 'ITR',
                        message: `<em>${username}</em> has left the chat`,
                        time: moment.utc().valueOf(),
                        itr: true
                    }
    
                    removeUser(username)
                    insertMessage(payload)
                }
            })
        },

        LOGOUT_USER: (state, username) => {
            state.username = null

            let payload = {
                username: 'ITR',
                message: `<em>${username}</em> has left the chat`,
                time: moment.utc().valueOf(),
                itr: true
            }

            removeUser(username)
            insertMessage(payload)
        },

        SET_MESSAGES: (state, messages) => {
            // purge messages if too many
            if (messages.length > 200)
                deleteOldestXMessages(100)

            state.messages = messages
        },

        SET_USERS: (state, users) => {
            state.users = users
        }
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

        setUsers({ commit }, users) {
            commit('SET_USERS', users)
        },

        logoutUser({ commit }, username) {
            commit('LOGOUT_USER', username)
        }
    }
}
  
  export default chatStore