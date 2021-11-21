import { deleteOldestXMessages } from '@/database/queries'

const chatStore = {
    state: () => ({
        showChat: false,
        users: [],
        username: null,
        messages: []
    }),

    mutations: {

        TOGGLE_CHAT: (state) => {
            state.showChat = !state.showChat
        },

        CHAT_OFF: (state) => {
            state.showChat = false
        },

        CHAT_ON: (state) => {
            state.showChat = true
        },

        SET_USERNAME: (state, username) => {
            state.username = username
        },

        SET_MESSAGES: (state, messages) => {
            // purge messages if too many
            if (messages.length > 200) {
                deleteOldestXMessages(50)
                console.log('REMOVING 300 MESSAGES')
                return
            }

            state.messages = messages
        }
    },

    actions: {

        toggleChat({ commit }) {
            commit('TOGGLE_CHAT')
        },

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
        }
    }
}
  
  export default chatStore