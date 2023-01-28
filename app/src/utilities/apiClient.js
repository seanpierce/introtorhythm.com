import axios from 'axios'

const API = axios.create({
    baseURL: process.env.VUE_APP_API_BASE_URL
})

let get = async (url, payload) => {
    try {
        let response = await API.get(url, payload)
        return response
    } catch(err) {
        handleError(err)
    }
}

let post = async (url, payload) => {
    try {
        let response = await API.post(url, payload)
        return response
    } catch(err) {
        handleError(err)
    }
}

let put = async (url, payload) => {
    try {
        let response = await API.put(url, payload)
        return response
    } catch(err) {
        handleError(err)
    }
}

let del = async (url, payload) => {
    try {
        let response = await API.delete(url, payload)
        return response
    } catch(err) {
        handleError(err)
    }
}

let handleError = error => {
    console.error('Error seen by apiClient', error.response.status, error.response)
    throw error
}

export {
    get,
    post,
    put,
    del
}