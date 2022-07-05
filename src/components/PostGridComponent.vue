<template>
  <div
    class="
      w-4/5
      mx-auto
      border-2
      rounded-md
      shadow-md
      border-white
      mb-5
      bg-neutral-800
    "
  >
    <div class="text-white text-5xl break-words px-5 py-7">{{ title }}</div>
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
