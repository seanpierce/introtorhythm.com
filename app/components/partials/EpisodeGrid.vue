<template>
    <div>
        <div v-for="episode in episodes"
            :key="episode.id"
            class="episode-container">
            <div class="episode-wrapper">
                <div class="episode"
                    :style="{ backgroundImage: 'url(' + $root.mediaUrl + episode.image + ')' }">
                    <div class="episode-content">
                        <div>{{ episode.number }}<br>{{ episode.title }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: [
        'episodes'
    ]
}
</script>