<template>
  <div id="live" class="content clearfix">
    <div class="background-container">
      <img id="bg" :src="bg" alt="" />
    </div>

    <PlayButton v-if="streamUrl.length" :streamUrl="streamUrl"/>

    <div id="actions">
      <a href="mailto:hello@introtorhythm.com">hello@introtorhythm.com</a><br />
      <a :href="`tel:${callInNumber}`">{{ formattedCallInNumber }}</a><br />
      <a href="#chat" @click.prevent="goDown()">Chat</a>
    </div>

    <Marquee v-if="marqueeText.length && showMarquee" :text="marqueeText" />
  </div>
</template>

<script setup lang="ts">
import bg from '@/assets/images/i2r-bg-big-tall.webp';
import { computed, nextTick, onMounted, onUnmounted, ref, watch } from 'vue';
import { useContentStore } from '@/stores/';
import { storeToRefs } from 'pinia';
import PlayButton from '@/components/PlayButton.vue';
import Marquee from '@/components/Marquee.vue';

const contentStore = useContentStore();
const { marqueeText, streamUrl, callInNumber } = storeToRefs(contentStore);
const compareMarqueeText = ref<string>('');
const showMarquee = ref<boolean>(true);

watch(marqueeText, async () => {
  if (compareMarqueeText.value != marqueeText.value) await forceRemount();
});


const formattedCallInNumber = computed(() => {
  if (!callInNumber.value) return '';

  // 1. Strip all non-numeric characters
  const cleaned = callInNumber.value.replace(/\D/g, '')

  // 2. Ensure it is 10 digits for NNN-NNN-NNNN format
  if (cleaned.length !== 10) return '';

  // 3. Insert hyphens at positions 3 and 6
  return cleaned.replace(/(\d{3})(\d{3})(\d{4})/, '$1-$2-$3')
});

const forceRemount = async () => {
  showMarquee.value = false;
  await nextTick(() => {
    showMarquee.value = true;
  });
  compareMarqueeText.value = marqueeText.value;
};

const goDown = () => {
  document.getElementById('chat-wrapper')!.scrollIntoView({ block: 'end', behavior: 'smooth' });
};

onMounted(() => {
  contentStore.startAutoRefresh();
});

onUnmounted(() => {
  contentStore.stopAutoRefresh();
});
</script>
