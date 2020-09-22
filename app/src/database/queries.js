import db from './index'
import store from '@/store'

export const insertMessage = (payload) => {
    db.ref('messages').push({
        ...payload
    })
}

export const readMessages = () => {
    let ref = db.ref('messages')
    ref.on('value', (snapshot) => {
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

export const purgeOldMessages = () => {
    let ref = db.ref('messages')
    let now = Date.now();
    // 2 hours ago
    let cutoff = now - 2 * 60 * 60 * 1000;

    let old = ref.orderByChild('time')
        .endAt(cutoff)
        .limitToLast(1)

    old.on('child_added', snapshot => {
        snapshot.ref.remove()
    })
}