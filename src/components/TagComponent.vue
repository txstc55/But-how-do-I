<template>
  <div class="py-7 px-5 text-white text-xl shadow-lg no-select">
    <span
      class="border-2 border-white rounded-lg px-2 py-1 mx-1"
      v-for="tag in tags"
      :key="tag"
      >{{ tag }}</span
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