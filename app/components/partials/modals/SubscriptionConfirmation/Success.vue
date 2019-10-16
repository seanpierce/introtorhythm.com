<template>
    <div id="subscription-confirmation-modal" @click="closeConfirmationSuccess()">
        <div class="content">
            <h1>Thanks! Your email has beed added to our list of subscribers. Click anywhere to return to Intro To Rhythm.</h1>
            <img :src="$root.staticUrl + '/images/wrench.png'">
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        closeConfirmationSuccess() {
            this.$parent.showConfirmationSuccess = false;
        }
    },
}
</script>