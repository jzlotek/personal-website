<template>
    <div class="wrapper">
      <div class="content">
        <h1>{{ entry.title }}</h1>
        <div :id="entry.slug"></div>
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
        let m = marked(this.entry.markdown);
        console.log(m)
        return m;
      } catch (err) {
        console.log(err)
        return this.entry.markdown;
      }
    },
  },
  mounted() {
    document.getElementById(this.entry.slug).innerHTML = this.md();
  }
}
</script>

<style lang="scss">
@import '../../scss/1-global/constants';

* {
  color: $font;
}
</style>
