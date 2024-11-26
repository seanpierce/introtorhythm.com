const liveStore = {

    state: () => ({
        playing: false,
        audio: null,
        loading: false,
        volume: 0.8
    }),

    mutations: {

        TOGGLE_LIVE(state) {
            state.playing = !state.playing
        },
      
        SET_AUDIO(state, audio) {
            state.audio = audio
        },
      
        SET_LOADING(state, loading) {
            state.loading = loading
        },

        SET_VOLUME(state, volume) {
            const volumeValue = parseInt(volume) * 0.01;
            state.audio.volume = volumeValue;
            state.volume = volumeValue;
        }
    },

    actions: {
        setVolume({ commit }, volume) {
            commit('SET_VOLUME', volume)
        },

        toggleLive({ commit }) {
            commit('TOGGLE_LIVE')
        },

        async setLiveAudio({ commit, dispatch, state }, url) {
            console.log('Setting live audio...');

            commit('SET_LOADING', true);

            state.audio?.pause();
            let audio = new Audio();
            audio.volume = state.volume;
            audio.src = url;
            audio.preload = 'metadata';
      
            // indicates when the audio file is ready to be played
            audio.addEventListener('loadeddata', function() {
                if (this.readyState >= 2) {
                    commit('SET_LOADING', false)
                    return
                }
            })
      
            // reset audio on error
            audio.addEventListener('error', function() { 
                console.log('audio error', new Date())
                // set from true to false
                dispatch('toggleLive')
                dispatch('setLiveAudio', url)
                    .then(() => {
                        // set back to true
                        dispatch('toggleLive')
                    })
            })
      
            commit('SET_AUDIO', audio)
        },

        playLiveAudio({ state }) {
            state.audio.play()
            state.playing = true
        },
      
        stopLiveAudio({ commit, state }) {
            state.audio?.pause()
            state.playing = false
            commit('SET_AUDIO', null)
        }
    }
}
  
  export default liveStore