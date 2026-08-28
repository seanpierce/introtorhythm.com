import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import CallInView from "@/views/CallInView.vue";
import { useContentStore } from "@/stores";

const routes = [
  { path: "/", name: "Home", component: HomeView },
  { path: "/call-in",
    name: "Call-In",
    component: CallInView,
    beforeEnter: async () => {
      const contentStore = useContentStore();
      try {
        await contentStore.loadContent();
      } catch (error) {
        console.error(error);
      }
    }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
