<template>

</template>

<script>
export default {

}
</script>

// const axios = require('axios');

// export var Subscribe = {
//     template:`
//         <div id="subscription-form" class="content">
//             <p>Subscribe to ITR to receive updates regarding new episodes, live streaming schedule, or general news. You can <a href="/unsubscribe">unsubscribe</a> at any time.</p>
//             <br>
//             <div v-if="!success">
//                 <label for="email-input">Email Address</label>
//                 <input type="email"
//                     name="email-input" id="email-input"
//                     placeholder="email address"
//                     v-model="email">
//                 <input type="submit" value="Subscribe" @click="submit()">
//             </div>
//             <div v-if="success">
//                 Thanks! A confirmation email was sent to {{ email }}
//             </div>
//             <br>
//             <p class="subtext"><em>ITR will not share or distribute your email. Collected data is only used for subscription updates and notifications.</em></p>
//         </div>
//     `,
//     data() {
//         return {
//             email: null,
//             success: false,
//         }
//     },
//     methods: {
//         submit() {
//             var payload = {
//                 email: this.email
//             }

//             axios.post('/api/requests/', payload)
//                 .then(res => {
//                     this.handleSuccess(this.email);
//                     console.log(res);
//                 })
//                 .catch(err => {
//                     this.handleError(err);
//                 })
//         },
//         handleSuccess(email) {
//             this.success = true;
//         },
//         handleError(err) {
//             console.log(err);
//         }
//     },
//     computed: {
//     },
//     mounted() {
//     }
// }