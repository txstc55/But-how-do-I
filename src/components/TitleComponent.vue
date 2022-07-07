<template>
  <div class="h-screen font-mono no-select titleText -z-10">
    <div class="h-1/2 relative -z-10">
      <div class="absolute bottom-0 text-2xl pl-8 pb-5">I have a CS degree</div>
    </div>
    <div class="h-1/2 relative -z-10">
      <div
        class="
          text-5xl
          m-auto
          pl-5
          absolute
          top-1/5
          sm:text-6xl
          md:text-7xl
          lg:text-8xl
          xl:text-9xl
        "
      >
        BUT HOW DO I {{ dots }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TitleComponent",
  data() {
    return {
      dots: ".   ",
      dotCount: 1,
    };
  },
  methods: {},
  created() {
    let me = this;
    setInterval(() => {
      me.dotCount = (me.dotCount + 1) % 4;
      me.dots = ".".repeat(me.dotCount) + " ".repeat(4 - me.dotCount);
    }, 600);
  },
};
</script>

<style scoped>
.titleText {
  color: #cf8944;
}
</style>
