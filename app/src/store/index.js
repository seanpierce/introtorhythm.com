import Vue from 'vue'
import Vuex from 'vuex'

import chatStore from './chat'
import episodesStore from './episodes'

Vue.use(Vuex)

export default new Vuex.Store({

  root: true,

  modules: {
    chat: chatStore,
    episodes: episodesStore
  },

  state: {
    live: {
      playing: false
    }
  },

  mutations: {

    TOGGLE_LIVE(state) {
      state.live.playing = !state.live.playing
    }
  },

  actions: {

    toggleLive({ commit }) {
      commit('TOGGLE_LIVE')
    },

    initialize() {
      this.dispatch('getEpisodes')
    }
  },

})
