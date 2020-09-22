<template>
    <div id="footer" v-bind:class="{ 'absolute': position === 'absolute' }" class="clearfix">
        <ul>
            <li class="button">Info</li>
            <li class="button">Subscribe</li>
            <li class="button">Support</li>
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