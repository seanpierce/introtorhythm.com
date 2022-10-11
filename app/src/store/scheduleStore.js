// const apiClient = require('@/utilities/apiClient')

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
        getSchedule({ commit }) {
            // let response = await apiClient.get('episodes')
            // commit('SET_EPISODES', response.data)
            let shows = [
                {
                    id: 1,
                    title: 'Lost In The Club',
                    startTime: new Date()
                },
                {
                    id: 2,
                    title: 'BoomShakaLaka',
                    startTime: new Date()
                },
                {
                    id: 3,
                    title: 'Torn Fabric',
                    startTime: new Date()
                },
                {
                    id: 4,
                    title: 'Greg\'s House of Sound',
                    startTime: new Date()
                },
            ]
            
            commit('SET_SCHEDULE', shows)
        },
    }
}

export default scheduleStore