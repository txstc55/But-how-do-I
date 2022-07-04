<template>
  <div>
    <TitleComponent />
  </div>
</template>

<script>
// @ is an alias to /src
import TitleComponent from "@/components/TitleComponent.vue";

export default {
  name: "HomeView",
  components: {
    TitleComponent,
  },
};
</script>
