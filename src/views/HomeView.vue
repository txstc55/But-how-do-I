<template>
  <div>
    <TitleComponent />
    <PostComponent title="How to Print to Console With Color" />
  </div>
</template>

<script>
// @ is an alias to /src
import TitleComponent from "@/components/TitleComponent.vue";
import PostComponent from "@/components/PostComponent.vue";

export default {
  name: "HomeView",
  components: {
    TitleComponent,
    PostComponent,
  },
};
</script>
