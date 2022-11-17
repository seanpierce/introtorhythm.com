import moment from 'moment'
const apiClient = require('@/utilities/apiClient')
const dateTimeFormat = 'YYYY-MM-DD hh:mm:ss'
const timeFormat = 'hh:mma'

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
            let response = await apiClient.get('content/refresh')
            console.log('Content: ', response.data)

            let bgImage = getBgImage(response.data)
            if (bgImage && state.bgImage != bgImage)
                commit('SET_BG_IMAGE', bgImage)
            
            let marqueeText = getMarqueeText(response.data)
            if (marqueeText && state.marqueeText != marqueeText)
                commit('SET_MARQUEE_TEXT', marqueeText)
        }
    }
}

/**
 * Method used to parse content from the content-refresh API and
 * return the path to an image that will be rendered on the site.
 * Will return null if no background image is available, 
 * and the app will render the default.
 */
const getBgImage = responseData => {
    // Check to see if a specific bg image was set and is active
    if (responseData.bg_image?.active)
        return responseData.bg_image.image

    // Check to see if a there is a current show that is now playing
    // If so, use the show's associated image, if applicable
    if (responseData.now_playing && responseData.now_playing.show_image)
        return responseData.now_playing.show_image

    return null
}

/**
 * Method used to parse content from the content-refresh API and
 * concatenate a string of text used in the scrolling marquee
 * on the site.
 */
const getMarqueeText = responseData => { 
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
        
        text += 'Coming up next: '

        let shows = []
        responseData.schedule_today.forEach(show => { 
            let startTime = moment(show.start_date_time, dateTimeFormat).format(timeFormat)
            shows.push(`${show.title} at ${startTime}`)
        })

        text += shows.join(', ')
    }

    if (responseData.schedule_tomorrow.length > 0) { 
        if (text.length > 0)
            text += divider
        
        text += 'Tomorrow: '

        let shows = []
        responseData.schedule_tomorrow.forEach(show => { 
            let startTime = moment(show.start_date_time, dateTimeFormat).format(timeFormat)
            shows.push(`${show.title} at ${startTime}`)
        })

        text += shows.join(', ')
    }

    text += divider
    
    return text
}
  
export default contentStore