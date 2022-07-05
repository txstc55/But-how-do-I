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
      border-white
      text-white
      font-mono
      text-lg
      py-2
      px-4
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