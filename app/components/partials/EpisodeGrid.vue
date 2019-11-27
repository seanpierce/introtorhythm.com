<template>
    <div>
        <div v-for="episode in episodes"
            :key="episode.id"
            class="recent-episode-container">
            <div class="recent-episode-wrapper">
                <div class="recent-episode"
                    :style="{ backgroundImage: 'url(' + $root.mediaUrl + episode.image + ')' }">
                    <div class="recent-episode-content">
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