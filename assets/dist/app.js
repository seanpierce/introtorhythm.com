/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./App.js":
/*!****************!*\
  !*** ./App.js ***!
  \****************/
/*! exports provided: App */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"App\", function() { return App; });\n/* harmony import */ var _components_Home_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./components/Home.js */ \"./components/Home.js\");\n/* harmony import */ var _components_Archive_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./components/Archive.js */ \"./components/Archive.js\");\n\n\n\nvar App = {\n    components: {\n        'Home': _components_Home_js__WEBPACK_IMPORTED_MODULE_0__[\"Home\"],\n        'Archive': _components_Archive_js__WEBPACK_IMPORTED_MODULE_1__[\"Archive\"]\n    },\n    data() {\n        return {\n        }\n    },\n    methods: {\n        test() {\n            console.log('ok');\n        }\n    },\n    computed: {\n        route() {\n            var path = window.location.pathname;\n            switch (path) {\n                case '/archive':\n                    return 'archive';\n                default:\n                    return 'home';\n            }\n        },\n        loaded() {\n            return this.$root.loaded;\n        },\n    },\n    template: `\n        <div v-if=\"loaded\">\n            <Home v-if=\"route === 'home'\"/>\n            <Archive v-if=\"route === 'archive'\"/>\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./App.js?");

/***/ }),

/***/ "./components/Archive.js":
/*!*******************************!*\
  !*** ./components/Archive.js ***!
  \*******************************/
/*! exports provided: Archive */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"Archive\", function() { return Archive; });\nvar Archive = {\n    data() {\n        return {\n        }\n    },\n    methods: {\n        formatFileName(number, title) {\n            var formattedTitle = title.replace(/[-,./ !*:]/g, '_');\n            return '/' + number + '_' + formattedTitle;\n        } \n    },\n    computed: {\n        episodes() {\n            return this.$root.data.episodes;\n        }\n    },\n    template: `\n        <div id=\"archive\">\n            <div><a href=\"/\">Intro To Rhythm/</a></div>\n            <div class=\"tab-1\">archive/</div>\n            <div class=\"tab-2\">episodes/</div>\n            <div class=\"tab-3\">\n                <li v-for=\"episode in episodes\" :key=\"episode.number\">\n                    <a :href=\"'/' + episode.number\">{{ formatFileName(episode.number, episode.title) }}</a>\n                </li>\n            </div>\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./components/Archive.js?");

/***/ }),

/***/ "./components/Home.js":
/*!****************************!*\
  !*** ./components/Home.js ***!
  \****************************/
