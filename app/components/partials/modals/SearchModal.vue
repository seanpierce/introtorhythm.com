<template>
    <div id="search-modal" class="modal" @click="hideModal($event)">
        <div class="content">
            <img @click="hideModal($event)" src="/assets/images/icons/close.svg" id="icon-close" />
            <div v-if="modalData">
                <h1 v-if="!tagSearch">{{ modalData.data.length }} result{{ modalData.data.length !== 1 ? 's' : '' }} found for "{{ modalData.search }}"</h1>
                <h1 v-if="tagSearch">{{ modalData.data.length }} episode{{ modalData.data.length !== 1 ? 's' : '' }} tagged "{{ modalData.tag }}"</h1>
                <ul v-if="modalData.data.length > 0">
                    <li v-for="result in modalData.data" :key="result.id">
                        <a :href="'/episodes/' + result.number">{{ result.number }}- {{ result.title }}</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        modalData: Object,
        tagSearch: {
            type: Boolean,
            default: false
        }
    },
    methods: {
        hideModal(event) {
            var target = event.target.id;
            if (target !== 'search-modal' && target !== 'icon-close') return;
            this.$parent.hideModal();
        }
    }
}
</script>