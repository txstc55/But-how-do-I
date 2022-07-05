<template>
  <div class="text-5xl text-white text-center pb-5">{{title}}</div>
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
        this.$props.title.replace(/\s/g, "%20") +
        ".html"
    );
  },
};
</script>
