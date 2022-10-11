const apiClient = require('@/utilities/apiClient')

const scheduleStore = {

    state: () => ({
        shows: null
    }),

    mutations: {

        SET_SCHEDULE: (state, shows) => {
            state.shows = shows
        }
    },

    actions: {
        async getSchedule({ commit }) {
            let response = await apiClient.get('schedule')
            console.log(response.data)
            commit('SET_SCHEDULE', response.data)
        },
    }
}

export default scheduleStore