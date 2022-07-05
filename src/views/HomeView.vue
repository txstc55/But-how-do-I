<template>
  <div>
    <TitleComponent />
    <!-- <PostComponent
      title="How to Print to Console With Color"
      tags="['c++', 'vue']"
    /> -->
    <PostGridView></PostGridView>
  </div>
</template>

<script>
// @ is an alias to /src
import TitleComponent from "@/components/TitleComponent.vue";
import PostComponent from "@/components/PostComponent.vue";
import PostGridView from "@/views/PostGridView.vue";

export default {
  name: "HomeView",
  components: {
    TitleComponent,
    PostComponent,
    PostGridView,
  },
  data() {
    return {};
  },
  created() {},
};
</script>
