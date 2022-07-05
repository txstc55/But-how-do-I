<template>
  <div>
    <TitleComponent />
    <div
      class="
        text-white text-2xl
        font-mono
        my-14
        mx-auto
        text-center
        sm:text-3xl
        md:text-4xl
        lg:text-5xl
        xl:text-6xl
      "
    >
      CHECK OUT MY CODE SNIPPET COLLECTION
    </div>
    <PostGridView></PostGridView>
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
