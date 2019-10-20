<template>
    <div id="subscription-confirmation-modal" @click="closeConfirmationSuccess()">
        <div class="content">
            <h1>Oh no! We're unable to add your email to our subscription list. If you need help, reach out to introtorhythm@gmail.com. Click anywhere to return to Intro To Rhythm.</h1>
            <img :src="$root.staticUrl + '/images/wrench.png'">
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        closeConfirmationSuccess() {
            this.$parent.showConfirmationFailure = false;
        }
    },
}
</script>