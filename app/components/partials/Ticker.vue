<template>
    <div>
        <div id="logo-spinner">
            <img :src="$root.staticUrl + '/images/itr-logo.png'">
        </div>
        <div class="ticker-wrap">
            <div class="ticker">
                <div class="ticker__item">&#9873;</div>
                <div class="ticker__item">Intro To Rhythm</div>
                <div class="ticker__item">&#9873;</div>
                <div class="ticker__item">Episode: {{ currentEpisode.number }} - {{ currentEpisode.title }}</div>
                <div class="ticker__item">&#9873;</div>
                <div class="ticker__item">{{ $parent.currentTime }} / {{ $parent.totalTime || '00:00:00' }}</div>
                <div class="ticker__item">&#9873;</div>
                <div class="ticker__item">introtorhythm@gmail.com</div>
                <div class="ticker__item">&#9873;</div>
                <div class="ticker__item">{{ localTime }}</div>
                <div class="ticker__item">&#9873;</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            localTime: null
        }
    },
    methods: {
        getLocalTime() {
            var output = '';
            var date = new Date();
            output += this.printDate(date) + ' - ';
            output += this.printTime(date);
            this.localTime = output;
        },
        printDate(date) {
            var output = '';
            output += (date.getMonth() + 1) + '/';
            output += date.getDate() + '/';
            output += date.getFullYear();
            return output;
        },
        printTime(date) {
            var output = '';
            var am = date.getHours() < 12;
            output += am ? date.getHours() + ':' :
                (date.getHours() === 12 ? date.getHours() : date.getHours() - 12) + ':'
            output +=  this.pad(date.getMinutes(), 2) + ':';
            output += this.pad(date.getSeconds(), 2);
            output += am ? ' am' : ' pm';
            return output;
        },
        pad(num, size) {
            var s = num + '';
            while (s.length < size) s = '0' + s;
            return s;
        }
    },
    computed: {
        currentEpisode() {
            return this.$root.data;
        },
    },
    mounted() {
        setInterval(() => {
            this.getLocalTime();
        }, 1000)
    },
}
</script>