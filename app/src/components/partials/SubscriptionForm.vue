<template>
    <div id="subscription-form">
        <form @submit.prevent="submit()" v-if="!success">
            <label for="kjhasd73">Email Address</label>
            <input type="email" 
                name="kjhasd73" id="kjhasd73" 
                class="j8sdaslkj" 
                placeholder="email address"
                v-model="email">
            <label for="sldkf9jk">Name</label>
            <input type="text" 
                name="sldkf9jk" 
                id="sldkf9jk" 
                class="a9842jhmk" 
                placeholder="name"
                v-model="name">
            <label for="kajsdh">I am not a robot</label>
            <input type="checkbox" 
                name="kajsdh" 
                id="kajsdh" 
                class="aujs8787s" 
                v-model="human">
            <input type="submit" value="Subscribe">
        </form>
        <div v-if="success">
            Thanks! A confirmation email was sent to {{ confirmationEmail }}
        </div>
    </div>
</template>

<script>
/*eslint no-console: ["error", { allow: ["log"] }] */
import axios from 'axios';

export default {
    data() {
        return {
            email: null,
            name: null,
            human: false,
            success: false,
            confirmationEmail: null
        }
    },
    methods: {
        submit() {
            if (!this.formIsValid) {
                // show success to spam bots
                this.handleSuccess(this.email)
                return;
            }

            var payload = {
                email: this.email
            }

            axios.post('/api/requests/', payload)
                .then(res => {
                    if (res.data.data)
                        this.handleSuccess(this.email);
                    else 
                        this.handleError(res);
                })
                .catch(err => {
                    this.handleError(err);
                })
        },
        handleSuccess(email) {
            this.success = true;
            this.confirmationEmail = email;
        },
        handleError(err) {
            console.log(err);
        }
    },
    computed: {
        formIsValid() {
            // catch spam bots who've attempted to fill honeypot fields
            return !this.name && !this.human && (this.email !== null && this.email !== '');
        }
    }
}
</script>

<style>
#subscription-form {
    margin-top: 1em;
}
#subscription-form form label,
.a9842jhmk, 
.aujs8787s {
    display: none;
}
#subscription-form input {
    padding: 4px;
    font-size: 0.75em;
    margin-right: 0.75em;
}
#subscription-form input[type='submit'] {
    color: #222;
    border: solid 1px #222;
    background: white;
    border-radius: 0;
}
</style>