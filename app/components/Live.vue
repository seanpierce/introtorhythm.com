<template>
    <div>
        <div id="live" class="content">
            <div class="cover-filter"></div>
            <div class="show-info">
                <div class="title">Listen Live</div>
                <div class="show-time">{{ $root.localTime }}</div>
            </div>
            <div class="play-button" @click="play()">
                <img :src="playing ? '/assets/images/pause.png' : '/assets/images/play.png'" alt="">
            </div>
            <img src="/assets/images/itr-logo.png" class="logo" alt="">
        </div>
        <div id="recent-episodes-container" class="sub-content">
            <RecentEpisodes />
            <div>
                <img src="/assets/images/itr-text.png" class="itr-text">
            </div>
        </div>
    </div>
</template>

<script>
import RecentEpisodes from './partials/RecentEpisodes.vue';

export default {
    components: {
        RecentEpisodes
    },
    computed: {
        playing() {
            return this.$parent.playing;
        }
    }
}
</script>