import { Navigation } from './partials/Navigation.js';
import { BackgroundImage } from './partials/BackgroundImage.js';
import { PlayButton } from './partials/PlayButton.js';
import { Modal } from './partials/modals/Modal.js';
import { Player } from './partials/Player.js';
import { Success } from './partials/modals/SubscriptionConfirmation/Success.js';
import { Failure } from './partials/modals/SubscriptionConfirmation/Failure.js';

export var Home = {
    components: {
        'Navigation': Navigation,
        'BackgroundImage': BackgroundImage,
        'PlayButton': PlayButton,
        'Modal': Modal,
        'Player': Player,
        'ConfirmationSuccess': Success,
        'ConfirmationFailure': Failure
    },
    data() {
        return {
            playing: false,
            audio: new Audio(),
            showEpisodeInfoModal: false,
            showAboutModal: false,
            currentTime: '00:00:00',
            totalTime: null,
            playPercent: 0,
            playerWidth: 0,
            onplayhead: false,
            mobile: document.documentElement.clientWidth < 750,
            showMobileNav: false,
            showConfirmationSuccess: false,
            showConfirmationFailure: false,
        }
    },
    methods: {
        togglePlay() {
            if (this.audio.paused) {
                this.playing = true;
                this.audio.play();
            } else {
                this.playing = false; 
                this.audio.pause();
            }
        },
        formatTime(input) {
            var sec_num = parseInt(input, 10);
            var hours   = Math.floor(sec_num / 3600);
            var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
            var seconds = sec_num - (hours * 3600) - (minutes * 60);
            if (hours   < 10) { hours   = "0" + hours; }
            if (minutes < 10) { minutes = "0" + minutes; }
            if (seconds < 10) { seconds = "0" + seconds; }
            return hours + ':' + minutes + ':' + seconds;
        },
        timeUpdate() {
            if (!this.totalTime)
                this.totalTime = this.formatTime(this.audio.duration);
        
            this.currentTime = this.formatTime(this.audio.currentTime);
            if (!this.onplayhead)
                this.playPercent = this.playerWidth * (this.audio.currentTime / this.audio.duration);
        },
        scribSubscriptionConfirmationOutcomeUrl() {
            window.history.replaceState({}, document.title, '/');
        },
        checkForSubscriptionConfirmationOutcome() {
            var url = new URL(window.location.href);
            var param = url.searchParams.get("success");
            if (param) {
                if (param === 'true') this.showConfirmationSuccess = true;
                else this.showConfirmationFailure = true;
                this.scribSubscriptionConfirmationOutcomeUrl();
            }
        }
    },
    computed: {
        currentEpisode() {
            return this.$root.data.current_episode;
        },
        episodes() {
            return this.$root.data.episodes;
        },
    },
    mounted() {
        this.checkForSubscriptionConfirmationOutcome();
        this.audio.src = this.$root.mediaUrl + this.currentEpisode.audio;
        this.audio.addEventListener('timeupdate', this.timeUpdate);
    },
    template: `
        <div id="home">
            <Navigation />
            <BackgroundImage />
            <PlayButton />
            <Modal v-if="showEpisodeInfoModal" type="episodeInfo"/>
            <Modal v-if="showAboutModal" type="about"/>
            <Player />
            <ConfirmationSuccess v-if="showConfirmationSuccess" />
            <ConfirmationFailure v-if="showConfirmationFailure" />
        </div>
    `
}