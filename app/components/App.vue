<template>
    <div>
        <Main v-if="showMain" />
        <Unsubscribe v-if="showUnsubscribe" />
        <Archive v-if="showArchive" />
    </div>
</template>

<script>
import Main from './Main';
import Unsubscribe from './Unsubscribe';
import Archive from './Archive';

export default {
    components: {
        Main,
        Unsubscribe,
        Archive
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
        },
        showArchive() {
            return this.page === 'archive'
        }
    }
}
</script>