/*! exports provided: Home */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"Home\", function() { return Home; });\n/* harmony import */ var _partials_Navigation_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./partials/Navigation.js */ \"./components/partials/Navigation.js\");\n/* harmony import */ var _partials_BackgroundImage_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./partials/BackgroundImage.js */ \"./components/partials/BackgroundImage.js\");\n/* harmony import */ var _partials_PlayButton_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./partials/PlayButton.js */ \"./components/partials/PlayButton.js\");\n/* harmony import */ var _partials_modals_Modal_js__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./partials/modals/Modal.js */ \"./components/partials/modals/Modal.js\");\n/* harmony import */ var _partials_Player_js__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./partials/Player.js */ \"./components/partials/Player.js\");\n/* harmony import */ var _partials_modals_SubscriptionConfirmation_Success_js__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./partials/modals/SubscriptionConfirmation/Success.js */ \"./components/partials/modals/SubscriptionConfirmation/Success.js\");\n/* harmony import */ var _partials_modals_SubscriptionConfirmation_Failure_js__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./partials/modals/SubscriptionConfirmation/Failure.js */ \"./components/partials/modals/SubscriptionConfirmation/Failure.js\");\n\n\n\n\n\n\n\n\nvar Home = {\n    components: {\n        'Navigation': _partials_Navigation_js__WEBPACK_IMPORTED_MODULE_0__[\"Navigation\"],\n        'BackgroundImage': _partials_BackgroundImage_js__WEBPACK_IMPORTED_MODULE_1__[\"BackgroundImage\"],\n        'PlayButton': _partials_PlayButton_js__WEBPACK_IMPORTED_MODULE_2__[\"PlayButton\"],\n        'Modal': _partials_modals_Modal_js__WEBPACK_IMPORTED_MODULE_3__[\"Modal\"],\n        'Player': _partials_Player_js__WEBPACK_IMPORTED_MODULE_4__[\"Player\"],\n        'ConfirmationSuccess': _partials_modals_SubscriptionConfirmation_Success_js__WEBPACK_IMPORTED_MODULE_5__[\"Success\"],\n        'ConfirmationFailure': _partials_modals_SubscriptionConfirmation_Failure_js__WEBPACK_IMPORTED_MODULE_6__[\"Failure\"]\n    },\n    data() {\n        return {\n            playing: false,\n            audio: new Audio(),\n            showEpisodeInfoModal: false,\n            showAboutModal: false,\n            currentTime: '00:00:00',\n            totalTime: null,\n            playPercent: 0,\n            playerWidth: 0,\n            onplayhead: false,\n            mobile: document.documentElement.clientWidth < 750,\n            showMobileNav: false,\n            showConfirmationSuccess: false,\n            showConfirmationFailure: false,\n        }\n    },\n    methods: {\n        togglePlay() {\n            if (this.audio.paused) {\n                this.playing = true;\n                this.audio.play();\n            } else {\n                this.playing = false; \n                this.audio.pause();\n            }\n        },\n        formatTime(input) {\n            var sec_num = parseInt(input, 10);\n            var hours   = Math.floor(sec_num / 3600);\n            var minutes = Math.floor((sec_num - (hours * 3600)) / 60);\n            var seconds = sec_num - (hours * 3600) - (minutes * 60);\n            if (hours   < 10) { hours   = \"0\" + hours; }\n            if (minutes < 10) { minutes = \"0\" + minutes; }\n            if (seconds < 10) { seconds = \"0\" + seconds; }\n            return hours + ':' + minutes + ':' + seconds;\n        },\n        timeUpdate() {\n            if (!this.totalTime)\n                this.totalTime = this.formatTime(this.audio.duration);\n        \n            this.currentTime = this.formatTime(this.audio.currentTime);\n            if (!this.onplayhead)\n                this.playPercent = this.playerWidth * (this.audio.currentTime / this.audio.duration);\n        },\n        scribSubscriptionConfirmationOutcomeUrl() {\n            window.history.replaceState({}, document.title, '/');\n        },\n        checkForSubscriptionConfirmationOutcome() {\n            var url = new URL(window.location.href);\n            var param = url.searchParams.get(\"success\");\n            if (param) {\n                if (param === 'true') this.showConfirmationSuccess = true;\n                else this.showConfirmationFailure = true;\n                this.scribSubscriptionConfirmationOutcomeUrl();\n            }\n        }\n    },\n    computed: {\n        currentEpisode() {\n            return this.$root.data.current_episode;\n        },\n        episodes() {\n            return this.$root.data.episodes;\n        },\n    },\n    mounted() {\n        this.checkForSubscriptionConfirmationOutcome();\n        this.audio.src = this.$root.mediaUrl + this.currentEpisode.audio;\n        this.audio.addEventListener('timeupdate', this.timeUpdate);\n    },\n    template: `\n        <div id=\"home\">\n            <Navigation />\n            <BackgroundImage />\n            <PlayButton />\n            <Modal v-if=\"showEpisodeInfoModal\" type=\"episodeInfo\"/>\n            <Modal v-if=\"showAboutModal\" type=\"about\"/>\n            <Player />\n            <ConfirmationSuccess v-if=\"showConfirmationSuccess\" />\n            <ConfirmationFailure v-if=\"showConfirmationFailure\" />\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./components/Home.js?");

/***/ }),

/***/ "./components/partials/BackgroundImage.js":
/*!************************************************!*\
  !*** ./components/partials/BackgroundImage.js ***!
  \************************************************/
/*! exports provided: BackgroundImage */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"BackgroundImage\", function() { return BackgroundImage; });\nvar BackgroundImage = {\n    data() {\n        return {\n        }\n    },\n    methods: {\n    },\n    computed: {\n        imageUrl() {\n            return this.$root.mediaUrl + this.$parent.currentEpisode.image;\n        }\n    },\n    template: `\n        <div>\n            <div id=\"brighten\"></div>\n            <div id=\"background-image\" :style=\"{ backgroundImage: 'url(' + imageUrl + ')' }\"></div>\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./components/partials/BackgroundImage.js?");

/***/ }),

/***/ "./components/partials/Navigation.js":
/*!*******************************************!*\
  !*** ./components/partials/Navigation.js ***!
  \*******************************************/
