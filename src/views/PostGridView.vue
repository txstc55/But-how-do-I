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
    if (this.posts.length == 0) {
      this.posts = postJson.sort(function (a, b) {
        return a.id - b.id;
      });
      this.posts = this.posts.reverse();
    }
  },
};
</script>

<style>
</style>