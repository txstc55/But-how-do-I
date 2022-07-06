<template>
  <div class="w-4/5 sm:w-4/5 md:w-4/5 lg:w-3/5 xl:w-1/2 relative mx-auto py-20">
    <div class="text-5xl text-white text-center pb-10 px-2 font-mono">
      {{ title }}
    </div>
    <div class="px-2" v-html="rawHtmlText"></div>
  </div>
</template>

<script>
import TagComponent from "@/components/TagComponent.vue";
export default {
  name: "PostComponent",
  props: {
    title: String,
  },
  components: {
    TagComponent,
  },
  data() {
    return {
      rawHtmlText: "",
    };
  },
  methods: {
    async httpGet(theUrl) {
      var xmlhttp = null;
      if (window.XMLHttpRequest) {
        // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
      } else {
        // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
      }
      let me = this;
      xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
          me.rawHtmlText = xmlhttp.responseText;
          setTimeout(() => {
            // scroll to top when animation is finished
            window.scrollTo(0, 0);
          }, 501);
          return xmlhttp.responseText;
        } else {
          return null;
        }
      };
      xmlhttp.open("GET", theUrl, false);
      xmlhttp.send();
    },
  },
  created() {
    this.httpGet(
      "https://raw.githubusercontent.com/txstc55/But-how-do-I/main/src/posts/" +
        encodeURIComponent(this.$props.title) +
        ".html"
    );
  },
};
</script>
