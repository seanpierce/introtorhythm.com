<template>
    <div id="nav">
        <div id="nav-top">
            Intro To Rhythm
        </div>

        <div id="nav-bottom">
            <router-link to="/"
                tag="span" 
                class="nav-tab"
                v-bind:class="{ active: route === 'Live' }">
                <span class="hide-on-mobile">Listen</span> Live
            </router-link>

            <span class="hide-on-desktop">/</span>

            <router-link to="/episodes"
                tag="span" 
                class="nav-tab"
                v-bind:class="{ active: route === 'Episodes' }">
                Episodes
            </router-link>

            <span class="hide-on-desktop">/</span>

            <router-link :to="'/episodes/' + selectedEpisodeNumber"
                v-if="route === 'Episode'" 
                tag="span" 
                class="nav-tab"
                v-bind:class="{ active: route === 'Episode' }">
                {{ selectedEpisodeNumber }}
            </router-link>

            <span class="hide-on-desktop" v-if="route === 'Episode'">/</span>

            <router-link :to="'/schedule'"
                tag="span" 
                class="nav-tab"
                v-bind:class="{ active: route === 'Schedule' }">
                Schedule
            </router-link>

            <span class="hide-on-desktop">/</span>

            <router-link to="/chat"
                tag="span" 
                class="nav-tab"
                v-bind:class="{ active: route === 'Chat' }">
                Chat
            </router-link>
        </div>

        <ChatNav v-if="route === 'Chat' && chat.username" />
    </div>
</template>

<script>
import ChatNav from '@/components/Chat/ChatNav'

export default {
    components: {
        ChatNav
    },

    computed: {
        route() {
            return this.$route.name
        },

        selectedEpisodeNumber() {
            return this.$store.state.episodes.selectedEpisode?.number
        },

        chat() {
            return this.$store.state.chat
        },
    }
}
</script>