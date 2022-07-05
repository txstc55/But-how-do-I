<template>
  <div>
    <TitleComponent />
    <div class="board">
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
        "
      >
        CHECK OUT MY CODE SNIPPET COLLECTION
      </div>
      <PostGridView></PostGridView>
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
  created() {},
};
</script>

<style scoped>
.board {
  padding-top:50px;
  padding-bottom: 50px;
}
</style>