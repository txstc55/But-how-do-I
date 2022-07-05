<template>
  <div class="w-4/5 sm:w-4/5 md:w-4/5 lg:w-3/5 xl:w-1/2 relative mx-auto">
    <div class="text-5xl text-white text-center pb-5 pt-20">{{ title }}</div>
    <div v-html="rawHtmlText"></div>
    <TagComponent :tags="tags"></TagComponent>
  </div>
</template>

<script>
import TagComponent from "@/components/TagComponent.vue";
export default {
  name: "PostComponent",
  props: {
    title: String,
    tags: Array,
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
          console.log(xmlhttp.responseText);
          me.rawHtmlText = xmlhttp.responseText;
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
    console.log(
      "https://raw.githubusercontent.com/txstc55/But-how-do-I/main/src/posts/" +
        this.$props.title.replace(/\s/g, "%20") +
        ".html"
    );
    this.httpGet(
      "https://raw.githubusercontent.com/txstc55/But-how-do-I/main/src/posts/" +
        this.$props.title.replace(/\s/g, "%20") +
        ".html"
    );
  },
};
</script>
