<template>
    <div id="search-modal" class="modal">
        <div class="content">
            <span @click="$parent.hideModal()" class="pointer">&lt; Back</span>
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
}
</script>