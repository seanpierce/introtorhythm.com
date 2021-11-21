import axios from 'axios'

const contentStore = {

    state: () => ({
        bgImage: null
    }),

    mutations: {

        SET_BG_IMAGE(state, bgImage) {
            state.bgImage = bgImage
        }
    },

    actions: {

        async getBgImage({ commit, state }) {
            let response = await axios.get(process.env.VUE_APP_API_BASE_URL + 'content/backgroundimage')
            if (state.bgImage != response.data)
                commit('SET_BG_IMAGE', response.data)
        }
    }
}
  
  export default contentStore