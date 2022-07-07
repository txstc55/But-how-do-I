<template>
  <div
    class="
      py-6
      px-3
      text-xs
      sm:text-xs
      md:text-sm
      lg:text-lg
      xl:text-lg
      no-select
      font-mono
      overflow-hidden
    "
  >
    <div
      class="
        border-2
        rounded-md
        px-3
        py-1
        mx-2
        float-left
        text-white
      "
      v-for="tag in tags.sort()"
      :key="tag"
    >
      {{ tag }}
    </div>
  </div>
</template>


<script>
export default {
  name: "TagComponent",
  props: {
    tags: Array,
  },
  data() {
    return {
      parsedTags: [],
    };
  },
  created() {
    this.parsedTags = [];
  },
};
</script>

<style scoped>
</style>