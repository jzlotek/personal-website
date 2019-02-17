<template>
    <div class="wrapper">
      <h1 class="title">{{ entry.title }}</h1>
      <div class="content">
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
@import '../../scss/1-global/breakpoints';
@import '../../scss/1-global/constants';

* {
  color: $font;
}
.wrapper {

  .title {
    padding: 20px;
  }

  .content {
    width: 50%;
    margin: 50px auto;
    @include breakpoint(mobile) {
      width: 200px;
    }

    h1 {
      padding: 10px;
      color: $accent-bold2;
    }

    h2 {
      padding: 5px;
    }

    h3 {

    }

    p {
      text-indent: 2em;
      padding: 10px;
    }

    a {
      text-indent: 0;
      text-decoration: none;
      color: $accent-bold2;

      &::hover {
        color: lighten($accent-bold2, 10%);
      }
    }

    img {

    }
  }
}

</style>
