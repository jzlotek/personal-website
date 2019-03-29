<template>
  <div class="content">
    <div class="content-text">
      <h1 class="text__title">{{ entry.title }}</h1>
      <div :id="entry.slug" v-html="md()"></div>
    </div>
  </div>
</template>

<script>
import marked from "marked";
import { client } from "../../plugins/contentful";
marked.setOptions({
  headerIds: false
});

export default {
  async asyncData({ params, error, payload }) {
    let entry = await client.getEntries({
      content_type: "markdownSection",
      "fields.slug": params.slug
    });

    entry = entry.items[0].fields;
    return {
      entry: entry
    };
  },
  methods: {
    md() {
      try {
        const m = marked(this.entry.markdown);
        return m;
      } catch (err) {
        console.log(err);
        return this.entry.markdown;
      }
    }
  }
};
</script>
