<template>
    <div id="footer" v-bind:class="{ 'absolute': position === 'absolute' }" class="clearfix">
        <ul>
            <li class="button" @click="$parent.modal = 'info'">Info</li>
        </ul>
    </div>
</template>

<script>
export default {
    props: {
        position: String
    }
}
</script>