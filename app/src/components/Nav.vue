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

        <div
            v-if="showChat && username" 
            id="chat-details">
            {{ chat.users.length === 1 ? 'it\s just you bro' : chat.users.length + ' active users'  }} | 
            username: <span class="username me">{{ this.chat.username }}</span> | 
            <span 
                class="logout"
                @click="logout()">
                Log out
            </span>
        </div>
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

        chat() {
            return this.$store.state.chat
        },

        username() {
            return this.$store.state.chat.username
        },

        selectedEpisodeNumber() {
            return this.$store.state.episodes.selectedEpisode?.number
        }
    },

    mnethods: {
        logout() {
            localStorage.removeItem('ITR_USER')
            this.$store.dispatch('logoutUser', this.chat.username)
        }
    }

}
</script>