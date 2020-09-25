<template>
    <div id="support-modal" 
        class="modal"
        @click="closeModal($event)">
        <div class="modal__content">
            <img :src="require('@/assets/images/close.svg')" class="modal__content__close">
            <br>
            <br>
            <p>This project is an entirely home-grown and DIY effort. While ITR is a labor of love, maintaining this application and it's server environments can be costly and time consuming. If you appreciate ITR and you have the means, please consider making a donation. Thanks!</p>
            <br>
            <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top"><input type="hidden" name="cmd" value="_s-xclick"> <input type="hidden" name="hosted_button_id" value="UT9UUF3R79DKC"> <input type="image" src="https://introtorhythm.com/static/images/donate.png" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button"> <img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1"></form>
        </div>
    </div>
</template>

<script>
export default {
    
    methods: {

        closeModal(event) {
            let elem = event.target
            if (elem.classList.contains('modal')
                || elem.classList.contains('modal__content__close'))
            
            return this.$parent.modal = null
        }
    }
}
</script>