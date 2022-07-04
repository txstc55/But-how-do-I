<template>
  <div class="h-screen font-mono no-select">
    <div class="text-white h-1/2 relative">
      <div class="absolute bottom-0 text-2xl pl-8 pb-5">I have a CS degree</div>
    </div>
    <div class="h-1/2 text-white relative">
      <div
        class="
          text-5xl text-white
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
