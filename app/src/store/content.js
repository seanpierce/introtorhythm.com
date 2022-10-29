import moment from 'moment'
const apiClient = require('@/utilities/apiClient')

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

        async getBgImage({ commit, state }) {
            let response = await apiClient.get('content/backgroundimage')
            if (state.bgImage != response.data)
                commit('SET_BG_IMAGE', response.data)
        },

        async getInfoContent({ commit }) {
            let response = await apiClient.get('content/info')
            commit('SET_INFO_CONTENT', response.data)
        },

        async getContentRefresh({ commit, state }) { 
            let response = await apiClient.get('content/refresh')

            let bgImage = getBgImage(response.data)
            if (bgImage && state.bgImage != bgImage)
                commit('SET_BG_IMAGE', response.data)
            
            let marqueeText = getMarqueeText(response.data)
            if (marqueeText && state.marqueeText != marqueeText)
                commit('SET_MARQUEE_TEXT', marqueeText)
        }
    }
}

const getBgImage = responseData => { 
    if (responseData.now_playing && responseData.now_playing.show_image)
        return responseData.now_playing.show_image
    
    if (responseData.bg_image && responseData.bg_image.image && responseData.bg_image.active)
        return responseData.bg_image.image
    
    return null
}

const getMarqueeText = responseData => { 
    const divider = ' | '
    let text = ''

    let liveCallout = responseData.live_callout?.plain_text || null
    if (liveCallout)
        text += `${liveCallout}`

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
            let startTime = moment(show.start_time, 'h').format('hh:mm a')
            shows.push(`${show.title} at ${startTime}`)
        })

        text += shows.join(', ')
    }

    text += divider
    
    return text
}
  
export default contentStore