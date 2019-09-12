<template>
    <div id="play-button-container">
        <button 
            id="play-button" 
            v-if="!$parent.showMobileNav || !$parent.mobile"
            v-bind:class="{ class : true }"
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
        class() {
            if (this.playing)
                return 'pause';
            else 
                return 'play';
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