<template>
    <div id="info-modal" class="modal" @click="hideModal($event)">
        <div class="content">
            <img @click="hideModal($event)" src="/assets/images/icons/close.svg" id="icon-close" />
            <div v-if="modalData">
                <div v-html="modalData"></div>
                <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
                    <input type="hidden" name="cmd" value="_s-xclick" />
                    <input type="hidden" name="hosted_button_id" value="UT9UUF3R79DKC" />
                    <input type="image" src="https://introtorhythm.com/static/images/donate.png" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
                    <img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: [
        'modalData'
    ],
    methods: {
        hideModal(event) {
            var target = event.target.id;
            if (target !== 'info-modal' && target !== 'icon-close') return;
            this.$parent.hideModal();
        }
    }
}
</script>