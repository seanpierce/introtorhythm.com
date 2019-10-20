<template>
    <div id="unsubscribe">
        <div class="content">
            <div v-if="!success">
                No longer want to receive notifications? Enter your email below to be removed from our list of subscribers.
                <input type="email" v-model="unsubscribeEmail" placeholder="email">
                <button @click="submit()">Submit</button>
            </div>
            <div v-if="success">You've been removed from our list of subscribers.</div>
            <br>
            <div><a href="/">Back to Intro To Rhythm</a></div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            unsubscribeEmail: null,
            success: false
        }
    },
    methods: {
        submit() {
            var payload = {
                email: this.unsubscribeEmail
            }

            axios.post('/api/unsubscribe/', payload)
            .then(() => {
                this.handleSuccess();
            })
            .catch(err => {
                console.log(err);
            })
        },
        handleSuccess() {
            this.success = true;
        }
    },
}
</script>

// const axios = require('axios');

// export var Unsubscribe = {
//     data() {
//         return {
//             unsubscribeEmail: null,
//             success: false
//         }
//     },
//     methods: {
//         submit() {
//             var payload = {
//                 email: this.unsubscribeEmail
//             }

//             axios.post('/api/unsubscribe/', payload)
//             .then(() => {
//                 this.handleSuccess();
//             })
//             .catch(err => {
//                 console.log(err);
//             })
//         },
//         handleSuccess() {
//             this.success = true;
//         }
//     },
//     computed: {
//     },
//     template: `
//         <div id="unsubscribe">
//             <div class="content">
//                 <div v-if="!success">
//                     No longer want to receive notifications? Enter your email below to be removed from our list of subscribers.
//                     <input type="email" v-model="unsubscribeEmail" placeholder="email">
//                     <button @click="submit()">Submit</button>
//                 </div>
//                 <div v-if="success">You've been removed from our list of subscribers.</div>
//                 <br>
//                 <div><a href="/">Back to Intro To Rhythm</a></div>
//             </div>
//         </div>
//     `
// }