/*! exports provided: Navigation */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"Navigation\", function() { return Navigation; });\n/* harmony import */ var _SubscriptionForm_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./SubscriptionForm.js */ \"./components/partials/SubscriptionForm.js\");\n\n\nvar Navigation = {\n    components: {\n        'SubscriptionForm': _SubscriptionForm_js__WEBPACK_IMPORTED_MODULE_0__[\"SubscriptionForm\"]\n    },\n    data() {\n        return {\n        }\n    },\n    methods: {\n        isCurrent(number) {\n            return this.currentEpisode.number === number;\n        },\n        showEpisodeInfoModal() {\n            this.$parent.showEpisodeInfoModal = true;\n        },\n        showAboutModal() {\n            this.$parent.showAboutModal = true;\n        },\n        toggleMobileNav() {\n            this.$parent.showMobileNav = !this.$parent.showMobileNav;\n        },\n        resize() {\n            var width = document.documentElement.clientWidth;  \n            if (width > 750)\n                this.$parent.mobile = false;\n            else\n              this.$parent.mobile = true;\n        }\n    },\n    computed: {\n        showNav() {\n            return this.$parent.mobile && this.$parent.showMobileNav || !this.$parent.mobile;\n        },\n        loaded() {\n            return this.$root.loaded;\n        },\n        currentEpisode() {\n            return this.$root.data.current_episode;\n        },\n        episodes() {\n            return this.$root.data.episodes;\n        },\n    },\n    mounted() {\n        window.addEventListener('resize', this.resize);\n    },\n    template: `\n        <div>\n            <div id=\"mobile-nav-toggle\" v-if=\"$parent.mobile\">\n                <div id=\"menu-container\" @click=\"toggleMobileNav()\" :class=\"{ 'change': $parent.showMobileNav }\">\n                    <div class=\"bar1\"></div>\n                    <div class=\"bar2\"></div>\n                    <div class=\"bar3\"></div>\n                </div>\n            </div>\n            <div id=\"nav\" v-if=\"loaded && showNav\">\n                <ul>\n                    <li><a href=\"/\">Intro To Rhythm</a><li>\n                    <li>------</li>\n                    <li>Now Playing: Ep {{ currentEpisode.number }}</li>\n                    <li id=\"tracktime\">{{ $parent.currentTime }} / {{ $parent.totalTime || '00:00:00' }}</li>\n                    <li>\n                    <span \n                        class=\"red pointer\"\n                        @click=\"showEpisodeInfoModal()\">\n                        See Ep {{ currentEpisode.number }} Info &lt;\n                    </span>\n                    </li>\n                    <li>------</li>\n                    <li v-for=\"episode in episodes\" :key=\"episode.number\" :class=\"isCurrent(episode.number) ? 'red': ''\">\n                    <a :href=\"'/' + episode.number\">{{ episode.number }}- {{ episode.title }}</a>\n                    </li>\n                    <li>------</li>\n                    <li><span class=\"pointer\" @click=\"showAboutModal()\">About ITR</span></li>\n                    <li><a href=\"/archive\">Archive</a></li>\n                    <SubscriptionForm />\n                </ul>\n            </div>\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./components/partials/Navigation.js?");

/***/ }),

/***/ "./components/partials/PlayButton.js":
/*!*******************************************!*\
  !*** ./components/partials/PlayButton.js ***!
  \*******************************************/
/*! exports provided: PlayButton */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"PlayButton\", function() { return PlayButton; });\nvar PlayButton = {\n    data() {\n        return {\n        }\n    },\n    methods: {\n        togglePlay() {\n            this.$parent.togglePlay();\n        },\n    },\n    computed: {\n        playing() {\n            return this.$parent.playing;\n        },\n        class() {\n            if (this.playing)\n                return 'pause'\n            else\n                return 'play'\n        }\n    },\n    template: `\n        <div id=\"play-button-container\">\n            <button \n                id=\"play-button\" \n                v-if=\"!$parent.showMobileNav || !$parent.mobile\"\n                v-bind:class=\"{ \n                    'play' : !playing, \n                    'pause' : playing,\n                }\"\n                @click=\"togglePlay()\">\n            </button>\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./components/partials/PlayButton.js?");

/***/ }),

/***/ "./components/partials/Player.js":
/*!***************************************!*\
  !*** ./components/partials/Player.js ***!
  \***************************************/
