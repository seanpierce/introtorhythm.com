<template>
    <div id="live" class="content clearfix">

        <div class="background-container">
            <img id="bg" :src="bg" alt="">
        </div>

        <PlayButton />

        <div id="actions">
            <a href="mailto:hello@introtorhythm.com">hello@introtorhythm.com</a><br>
            <a href="tel:9718018007">971-801-8007</a><br>
            <a href="#chat" @click.prevent="goDown()">Chat</a>
        </div>
        
        <Marquee v-if="marqueeText.length && showMarquee" :text="marqueeText" />
    </div>
</template>

<script setup lang="ts">
import bg from '@/assets/images/i2r-bg-big-tall.png';
import { computed, nextTick, ref, watch } from 'vue';
import { useContentStore } from '@/stores/content';
import PlayButton from '@/components/PlayButton.vue';
import Marquee from '@/components/Marquee.vue';

const contentStore = useContentStore();
const showMarquee = ref(true);
const compareMarqueeText = ref('');
const marqueeText = computed(() => {
  return contentStore.marqueeText;
});

watch(marqueeText, async () => {
  if (compareMarqueeText.value != marqueeText.value)
    await forceRemount();
});

const goDown = () => {
  document.getElementById('chat-wrapper')!.scrollIntoView({ block: 'end',  behavior: 'smooth' });
}

const forceRemount = async () => {
  showMarquee.value = false;
  await nextTick(() => {
    showMarquee.value = true;
  });
  compareMarqueeText.value = marqueeText.value;
}
</script>