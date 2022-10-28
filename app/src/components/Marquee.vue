<template>
    <div id="live-marquee" class="marquee">
        Coming Up - Chunt and Slart at 10pm PST to ruin YOUR night
    </div>
</template>

<script>
import nodeMarquee from 'node-marquee'

export default {
    mounted() {
        nodeMarquee({
            parent: '#live-marquee'
        })
    }
}
</script>