/*! exports provided: Player */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"Player\", function() { return Player; });\nvar Player = {\n    data() {\n        return {\n        }\n    },\n    methods: {\n        getPlayerWidth() {\n            var player = document.getElementById('player');\n            var playhead = document.getElementById('playhead');\n            var playerWidth = player.offsetWidth - playhead.offsetWidth;\n            this.$parent.playerWidth = playerWidth;\n        },\n        clickEvent(event) {\n            var player = document.getElementById('player');\n            var percent = (event.pageX - player.offsetLeft) / this.$parent.playerWidth;\n            this.$parent.audio.currentTime = this.$parent.audio.duration * percent;\n        },\n        mouseDownEvent() {\n            this.$parent.onplayhead = true;\n            window.addEventListener('mousemove', this.movePlayhead, true);\n            window.addEventListener('mouseup', this.mouseUpEvent, false);\n            this.$parent.audio.removeEventListener('timeupdate', this.$parent.timeUpdate, false);\n        },\n        mouseUpEvent() {\n            this.$parent.onplayhead = false;\n            this.$parent.audio.addEventListener('timeupdate', this.$parent.timeUpdate, true);\n            window.removeEventListener('mousemove', this.movePlayhead, true);\n            window.removeEventListener('mouseup', this.mouseUpEvent, true);\n        },\n        movePlayhead(event) {\n            var player = document.getElementById('player');\n            var playhead = document.getElementById('playhead');\n            var margin = event.pageX - player.offsetLeft;\n      \n            if (margin >= 0 && margin <= this.$parent.playerWidth)\n                playhead.style.marginLeft = margin + \"px\";\n      \n            if (margin < 0)\n                  playhead.style.marginLeft = \"0px\";\n      \n            if (margin > this.$parent.playerWidth)\n                playhead.style.marginLeft = this.$parent.playerWidth + \"px\"\n        },\n    },\n    computed: {\n        loaded() {\n            return this.$root.loaded;\n        }\n    },\n    mounted() {\n        var player = document.getElementById('player');\n        var playhead = document.getElementById('playhead');\n    \n        this.getPlayerWidth();\n    \n        player.addEventListener('click', (event) => {\n            this.clickEvent(event);\n        });\n    \n        playhead.addEventListener('mousedown', this.mouseDownEvent, false);\n        window.addEventListener('resize', this.getPlayerWidth);\n    },\n    template: `\n        <div id=\"player\" v-if=\"loaded\">\n            <div id=\"audio-player\">\n            <div id=\"timeline\">\n                <div id=\"playhead\" :style=\"{ marginLeft: $parent.playPercent + 'px' }\"></div>\n            </div>\n            </div>\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./components/partials/Player.js?");

/***/ }),

/***/ "./components/partials/SubscriptionForm.js":
/*!*************************************************!*\
  !*** ./components/partials/SubscriptionForm.js ***!
  \*************************************************/
/*! exports provided: SubscriptionForm */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"SubscriptionForm\", function() { return SubscriptionForm; });\nvar SubscriptionForm = {\n    data() {\n        return {\n            email: null,\n            name: null,\n            human: false,\n            success: false,\n            confirmationEmail: null\n        }\n    },\n    methods: {\n        submit() {\n            if (!this.formIsValid) {\n                // show success to spam bots\n                this.handleSuccess(this.email)\n                return;\n            }\n\n            var payload = {\n                email: this.email\n            }\n\n            axios.post('/api/requests/', payload)\n                .then(res => {\n                    this.handleSuccess(this.email);\n                    console.log(res);\n                })\n                .catch(err => {\n                    this.handleError(err);\n                })\n        },\n        handleSuccess(email) {\n            this.success = true;\n            this.confirmationEmail = email;\n        },\n        handleError(err) {\n            console.log(err);\n        }\n    },\n    computed: {\n        formIsValid() {\n            // catch spam bots who've attempted to fill honeypot fields\n            return !this.name && !this.human && (this.email !== null && this.email !== '');\n        }\n    },\n    mounted() {\n    },\n    template: `\n        <div id=\"subscription-form\">\n            <form @submit.prevent=\"submit()\" v-if=\"!success\">\n                <label for=\"kjhasd73\">Email Address</label>\n                <input type=\"email\" \n                    name=\"kjhasd73\" id=\"kjhasd73\" \n                    class=\"j8sdaslkj\" \n                    placeholder=\"email address\"\n                    v-model=\"email\">\n                <label for=\"sldkf9jk\">Name</label>\n                <input type=\"text\" \n                    name=\"sldkf9jk\" \n                    id=\"sldkf9jk\" \n                    class=\"a9842jhmk\" \n                    placeholder=\"name\"\n                    v-model=\"name\">\n                <label for=\"kajsdh\">I am not a robot</label>\n                <input type=\"checkbox\" \n                    name=\"kajsdh\" \n                    id=\"kajsdh\" \n                    class=\"aujs8787s\" \n                    v-model=\"human\">\n                <input type=\"submit\" value=\"Subscribe\">\n            </form>\n            <div v-if=\"success\">\n                Thanks! A confirmation email was sent to {{ confirmationEmail }}\n            </div>\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./components/partials/SubscriptionForm.js?");

