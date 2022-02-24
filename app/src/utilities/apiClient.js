import axios from 'axios'

const baseUrl = process.env.VUE_APP_API_BASE_URL

let get = async (url, payload) => {
    try {
        let response = await axios.get(`${baseUrl}${url}`, payload)
        return response
    } catch(err) {
        handleError(err)
    }
}

let post = async (url, payload) => {
    try {
        let response = await axios.post(`${baseUrl}${url}`, payload)
        return response
    } catch(err) {
        handleError(err)
    }
}

let put = async (url, payload) => {
    try {
        let response = await axios.put(`${baseUrl}${url}`, payload)
        return response
    } catch(err) {
        handleError(err)
    }
}

let del = async (url, payload) => {
    try {
        let response = await axios.delete(`${baseUrl}${url}`, payload)
        return response
    } catch(err) {
        handleError(err)
    }
}

let handleError = error => {
    console.error('Error seen by apiClient', error.response.status, error.response)

    // unauthorized
    if (error.response.status === 401) {
        // Reload page if session times out attempting to call API.
        // The dashboard template will interpolate the redirect URL.
        // Take the user back to login.
        window.location.reload()
        return
    }

    throw error
}

export {
    get,
    post,
    put,
    del
}