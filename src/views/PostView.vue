<template>
  <PostComponent :title="$route.params.title"></PostComponent>
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