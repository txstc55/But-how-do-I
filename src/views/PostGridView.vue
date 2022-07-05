<template>
  <div class="items-center mb-8 text-center">
    <button
      class="
        border-2
        rounded-lg
        px-2
        py-1
        mx-2
        w-fit
        shadow-lg
        inline-block
        mb-2
        text-lg
        hover:bg-white hover:text-black hover:-translate-y-1 hover:shadow-2xl
        transition
        duration-300
        whitespace-pre
      "
      v-for="tag in tagsSorted"
      :key="tag.name"
      @click="selectTag(tag.name)"
      :class="
        tagsSelected.indexOf(tag.name) != -1
          ? 'text-white border-white'
          : 'text-gray-400 border-gray-500'
      "
    >
      {{ tag.name + "   " + tag.count }}
    </button>
  </div>
  <transition-group name="list" tag="ul">
    <PostGridComponent
      v-for="post in postsSelected"
      :key="post.id"
      :title="post.title"
      :tags="post.tags"
    ></PostGridComponent
  ></transition-group>
</template>

<script>
import PostGridComponent from "@/components/PostGridComponent.vue";
import postJson from "@/posts/posts.json";
export default {
  name: "PostGridView",
  components: {
    PostGridComponent,
  },
  data() {
    return {
      posts: [],
      tagsToPosts: {},
      tagsSorted: [],
      tagsSelected: [],
      postsSelected: [],
    };
  },
  methods: {
    selectTag(name) {
      var add = true;
      const index = this.tagsSelected.indexOf(name);
      if (index > -1) {
        // remove the tag, add the ones that don't have the tag
        this.tagsSelected.splice(index, 1);
        add = false;
      } else {
        // add a tag, remove some posts
        this.tagsSelected.push(name);
      }
      if (this.tagsSelected.length == 0) {
        this.postsSelected = this.posts;
      } else {
        if (add) {
          this.postsSelected = this.postsSelected.filter((item) => {
            return item.tags.indexOf(name) > -1;
          });
        } else {
          let me = this;
          this.postsSelected = this.posts.filter((item) => {
            for (var i = 0; i < me.tagsSelected.length; i++) {
              if (item.tags.indexOf(me.tagsSelected[i]) == -1) {
                return false;
              }
              return true;
            }
          });
        }
      }
    },
  },
  created() {
    if (this.posts.length == 0) {
      this.posts = postJson.sort(function (a, b) {
        return a.id - b.id;
      });
      this.posts = this.posts.reverse();
      this.postsSelected = this.posts;
      for (var i = 0; i < this.posts.length; i++) {
        for (var j = 0; j < this.posts[i].tags.length; j++) {
          var tag = this.posts[i].tags[j];
          if (tag in this.tagsToPosts) {
            this.tagsToPosts[tag].push(this.posts[i].id);
          } else {
            this.tagsToPosts[tag] = [this.posts[i].id];
          }
        }
      }
    }
    for (var tag in this.tagsToPosts) {
      this.tagsSorted.push({ name: tag, count: this.tagsToPosts[tag].length });
    }
    this.tagsSorted.sort(function (a, b) {
      return b.count - a.count;
    });
  },
};
</script>

<style scoped>
.list-enter-active {
  transition: all 1s;
}
.list-leave-active {
  transition: all 0.5s;
}
.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateX(20vw);
}

.list-leave,
.list-enter-from {
  opacity: 0;
  transform: translateX(20vw);
}
</style>