<template>
  <div>
    <TitleComponent />
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
