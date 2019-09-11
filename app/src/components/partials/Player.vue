<template>
  <div id="player" v-if="loaded">
    <div id="audio-player">
      <div id="timeline">
        <div id="playhead" :style="{ marginLeft: $parent.playPercent + 'px' }"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
    }
  },
  methods: {
    getPlayerWidth() {
      var player = document.getElementById('player');
      var playhead = document.getElementById('playhead');
      var playerWidth = player.offsetWidth - playhead.offsetWidth;
      this.$parent.playerWidth = playerWidth;
    },
    clickEvent(event) {
      var player = document.getElementById('player');
      var percent = (event.pageX - player.offsetLeft) / this.$parent.playerWidth;
      this.$parent.audio.currentTime = this.$parent.audio.duration * percent;
    },
    mouseDownEvent() {
      this.$parent.onplayhead = true;
      window.addEventListener('mousemove', this.movePlayhead, true);
      window.addEventListener('mouseup', this.mouseUpEvent, false);
      this.$parent.audio.removeEventListener('timeupdate', this.$parent.timeUpdate, false);
    },
    mouseUpEvent() {
      this.$parent.onplayhead = false;
      this.$parent.audio.addEventListener('timeupdate', this.$parent.timeUpdate, true);
      window.removeEventListener('mousemove', this.movePlayhead, true);
      window.removeEventListener('mouseup', this.mouseUpEvent, true);
    },
    movePlayhead(event) {
      var player = document.getElementById('player');
      var playhead = document.getElementById('playhead');
      var margin = event.pageX - player.offsetLeft;

      if (margin >= 0 && margin <= this.$parent.playerWidth)
        playhead.style.marginLeft = margin + "px";

      if (margin < 0)
        playhead.style.marginLeft = "0px";

      if (margin > this.$parent.playerWidth)
        playhead.style.marginLeft = this.$parent.playerWidth + "px"
    },
  }, 
  computed: {
    loaded() {
      return this.$root.loaded;
    }
  },
  mounted() {
    var player = document.getElementById('player');
    var playhead = document.getElementById('playhead');

    this.getPlayerWidth();

    player.addEventListener('click', (event) => {
      this.clickEvent(event);
    });

    playhead.addEventListener('mousedown', this.mouseDownEvent, false);
  }
}; 
</script>

<style scoped>
#player {
	position: fixed;
	bottom: 0;
	left: 0;
	height: 3em;
	width: 100%;
	background-color: rgba(255, 255, 255, 1);
	z-index: 7;
}
#audioplayer {
	width: 100%;
	height: 3em;
}
#timeline {
	width: 100%;
	height: 3em;
	border-top: solid 1px black;
	background: rgba(255,255,255,1);
}
#playhead {
	width: 10px;
	height: 3em;
	background: rgba(0, 0, 0, 1);
	cursor: ew-resize;
}
</style>
