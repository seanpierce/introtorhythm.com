<template>
    <div id="subscribe-modal" class="modal" @click="hideModal($event)">
        <div class="content">
            <img @click="hideModal($event)" src="/assets/images/icons/close.svg" id="icon-close" />
            <div>
                <p>Subscribe to ITR to receive updates regarding new episodes, live streaming schedule, or general news. You can <a href="mailto:introtorhythm@gmail.com?subject=Unsubscribe&body=Please remove this email address from your mail list.">unsubscribe</a> at any time.</p>
                <br>
                <div v-if="!success">
                    <label for="email-input">Email Address</label>
                    <input type="email"
                        name="email-input" id="email-input"
                        placeholder="email address"
                        v-model="email"
                        @keypress="checkForSubmit($event)">
                    <input type="submit" value="Subscribe" @click="submit()">
                </div>
                <div v-if="success">
                    Thanks! A confirmation email was sent to {{ email }}
                </div>
                <br>
                <p class="subtext"><em>ITR will neither share nor distribute your email. Collected data is only used for subscription updates and listener notifications.</em></p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: null,
            success: false,
        }
    },
    methods: {
        checkForSubmit(e) {
            var keyCode = e.keyCode || e.which;
            if (keyCode == '13') this.submit();
        },
        hideModal(event) {
            var target = event.target.id;
            if (target !== 'subscribe-modal' && target !== 'icon-close') return;
            this.$parent.hideModal();
        },
        submit() {
            var payload = {
                email: this.email
            }

            axios.post('/api/subscribers/request', payload)
                .then(res => {
                    this.handleSuccess(this.email);
                    console.log(res);
                })
                .catch(err => {
                    this.handleError(err);
                })
        },
        handleSuccess(email) {
            this.success = true;
        },
        handleError(err) {
            console.log(err);
        }
    }
}
</script>