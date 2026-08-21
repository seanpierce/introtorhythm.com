<template>
  <button>
    <img
      v-if="!loading"
      :src="playing ? pauseButton : playButton"
      @click="toggleLive"
      alt="Intro To Rhythm Live play button"
      id="play-button"
    />
    <Spinner v-if="loading" />
  </button>
</template>

<script lang="ts" setup>
import { watch } from 'vue';
import Spinner from '@/components/Spinner.vue';
import { useLiveStore } from '@/stores/live';
import { storeToRefs } from 'pinia';

import playButton from '@/assets/images/play-circle-orange.webp';
import pauseButton from '@/assets/images/pause-circle-orange.webp';

const liveStore = useLiveStore();
const { playing, loading } = storeToRefs(liveStore);

const props = defineProps<{
  streamUrl: string;
}>();

const toggleLive = () => {
    liveStore.toggleLive();
}

watch(playing, async (newVal: boolean) => {
  if (newVal) {
    await liveStore.setLiveAudio(props.streamUrl);
    liveStore.playLiveAudio();
  } else {
    liveStore.stopLiveAudio();
  }
});

// if the streaming url updates
watch(() => props.streamUrl, async (newVal, oldVal) => {
  if (newVal != oldVal) {
    // stop, reset, start again
    liveStore.stopLiveAudio();
    await liveStore.setLiveAudio(props.streamUrl);
    liveStore.playLiveAudio();
  }
});
</script>
