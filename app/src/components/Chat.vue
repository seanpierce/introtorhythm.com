<template>
    <div id="chat">
        <div id="chat-wrapper">
            <div 
                class="new-user"
                v-if="!chat.username">
        
                <div class="new-user-form">
                    Please enter a username
                    <input 
                        placeholder="Chester"
                        type="text" 
                        autofocus
                        minlength="4"
                        maxlength="20"
                        @keyup.enter="setUser()"
                        v-model="newUser">
                    <button @click="setUser()">Join</button>
        
                    <div 
                        class="helper" 
                        v-bind:class="{ warning: newUserError }">
                        Usernames may only contain letters, numbers, underscores, or hyphens
                    </div>
                </div>
            </div>
        
            <div v-else>
                <div id="messages-header">
                    <span>Username: <strong>{{ chat.username }}</strong></span> | <strong><span class="clickable" @click="logout()">Logout</span></strong>
                </div>
                <div id="messages">
                    <!-- <Message 
                        v-for="(message, index) in chat.messages" :key="index"
                        :message="message"
                        :myMessage="message.username === chat.username" /> -->
                </div>
        
                <div id="message-input">
                    <input 
                        type="text" 
                        maxlength="140"
                        @keyup.enter="submit()"
                        v-model="message"
                        placeholder="Say something">
        
                    <button class="submit" @click="submit()">Submit</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue';

const message = ref<string>();
const newUser = ref<string>();
const newUserError = ref(false);

const chat = computed(() => {
    // return store.chat
    return {
        username: null,
        messages: []
    }
});

const setUser = () => {}

const submit = () => {}

const logout = () => {}
</script>