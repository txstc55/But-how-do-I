<template>
  <PostGridComponent
    v-for="post in posts"
    :key="post.title"
    :title="post.title"
    :tags="post.tags"
  ></PostGridComponent>
</template>

<script>
import PostGridComponent from "@/components/PostGridComponent.vue";
import postJson from "@/posts/posts.json";
export default {
  name: "PostGridView",
  components: {
    PostGridComponent,
  },
  data() {
    return {
      posts: [],
    };
  },
  created() {
    this.posts = postJson.reverse();
  },
};
</script>

<style>
</style>