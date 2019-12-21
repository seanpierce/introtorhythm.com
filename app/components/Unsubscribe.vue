<template>
    <div id="unsubscribe">
        <h1>Unsubscribe</h1>
        <div id="wrapper">
            <div id="form" v-if="!success">
                <div>Enter your email below to remove yourself from our mailing list.</div>
                <input type="email" placeholder="your@email.com" v-model="email" @keypress="enterSubmit($event)"/>
                <button @click="submit()">Submit</button>
            </div>
            <div v-if="submitted" v-html="message"></div>
        </div>
        <div><a href="/">Return to ITR</a></div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: null,
            submitted: false,
            success: false,
            message: null
        }
    },
    methods: {
        enterSubmit(e) {
            if (e.keyCode == 13) return this.submit();
        },
        submit() {
            this.message = null;
            if (!this.validEmail) return;
            axios.post('/api/subscribers/unsubscribe', { email: this.email })
                .then(response => {
                    this.submitted = true;
                    if (response.data) this.showSuccess();
                    else this.showFailure();
                })
        },
        showSuccess() {
            this.success = true;
            this.message = 'Thanks! Your email address has been removed from our subscription list.';
        },
        showFailure() {
            this.message = 'Oops - something went wrong attempting to remove <strong>' + this.email + '</strong> from our list of subscribers. Please try again, or email <a href="mailto:introtorhythm@gmail.com?subject=Unsubscribe&body=Please remove this email address from your mail list.">introtorhtyhm@gmail.com</a>.';
            this.email = null;
        }
    },
    computed: {
        validEmail() {
            if (!this.email) return false;
            if (this.email.indexOf('@') === -1) return false;
            if (this.email.indexOf('.') === -1) return false;
            if (this.email.indexOf(' ') > -1) return false;
            return true;
        }
    }
}
</script>