<template>
  <div>
    <TitleComponent />
    <div class="board min-h-screen">
      <div
        class="
          text-2xl
          font-mono
          my-14
          mx-auto
          text-center
          sm:text-3xl
          md:text-4xl
          lg:text-5xl
          xl:text-6xl
          text-white
          no-select
        "
      >
        CODES I FOUND USEFUL
      </div>
      <PostGridView></PostGridView>
    </div>
    <div class="mt-10 mb-2 text-gray-400 w-full text-center">A collection of code snippets by <a href="https://txstc55.github.io/" class="underline italic">Xuan Tang</a> from his side projects</div>
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
  created() {},
};
</script>

<style scoped>
.board {
  padding-top: 50px;
  padding-bottom: 50px;
}
</style>