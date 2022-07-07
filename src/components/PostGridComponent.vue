<template>
  <div
    class="
      w-4/5
      mx-auto
      shadow-inner
      mb-5
      hover:shadow-2xl
      animate-all
      transition
      hover:scale-102
      border-gray-900 border-2
      rounded-lg
      duration-200
      hover:border-gray-900/30
      post-grid
    "
  >
    <div
      class="
        text-white text-xl
        sm:text-xl
        md:text-2xl
        lg:text-3xl
        xl:text-3xl
        break-words
        px-5
        py-7
        font-mono
      "
    >
      <router-link :to="'/post/' + title" class="no-select">{{
        title
      }}</router-link>
    </div>
    <TagComponent :tags="tags"></TagComponent>
  </div>
</template>

<script>
import TagComponent from "@/components/TagComponent.vue";

export default {
  name: "PostGridComponent",
  props: {
    title: String,
    tags: Array,
  },
  components: {
    TagComponent,
  },
};
</script>

<style scoped>
.post-grid {
  background-color: #1a273330;
  color: rgb(10, 12, 18);
}

.post-grid:hover {
  background-color: #3e465e40;
  color: rgb(10, 12, 18);
}
</style>