/***/ }),

/***/ "./components/partials/modals/About.js":
/*!*********************************************!*\
  !*** ./components/partials/modals/About.js ***!
  \*********************************************/
/*! exports provided: About */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"About\", function() { return About; });\nvar About = {\n    data() {\n        return {\n        }\n    },\n    methods: {\n    },\n    computed: {\n    },\n    template: `\n        <div id=\"about\">\n            <div class=\"content\">\n                Intro To Rhythm is a freeform mix series and live-streaming audio station that began in 2017. All episodes and content are owned by their creators and made exclusively for Intro To Rhythm.\n                <br>\n                <br>\n                Additionally, ITR is dedicated to open-source projects, and the collective idea sharing that fuels creative expression. If you're interested in developing your own live-streaming station or podcasting platform, you're invited to refer to ITR's source code (Licence MIT).\n                <br>\n                <br>\n                Send questions and comments to introtorhythm@gmail.com<br>\n                Follow ITR on: <a href=\"https://www.facebook.com/introtorhythm/\">Facebook</a> / <a href=\"https://www.instagram.com/introtorhythm/\">Instagram</a> / <a href=\"https://twitter.com/introtorhythm\">Twitter</a>\n                <br>\n                <br>\n                ------------\n                <br>\n                <br>\n                Maintaining this application and it's server environments can be costly and time consuming. If you appreciate ITR and you have the means, please consider making a donation.\n                <br>\n                <br>\n                <form action=\"https://www.paypal.com/cgi-bin/webscr\" method=\"post\" target=\"_top\">\n                    <input type=\"hidden\" name=\"cmd\" value=\"_s-xclick\" />\n                    <input type=\"hidden\" name=\"hosted_button_id\" value=\"TUHQST72H25YS\" />\n                    <input type=\"image\" src=\"https://introtorhythm.com/assets/images/donate-button-2.png\" border=\"0\" name=\"submit\" title=\"PayPal - The safer, easier way to pay online!\" alt=\"Donate with PayPal button\" />\n                <img alt=\"\" border=\"0\" src=\"https://www.paypal.com/en_US/i/scr/pixel.gif\" width=\"1\" height=\"1\" />\n                </form>\n            </div>\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./components/partials/modals/About.js?");

/***/ }),

/***/ "./components/partials/modals/EpisodeInfo.js":
/*!***************************************************!*\
  !*** ./components/partials/modals/EpisodeInfo.js ***!
  \***************************************************/
/*! exports provided: EpisodeInfo */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"EpisodeInfo\", function() { return EpisodeInfo; });\nvar EpisodeInfo = {\n    data() {\n        return {\n        }\n    },\n    methods: {\n    },\n    computed: {\n        currentEpisode() {\n            return this.$root.data.current_episode;\n        }\n    },\n    template: `\n        <div id=\"episode-info\" class=\"content\">\n            <div id=\"episode-heading\">{{ currentEpisode.number }}- {{ currentEpisode.title }}</div>\n            <div v-html=\"currentEpisode.content\"></div>\n            <div>\n                ------------<br>\n                <br>\n                Share this episode on:<br>\n                <a :href=\"'https://www.facebook.com/sharer/sharer.php?u=https://introtorhythm.com/' + currentEpisode.number\" target=\"_blank\">facebook</a> / <a :href=\"'https://twitter.com/home?status=https://introtorhythm.com/' + currentEpisode.number\">twitter</a><br>\n                <br>\n                info@introtorhythm.com\n            </div>\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./components/partials/modals/EpisodeInfo.js?");

/***/ }),

/***/ "./components/partials/modals/Modal.js":
/*!*********************************************!*\
  !*** ./components/partials/modals/Modal.js ***!
  \*********************************************/
