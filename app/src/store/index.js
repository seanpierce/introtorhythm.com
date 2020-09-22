import Vue from 'vue'
import Vuex from 'vuex'

import chatStore from './chat'
import episodesStore from './episodes'
import liveStore from './live'

Vue.use(Vuex)

export default new Vuex.Store({

  root: true,

  modules: {
    chat: chatStore,
    episodes: episodesStore,
    live: liveStore
  },

  state: {

  },

  mutations: {

  },

  actions: {

    initialize({ dispatch }) {
      dispatch('getEpisodes')
    }
  },

})
