import Vue from 'vue'
import Vuex from 'vuex'
import chatStore from './chat'
import liveStore from './live'
import contentStore from './content'

Vue.use(Vuex)

export default new Vuex.Store({
  root: true,

  modules: {
    chat: chatStore,
    live: liveStore,
    content: contentStore,
  },

  actions: {
    initialize({ dispatch }) {
      dispatch('getInfoContent')
      dispatch('getContentRefresh')
    },

    pollRefreshContent({ dispatch }) {
      dispatch('getContentRefresh')
    }
  }
})
