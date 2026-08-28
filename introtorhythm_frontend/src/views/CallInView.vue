<script setup lang="ts">
import { useContentStore } from '@/stores/';
import { storeToRefs } from 'pinia';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const contentStore = useContentStore();
const { callInNumber } = storeToRefs(contentStore);
const router = useRouter();

const redirectToTelRef = () => {
  const link = document.createElement('a');
  link.href = `tel:${callInNumber}`;
  link.click();
  router.push('/');
}

onMounted(() => {
  redirectToTelRef();
});
</script>
