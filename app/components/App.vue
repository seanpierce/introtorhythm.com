<template>
    <div>
        <Main v-if="showMain" />
        <Unsubscribe v-if="showUnsubscribe"/>
    </div>
</template>

<script>
import Main from './Main.vue';
import Unsubscribe from './Unsubscribe.vue';

export default {
    components: {
        Main,
        Unsubscribe
    },
    computed: {
        page() {
            return this.$parent.page;
        },
        showMain() {
            var mainPages = ['index', 'episodes', 'episode']
            return mainPages.indexOf(this.page) > -1;
        },
        showUnsubscribe() {
            return this.page === 'unsubscribe'
        }
    }
}
</script>