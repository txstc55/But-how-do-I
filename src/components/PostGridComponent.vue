<template>
  <div
    class="
      w-4/5
      mx-auto
      shadow-inner
      mb-5
      bg-slate-900/20
      hover:shadow-2xl
      animate-all
      transition
      hover:-translate-y-1
      border-gray-900 border-2
      rounded-sm
      hover:bg-slate-700/20
      duration-200
      hover:border-gray-900/30
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
      <router-link :to="'/post/' + title">{{ title }}</router-link>
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
</style>
