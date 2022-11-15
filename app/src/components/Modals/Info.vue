<template>
    <div id="info-modal" 
        class="modal"
        @click="closeModal($event)">
        <div class="modal__content">
            <img :src="require('@/assets/images/close.svg')" class="modal__content__close">
            <br>
            <br>
            
            <div v-html="content"></div>
            <br>

            <br>
            <form action="https://www.paypal.com/donate" method="post" target="_top">
                <input type="hidden" name="hosted_button_id" value="WUK6JYHURH6KJ" />
                <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
                <img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
            </form>
        </div>
    </div>
</template>

<script>
export default {

    computed: {

        content() {
            return this.$store.state.content.infoContent
        }
    },
    
    methods: {

        closeModal(event) {
            let elem = event.target
            if (elem.classList.contains('modal')
                || elem.classList.contains('modal__content__close'))
            
            return this.$parent.modal = null
        }
    },

    mounted() {
        this.$store.dispatch('getInfoContent')
    }
}
</script>