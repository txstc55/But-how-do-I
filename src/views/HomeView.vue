<template>
  <div>
    <TitleComponent />
    <PostGridView></PostGridView>
    <div class="mt-1 mb-4 text-gray-400 w-full text-center">
      A collection of code snippets by
      <a target="_blank" href="https://txstc55.github.io/" class="underline italic"
        >Xuan Tang</a
      >
      from his side projects<br />Suggestions? Email me:
      txstc55[at]gmail[dot]com
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import TitleComponent from "@/components/TitleComponent.vue";
import PostGridView from "@/views/PostGridView.vue";

export default {
  name: "HomeView",
  components: {
    TitleComponent,
    PostGridView,
  },
  data() {
    return {};
  },
  created() {
    setTimeout(() => {
      // scroll to top when animation is finished
      window.scrollTo(0, 0);
    }, 510);
  },
};
</script>

<style scoped>
</style>