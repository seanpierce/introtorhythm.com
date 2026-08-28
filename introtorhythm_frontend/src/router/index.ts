import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import CallInView from "@/views/CallInView.vue";

const routes = [
  { path: "/", name: "Home", component: HomeView },
  { path: "/call-in", name: "Call-In", component: CallInView }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
