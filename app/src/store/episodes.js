const apiClient = require('@/utilities/apiClient')

const episodesStore = {

    state: () => ({
        episodes: [],
        selectedEpisode: null,
        nowPlaying: null,
        playing: false,
        audio: null,
        currentTime: null,
        duration: null,
        loading: false
    }),

    mutations: {

        SET_EPISODES: (state, episodes) => {
            state.episodes = episodes
        },

        SET_SELECTED_EPISODE: (state, episode) => {
            state.selectedEpisode = episode
        },

        SET_NOW_PLAYING: (state, episode) => {
            state.nowPlaying = episode
        },

        SET_EPISODE_PLAYING: (state, playing) => {
            state.playing = playing
        },

        SET_EPISODE_LOADING(state, loading) {
            state.loading = loading
        },

        SET_EPISODE_AUDIO(state, audio) {
            state.audio = audio
        },

        PAUSE_AUDIO: (state) => {
            state.audio?.pause()
        },

        PLAY_AUDIO: (state) => {
            state.audio.play()
        },

        SET_CURRENT_TIME: (state, input) => {
            state.audio.currentTime = input
        }
    },

    actions: {

        async getEpisodes({ commit }) {
            let response = await apiClient.get('episodes')
            commit('SET_EPISODES', response.data)
        },

        async toggleEpisodePlaying({ state, rootState, dispatch }, episode) {
            // Turn off live player, if playing
            if (rootState.live.playing) 
                dispatch('stopLiveAudio', null, { root: true })

            // Set passed-in episode to 'now playing'.
            // Condition is met when a new episode is invoked.
            if (state.nowPlaying?.number !== episode.number) 
                dispatch('setNowPlaying', episode)

            if (state.playing) {
                dispatch('pauseEpisodeAudio')
            } else {
                // If no audio, set audio, then play.
                if (!state.audio) {
                    let url = process.env.VUE_APP_MEDIA_URL + state.nowPlaying.audio
                    await dispatch('setEpisodeAudio', url)
                }
                // If audio, play audio.
                dispatch('playEpisodeAudio')
            }
        },

        setSelectedEpisode({ commit }, episode) {
            commit('SET_SELECTED_EPISODE', episode)
        },

        setNowPlaying({ commit, dispatch }, episode) {
            // pause, then remove current 'now playing'
            dispatch('pauseEpisodeAudio')
            commit('SET_EPISODE_AUDIO', null)
            // add the new 'now playing' episode
            commit('SET_NOW_PLAYING', episode)
        },


        async setEpisodeAudio({ commit, state }, url) {
            // Set initial loading states.
            console.log('Setting episode audio...')
            commit('SET_EPISODE_LOADING', true)

            // Create audio element.
            let audio = new Audio()
            audio.src = url
            audio.preload = 'metadata'
      
            // Indicates when the audio file is ready to be played.
            audio.addEventListener('loadeddata', function() {
                if (this.readyState >= 2) {
                    commit('SET_EPISODE_LOADING', false)
                    state.duration = audio.duration
                    return
                }
            })

            // Add time update events.
            audio.addEventListener('timeupdate', function() {
                state.currentTime = audio.currentTime
            })

            commit('SET_EPISODE_AUDIO', audio)
        },

        playEpisodeAudio({ commit }) {
            commit('SET_EPISODE_PLAYING', true)
            commit('PLAY_AUDIO')
        },
      
        pauseEpisodeAudio({ commit }) {
            commit('SET_EPISODE_PLAYING', false)
            commit('PAUSE_AUDIO')
        },

        unsetEpisodeAudio({ dispatch, commit }) {
            dispatch('pauseEpisodeAudio')
            commit('SET_EPISODE_AUDIO', null)
        },

        setCurrentTime({ commit }, input) {
            commit('SET_CURRENT_TIME', input)
        },

    }

}
  
export default episodesStore