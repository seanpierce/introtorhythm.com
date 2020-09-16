import axios from 'axios'

const episodesStore = {

    state: () => ({
        episodes: [],
        selectedEpisode: null,
        playing: false
    }),

    mutations: {

        SET_EPISODES: (state, episodes) => {
            state.episodes = episodes
        },

        SET_SELECTED_EPISODE: (state, episode) => {
            state.selectedEpisode = episode
        },

        TOGGLE_EPISODE_PLAYING: (state) => {
            state.playing = !state.playing
        },
    },

    actions: {

        async getEpisodes({ commit }) {
            let response = await axios.get(process.env.VUE_APP_API_BASE_URL + 'episodes')
            commit('SET_EPISODES', response.data)
        },

        setSelectedEpisode({ commit }, episode) {
            commit('SET_SELECTED_EPISODE', episode)
        },

        toggleEpisodePlaying({ commit }) {
            commit('TOGGLE_EPISODE_PLAYING')
        }
    },
}
  
  export default episodesStore