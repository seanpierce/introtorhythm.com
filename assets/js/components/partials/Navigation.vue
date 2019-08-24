<template>
    <div>
        <div id="nav" v-if="loaded">
            <ul>
                <li><a href="/">Intro To Rhythm</a><li>
                <li>------</li>
                <li>Now Playing: Ep {{ currentEpisode.number }}</li>
                <li id="tracktime">{{ currentTime }} / {{ totalTime }}</li>
                <li>
                    <span class="see-info pointer" @click="showEpsisodeInfoModal = true">
                        See Ep {{ currentEpisode.number }} Info &lt;
                    </span>
                </li>
                <li>------</li>
                <li 
                    v-for="episode in episodes" 
                    v-bind:key="episode.number">
                    <a :href="'/' + episode.number" v-bind:class="{ active: episode.number === currentEpisode.number }">
                        {{ episode.number }}- {{ episode.title }}
                    </a>
                </li>
                <li>------</li>
                <li>About ITR</li>
                <li><a href="/archive" target="_blank">Archive</a></li>
                <li>
                    <div id="subscription-form-wrapper">
                        <form id="subscription-form" @submit="createSubscriptionRequest($event)" v-if="!submittedRequestMessage">
                            <input type="email" name="subscriber-email" id="subscriber-email" placeholder="email address" />
                            <input type="submit" value="Subscribe">
                        </form>
                        <span v-if="submittedRequestMessage">{{ submittedRequestMessage }}</span>              
                    </div>
                </li>
            </ul>
        </div>
        <EpisodeInfoModal />
    </div>
</template>

<script>
import EpisodeInfoModal from './EpisodeInfoModal.vue';

export default {
    components: {
        EpisodeInfoModal
    },
    data() {
        return {
            submittedRequestMessage: null,
            showEpsisodeInfoModal: false
        }
    },
    methods: {
        createSubscriptionRequest(e) {
            e.preventDefault();
            // post to subscription request API
            // once complete remove form and update message
            this.submittedRequestMessage = 'Thanks!'
        }
    },
    computed: {
        episodes() {
            return this.$root.data.episodes;
        },
        currentEpisode() {
            return this.$root.data.current_episode;
        },
        loaded() {
            return this.$root.loaded;
        },
        currentTime() {
            return this.$root.currentTime;
        },
        totalTime() {
            return this.$root.totalTime;
        }
    },
    mounted() {
    }
}
</script>