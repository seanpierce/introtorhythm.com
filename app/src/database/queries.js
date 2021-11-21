import db from './index'
import store from '@/store'
import moment from 'moment'

/**
 * Inserts a message into the database.
 * @param {object} payload Object containing the message data:
 * username, timestamp, message content.
 */
export const insertMessage = (payload) => {
    db.ref('messages').push({
        ...payload
    })
}

/**
 * Reads the messages form the database.
 * Updates the value of the sotre when changes are detected.
 */
export const readMessages = () => {
    let ref = db.ref('messages')
    ref.on('value', snapshot => {
        try {
            if (snapshot.val())
                store.dispatch('setMessages', Object.values(snapshot.val()))
            else 
                store.dispatch('setMessages', [])
        } catch {
            store.dispatch('setMessages', [])
        }
    })
}

/**
 * Removes messages older than a configured amount of time.
 * @param {number} timeLimit Optional number (in hours) 
 * representing the time limit to keep messages.
 */
export const purgeOldMessages = (timeLimit = null) => {
    let ref = db.ref('messages')
    let now = moment.utc().valueOf()


    let cutoff = timeLimit ?
        // supplied timelimit (in hours)
        now - timeLimit * 60 * 60 * 1000 :
        // 6 hours ago
        now - 6 * 60 * 60 * 1000

    let old = ref.orderByChild('time')
        .endAt(cutoff)
        .limitToLast(1)

    old.on('child_added', snapshot => {
        snapshot.ref.remove()
    })
}

/**
 * Removes N number of old messages.
 * @param {number} numberOfMessages The number of messages to purge.
 */
export const deleteOldestXMessages = (numberOfMessages) => {
    let ref = db.ref('messages')
    let childCount = 0
    let updates = {}

    ref.on('value', snapshot => {
        snapshot.forEach(child => {
            if (++childCount < snapshot.numChildren() - numberOfMessages) {
                let key = child.key
                updates[key] = null
            }
        })
    })

    ref.update(updates)
}

/**
 * Adds a user to the database.
 * @param {string} username 
 */
export const addUser = username => {
    db.ref('users').push({ username: username })
}

/**
 * Removes a user from the database.
 * @param {string} username 
 */
export const removeUser = username => {
    db.ref('users').orderByChild('username')
        .equalTo(username).on("child_added", snapshot => {
        snapshot.ref.remove()
    })
}

/**
 * Inserts all users data in to the store.
 */
export const readUsers = () => {
    let ref = db.ref('users')
    ref.on('value', snapshot => {
        try {
            if (snapshot.val())
                store.dispatch('setUsers', Object.values(snapshot.val()))
            else 
                store.dispatch('setUsers', [])
        } catch {
            store.dispatch('setUsers', [])
        }
    })
}