<template>
    <div class="wrapper">
      <div class="content">
        <h1>{{ entry.title }}</h1>
        <div :id="entry.slug" v-html="md()"></div>
      </div>
    </div>
</template>

<script>
import marked from 'marked';
import { client } from '../../plugins/contentful';
marked.setOptions({
  headerIds: false,
});

export default {
  async asyncData ({ params, error, payload }) {
    let entry = await client.getEntries({
      content_type: 'markdownSection',
      'fields.slug': params.slug,
    });

    entry = entry.items[0].fields;

    return {
      entry: entry,
    };
  },
  methods: {
    md() {
      try {
        const m = marked(this.entry.markdown);
        return m;
      } catch (err) {
        console.log(err)
        return this.entry.markdown;
      }
    },
  },
}
</script>

<style lang="scss">
@import '../../scss/1-global/constants';

* {
  color: $font;
}
</style>
