<template>
    <div id="chat-nav">
        <section class="hide-on-mobile">
            {{ chat.users.length === 1 ? 'it\s just you bro' : chat.users.length + ' active users'  }} | 
        </section>

        <section>
            <span class="hide-on-mobile">username: </span><span class="username me">{{ this.chat.username }}</span> | 
        </section>

        <section>
            <span 
                class="logout"
                @click="logout()">
                Log out
            </span>
        </section>
    </div>
</template>

<script>

export default {
    computed: {
        chat() {
            return this.$store.state.chat
        },
    },

    methods: {
        logout() {
            localStorage.removeItem('ITR_USER')
            this.$store.dispatch('logoutUser', this.chat.username)
        }
    } 
}

</script>
