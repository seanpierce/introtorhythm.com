<template>
    <div id="booking">
        <div v-if="success"
            id="booking-success">
            Thanks! We'll be in touch.
        </div>

        <div v-else
            id="booking-form">
            If you're interested in booking a show on Intro To Rhythm please fill out the form below. Due to the amount of requests received we cannot guarantee a reply to each submission.

            <br>
            <br>

            <div class="input-group">
                <div class="col100">
                    <label for="booking.name">Name</label>
                    <input 
                        type="text" 
                        id="booking.name" 
                        ref="name" 
                        v-model="name"
                        maxlength="100" />
                    <span class="text-area-count">{{ name ? name.length : 0 }}/100</span>
                </div>
            </div>

            <div class="input-group">
                <div class="col100">
                    <label for="booking.djName">DJ/ Artist Name</label>
                    <input 
                        type="text" 
                        id="booking.djName" 
                        v-model="djName"
                        maxlength="100" />
                    <span class="text-area-count">{{ djName ? djName.length : 0 }}/100</span>
                </div>
            </div>

            <div class="input-group">
                <div class="col100">
                    <label for="booking.email">Email</label>
                    <input 
                        type="text" 
                        id="booking.email" 
                        v-model="email"
                        maxlength="100" />
                    <span class="text-area-count">{{ email ? email.length : 0 }}/100</span>
                </div>
            </div>

            <div class="input-group">
                <div class="col100">
                    <label for="proposal">Tell us about yourself/ your music/ your show proposal</label>
                    <textarea 
                        id="booking.proposal" 
                        v-model="proposal" 
                        maxlength="300">
                    </textarea>
                    <span class="text-area-count">{{ proposal ? proposal.length : 0 }}/300</span>
                </div>
            </div>

            <div class="input-group">
                <div class="col100">
                    <label for="additional">Anything else you'd like us to know? Links, socials, etc.</label>
                    <textarea 
                        id="booking.additional" 
                        v-model="additional" 
                        maxlength="300">
                    </textarea>
                    <span class="text-area-count">{{ additional ? additional.length : 0 }}/300</span>
                </div>
            </div>

            <div class="input-group">
                <label class="checkbox-container"> Are you down?
                    <input type="checkbox" v-model="down">
                    <span class="checkmark"></span>
                </label>
            </div>

            <div class="errors" v-if="errors.length">
                {{ formatErrors(errors) }}
            </div>

            <div class="input-group">
                <div class="col100">
                    <button @click="submit()">Submit</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
const apiClient = require('@/utilities/apiClient')

export default {
    data() {
        return {
            success: false,
            name: null,
            djName: null,
            email: null,
            proposal: null,
            additional: null,
            down: false,
            errors: []
        }
    },

    methods: {
        async submit() {
            if (!this.validate())
                return

            const payload = {
                name: this.name,
                djName: this.djName,
                email: this.email,
                proposal: this.proposal,
                additional: this.additional
            }

            let response = await apiClient.post('contact/booking', payload)
            console.log(response.data)

            this.success = true

            window.scrollTo({
                top: 0,
                left: 0,
                behavior: 'smooth'
            })
        },

        validate() {
            this.errors = []

            if (!this.name)
                this.errors.push('name is required')

            if (!this.djName)
                this.errors.push('DJ/ artist name is required')

            if (!this.email)
                this.errors.push('email is required')

            if (!this.proposal)
                this.errors.push('show proposal is required')

            if (!this.down)
                this.errors.push('you must be down to submit the form')

            return this.errors.length === 0
        },

        formatErrors(errors) {
            errors = errors.join(', ')
            return errors[0].toUpperCase() + errors.substring(1) + '.'
        }
    },

    mounted() {
        this.$refs.name.focus()
    }
}
</script>