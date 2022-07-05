<template>
  <div v-html="rawHtmlText"></div>
</template>

<script>
export default {
  name: "PostComponent",
  props: {
    title: String,
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
          console.log("Here");
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
    this.httpGet(
      "https://raw.githubusercontent.com/txstc55/But-how-do-I/main/src/posts/" +
        this.$props.title +
        ".html"
    );
  },
};
</script>

<style scoped>
postParagraph {
  color: rgb(255 255 255);
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
    "Liberation Mono", "Courier New", monospace;
  font-size: 1.25rem /* 20px */;
  line-height: 1.75rem /* 28px */;
}
</style>