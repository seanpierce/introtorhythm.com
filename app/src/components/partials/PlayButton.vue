<template>
    <div id="play-button-container">
        <button 
            id="play-button" 
            v-if="!$parent.showMobileNav || !$parent.mobile"
            v-bind:style="{ 
                backgroundImage: 'url(' + playButtonBackgroundUrl + ')', 
                backgroundColor: 'rgba(0,0,0,0)'
            }"
            @click="togglePlay()">
        </button>
    </div>
</template>

<script>
export default {
    methods: {
        togglePlay() {
            this.$parent.togglePlay();
        },
    },
    computed: {
        playing() {
            return this.$parent.playing;
        },
        playButtonBackgroundUrl() {
            if (this.playing)
                return require('../../assets/pause.png')
            else
                return require('../../assets/play.png')
        }
    }
}
</script>

<style>
#play-button-container {
	width: 200px;
	text-align: center;
	height: 200px;
	position: fixed;
	top:0;
	bottom: 0;
	left: 0;
	right: 0;
	margin: auto;
	z-index: 5;
}
#play-button {
	height:200px;
	width: 200px;
	border: none;
	background-size: 50% 50%;
	background-repeat: no-repeat;
	background-position: center;
	outline:none;
	cursor: pointer;
}
</style>