/*! exports provided: Modal */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"Modal\", function() { return Modal; });\n/* harmony import */ var _EpisodeInfo_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./EpisodeInfo.js */ \"./components/partials/modals/EpisodeInfo.js\");\n/* harmony import */ var _About_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./About.js */ \"./components/partials/modals/About.js\");\n\n\n\nvar Modal = {\n    components: {\n        'EpisodeInfo': _EpisodeInfo_js__WEBPACK_IMPORTED_MODULE_0__[\"EpisodeInfo\"],\n        'About': _About_js__WEBPACK_IMPORTED_MODULE_1__[\"About\"]\n    },\n    props : {\n        type: String\n    },\n    data() {\n        return {\n        }\n    },\n    methods: {\n        closeModal(event) {\n            var target = event.target.id;\n            if (target !== 'modal' && target !== 'close') return;\n\n            if (this.type === \"episodeInfo\")\n                this.$parent.showEpisodeInfoModal = false;\n\n            if (this.type === \"about\")\n                this.$parent.showAboutModal = false;\n        }\n    },\n    computed: {\n    },\n    template: `\n        <div id=\"modal\" @click=\"closeModal($event)\">\n            <div class=\"modal-content\">\n                <img id=\"close\" \n                    class=\"pointer\" \n                    @click=\"closeModal($event)\"\n                    :src=\"$root.staticUrl + '/images/close.svg'\">\n                <!-- content -->\n                <EpisodeInfo v-if=\"type==='episodeInfo'\" />\n                <About v-if=\"type==='about'\" />\n            </div>\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./components/partials/modals/Modal.js?");

/***/ }),

/***/ "./components/partials/modals/SubscriptionConfirmation/Failure.js":
/*!************************************************************************!*\
  !*** ./components/partials/modals/SubscriptionConfirmation/Failure.js ***!
  \************************************************************************/
/*! exports provided: Failure */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"Failure\", function() { return Failure; });\nvar Failure = {\n    data() {\n        return {\n        }\n    },\n    methods: {\n        closeConfirmationSuccess() {\n            this.$parent.showConfirmationFailure = false;\n        }\n    },\n    computed: {\n    },\n    template: `\n        <div id=\"subscription-confirmation-modal\" @click=\"closeConfirmationSuccess()\">\n            <div class=\"content\">\n                <h1>Oh no! We're unable to add your email to our subscription list. If you need help, reach out to introtorhythm@gmail.com. Click anywhere to return to Intro To Rhythm.</h1>\n                <img :src=\"$root.staticUrl + '/images/wrench.png'\">\n            </div>\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./components/partials/modals/SubscriptionConfirmation/Failure.js?");

/***/ }),

/***/ "./components/partials/modals/SubscriptionConfirmation/Success.js":
/*!************************************************************************!*\
  !*** ./components/partials/modals/SubscriptionConfirmation/Success.js ***!
  \************************************************************************/
/*! exports provided: Success */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"Success\", function() { return Success; });\nvar Success = {\n    data() {\n        return {\n        }\n    },\n    methods: {\n        closeConfirmationSuccess() {\n            this.$parent.showConfirmationSuccess = false;\n        }\n    },\n    computed: {\n    },\n    template: `\n        <div id=\"subscription-confirmation-modal\" @click=\"closeConfirmationSuccess()\">\n            <div class=\"content\">\n                <h1>Thanks! Your email has beed added to our list of subscribers. Click anywhere to return to Intro To Rhythm.</h1>\n                <img :src=\"$root.staticUrl + '/images/wrench.png'\">\n            </div>\n        </div>\n    `\n}\n\n//# sourceURL=webpack:///./components/partials/modals/SubscriptionConfirmation/Success.js?");

/***/ }),

/***/ "./index.js":
/*!******************!*\
  !*** ./index.js ***!
  \******************/
/*! exports provided: vue */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"vue\", function() { return vue; });\n/* harmony import */ var _App_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./App.js */ \"./App.js\");\n\n\nconst vue = new Vue({\n    delimiters: ['[[', ']]'],\n    el: '#app',\n    components: {\n        'App': _App_js__WEBPACK_IMPORTED_MODULE_0__[\"App\"]\n    },\n    data: {\n        data: null,\n        mediaUrl: 'https://s3.amazonaws.com/podcasts.introtorhythm.com/media/',\n        staticUrl: 'static'\n    },\n    computed: {\n        loaded() {\n            return this.data != null;\n        }\n    },\n    mounted() {\n        // Fetch the initial page data MVC style\n        var elem = document.getElementById('data');\n\n        if (elem) {\n            var data = elem.attributes.data.value;\n            this.data = JSON.parse(data);\n        }\n    },\n    template: `\n        <App />\n    `\n  })\n\n//# sourceURL=webpack:///./index.js?");

/***/ })

/******/ });