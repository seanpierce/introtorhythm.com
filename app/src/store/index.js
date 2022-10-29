import Vue from 'vue'
import Vuex from 'vuex'
import chatStore from './chat'
import episodesStore from './episodes'
import liveStore from './live'
import contentStore from './content'
import scheduleStore from './schedule'

Vue.use(Vuex)

export default new Vuex.Store({
  root: true,

  modules: {
    chat: chatStore,
    episodes: episodesStore,
    live: liveStore,
    content: contentStore,
    schedule: scheduleStore
  },

  actions: {
    initialize({ dispatch }) {
      dispatch('getEpisodes')
      dispatch('getContentRefresh')
    },

    pollRefreshContent({ dispatch }) {
      dispatch('getContentRefresh')
    }
  },

})
