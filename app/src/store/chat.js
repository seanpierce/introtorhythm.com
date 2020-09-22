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

        SET_USERNAME: (state, username) => {
            state.username = username
        },

        SET_MESSAGES: (state, messages) => {
            state.messages = messages
        }
    },

    actions: {

        toggleChat({ commit }) {
            commit('TOGGLE_CHAT')
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