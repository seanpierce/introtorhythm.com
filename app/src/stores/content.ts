import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useContentStore = defineStore('content', () => {
  const marqueeText = ref('');

  return { marqueeText }
})
