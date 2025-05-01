import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useContentStore = defineStore('content', () => {
  const marqueeText = ref('This is a test to ensure that the marquee is working as expected. Is it? Up next: Sean Pierce throws his computer in the river!');

  return { marqueeText }
})
