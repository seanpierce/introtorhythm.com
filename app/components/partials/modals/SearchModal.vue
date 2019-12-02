<template>
    <div id="search-modal" class="modal" @click="hideModal($event)">
        <div class="content">
            <img @click="hideModal($event)" src="/assets/images/icons/close.svg" id="icon-close" />
            <div v-if="modalData">
                <h1>{{ modalData.data.length }} result{{ modalData.data.length !== 1 ? 's' : '' }} found for "{{ modalData.search }}"</h1>
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
    props: [
        'modalData'
    ],
    methods: {
        hideModal(event) {
            var target = event.target.id;
            console.log(target);
            if (target !== 'search-modal' && target !== 'icon-close') return;
            this.$parent.hideModal();
        }
    }
}
</script>