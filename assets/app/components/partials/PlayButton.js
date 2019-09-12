export var PlayButton = {
    data() {
        return {
        }
    },
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
                return 'pause'
            else
                return 'play'
        }
    },
    template: `
        <div id="play-button-container">
            <button 
                id="play-button" 
                v-if="!$parent.showMobileNav || !$parent.mobile"
                v-bind:class="{ 'play' : !playing, 'pause' : playing}"
                @click="togglePlay()">
            </button>
        </div>
    `
}