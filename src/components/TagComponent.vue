<template>
  <div class="py-6 px-5 text-white text-xl shadow-lg no-select font-mono overflow-hidden">
    <div
      class="border-2 border-white rounded-lg px-2 py-1 mx-2 float-left"
      v-for="tag in tags"
      :key="tag"
      >{{ tag }}</div
    >
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