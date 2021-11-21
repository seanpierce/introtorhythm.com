<template>
    <div id="nav">
        <div id="nav-top">
            Intro To Rhythm
        </div>

        <div id="nav-bottom">
            <router-link to="/"
                tag="span" 
                class="nav-tab"
                @click.native="chatOff()"
                v-bind:class="{ active: currentRoute === 'Live' }">
                Listen Live
            </router-link>

            <router-link to="/episodes"
                tag="span" 
                class="nav-tab"
                @click.native="chatOff()"
                v-bind:class="{ active: currentRoute === 'Episodes' }">
                Episodes
            </router-link>

            <router-link :to="'/episodes/' + selectedEpisodeNumber"
                v-if="currentRoute === 'Episode'" 
                tag="span" 
                class="nav-tab"
                @click.native="chatOff()"
                v-bind:class="{ active: currentRoute === 'Episode' }">
                {{ selectedEpisodeNumber }}
            </router-link>

            <span 
                class="nav-tab"
                v-bind:class="{ active: currentRoute === 'Chat' }"
                @click="chatOn()">
                Chat
            </span>
        </div>
<!-- 
        <span id="chat-button" 
            class="button" 
            v-if="!showChat"
            @click="chatOn()">Chat</span> -->
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {

    methods: {
        ...mapActions(['chatOff', 'chatOn'])
    },

    computed: {
        currentRoute() {
            if (this.showChat)
                return 'Chat'
            else
                return this.$route.name
        },

        showChat() {
            return this.$store.state.chat.showChat
        },

        selectedEpisodeNumber() {
            return this.$store.state.episodes.selectedEpisode?.number
        }
    }

}
</script>