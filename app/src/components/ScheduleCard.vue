<template>
    <div class="schedule-card">
        {{ show.title }}
    </div>
</template>

<script>
export default {
    props: {
        show: {
            type: Object
        }
    }
}
</script>