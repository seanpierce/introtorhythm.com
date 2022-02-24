const apiClient = require('@/utilities/apiClient')

const contentStore = {

    state: () => ({
        bgImage: null,
        infoContent: null
    }),

    mutations: {

        SET_BG_IMAGE(state, bgImage) {
            state.bgImage = bgImage
        },

        SET_INFO_CONTENT(state, info) {
            state.infoContent = info
        }
    },

    actions: {

        async getBgImage({ commit, state }) {
            let response = await apiClient.get('content/backgroundimage')
            if (state.bgImage != response.data)
                commit('SET_BG_IMAGE', response.data)
        },

        async getInfoContent({ commit }) {
            let response = await apiClient.get('content/info')
            commit('SET_INFO_CONTENT', response.data)
        }
    }
}
  
  export default contentStore