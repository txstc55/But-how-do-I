<template>
  <PostComponent :title="$route.params.title"></PostComponent>
  <router-link
    to="/"
    class="
      fixed
      bottom-5
      left-1/2
      -translate-x-1/2
      border-2
      rounded-lg
      border-white/50
      text-white
      font-mono
      text-lg
      py-2
      px-5
      hover:bg-gray-900/70
      transform
      duration-500
      hover:shadow-xl hover:scale-105 hover:border-white
    "
  >
    HOME
  </router-link>
</template>

<script>
import PostComponent from "@/components/PostComponent.vue";
export default {
  name: "PostView",
  components: {
    PostComponent,
  },
};
</script>

<style>
</style>