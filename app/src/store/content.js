import moment from 'moment'
const apiClient = require('@/utilities/apiClient')
const originalDateTimeFormat = 'YYYY-MM-DD hh:mm:ss'
const newTimeFormat = 'hh:mma'
const newDateTimeFormat = 'MM/DD hh:mma'

const contentStore = {

    state: () => ({
        bgImage: null,
        infoContent: null,
        marqueeText: null
    }),

    mutations: {

        SET_BG_IMAGE(state, bgImage) {
            state.bgImage = bgImage
        },

        SET_INFO_CONTENT(state, info) {
            state.infoContent = info
        },

        SET_MARQUEE_TEXT(state, text) { 
            state.marqueeText = text
        }
    },

    actions: {
        async getInfoContent({ commit }) {
            let response = await apiClient.get('content/info')
            commit('SET_INFO_CONTENT', response.data?.info)
        },

        /**
         * Method used to refresh live data rendered on the site.
         * Is called in an interval from the front-end app.
         */
        async getContentRefresh({ commit, state }) { 
            const response = await apiClient.get('content/refresh')
            
            const marqueeText = getMarqueeText(response.data)
            if (marqueeText && state.marqueeText != marqueeText)
                commit('SET_MARQUEE_TEXT', marqueeText)
        }
    }
}

/**
 * Method used to parse content from the content-refresh API and
 * concatenate a string of text used in the scrolling marquee
 * on the site.
 */
const getMarqueeText = responseData => { 
    console.log(responseData)
    const divider = ' | '
    let text = ''

    if (responseData.live_callout?.active && responseData.live_callout?.content)
        text += `${responseData.live_callout.content}`

    let nowPlaying = responseData.now_playing?.title || null
    if (nowPlaying) { 
        if (text.length > 0)
            text += divider
        
        text += `Now Playing - ${nowPlaying}`
    }

    if (responseData.schedule_today.length > 0) { 
        if (text.length > 0)
            text += divider
        
        text += 'Next: '

        let shows = []
        responseData.schedule_today.forEach(show => { 
            let startTime = moment(show.start_date_time, originalDateTimeFormat).format(newTimeFormat)
            shows.push(`${show.title} ${startTime}`)
        })

        text += shows.join(', ')
    }

    if (responseData.schedule_upcoming.length > 0) { 
        if (text.length > 0)
            text += divider
        
        text += 'Coming up: '

        let shows = []
        responseData.schedule_upcoming.forEach(show => { 
            let startTime = moment(show.start_date_time, originalDateTimeFormat).format(newDateTimeFormat)
            shows.push(`${show.title} ${startTime}`)
        })

        text += shows.join(', ')
    }

    text += divider
    
    return text
}
  
export default contentStore