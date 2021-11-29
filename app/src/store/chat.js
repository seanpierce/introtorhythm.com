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
        },

        LOGOUT_USER: (state) => {
            state.username = null
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

        async setUsername({ commit, state }, username) {
            commit('SET_USERNAME', username)

            let success = await addUser(username)
            if (success) {
                let payload = {
                    username: 'ITR',
                    message: `${username} has entered the chat`,
                    time: moment.utc().valueOf(),
                    itr: true
                }
    
                insertMessage(payload)
            }

            window.addEventListener('beforeunload', () => {
                if (state.users.some(u => u.username === username)) {
                    let payload = {
                        username: 'ITR',
                        message: `${username} has left the chat`,
                        time: moment.utc().valueOf(),
                        itr: true
                    }
    
                    removeUser(username)
                    insertMessage(payload)
                }
            })
        },

        setMessages({ commit }, messages) {
            commit('SET_MESSAGES', messages)
        },

        setUsers({ commit }, users) {
            commit('SET_USERS', users)
        },

        logoutUser({ commit }, username) {
            commit('LOGOUT_USER', username)
            removeUser(username)

            let payload = {
                username: 'ITR',
                message: `${username} has left the chat`,
                time: moment.utc().valueOf(),
                itr: true
            }

            insertMessage(payload)
        }
    }
}
  
  export default chatStore