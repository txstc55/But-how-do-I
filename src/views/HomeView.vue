<template>
  <div>
    <div class="h-screen w-screen"></div>
    <div
      class="fixed top-0 h-screen w-screen main-title"
      :style="{ filter: 'blur(' + this.blur + 'px)', opacity: this.opacity }"
    >
      <TitleComponent />
    </div>
    <div :style="{ height: '50vh' }"></div>
    <PostGridView></PostGridView>
    <div class="mt-1 mb-4 text-gray-400 w-full text-center">
      A collection of code snippets by
      <a
        target="_blank"
        href="https://txstc55.github.io/"
        class="underline italic"
        >Xuan Tang</a
      >
      from his side projects<br />Suggestions? Email me:
      txstc55[at]gmail[dot]com
    </div>
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
    return {
      blur: 0,
      opacity: 1,
    };
  },
  methods: {
    computeBlurAndOpacity() {
      this.blur = Math.min(
        15,
        Math.ceil((window.scrollY / (window.innerHeight * 0.7)) * 15)
      );
      this.opacity = Math.max(
        0,
        1.5 - window.scrollY / (window.innerHeight * 0.7)
      );
    },
    scrollMethod() {
      this.computeBlurAndOpacity();
    },
    resizeMethod() {
      this.computeBlurAndOpacity();
    },
  },
  created() {
    setTimeout(() => {
      // scroll to top when animation is finished
      window.scrollTo(0, 0);
    }, 510);
    window.addEventListener("scroll", this.scrollMethod);
    window.addEventListener("resize", this.resizeMethod);
  },
  destroyed() {
    window.removeEventListener("scroll", this.scrollMethod);
    window.removeEventListener("resize", this.resizeMethod);
  },
};
</script>

<style scoped>
</style>