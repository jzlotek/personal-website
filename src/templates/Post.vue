<template>
  <Layout>
    <div class="content">
      <div class="content-text">
        <section class="content-text__section markdown-content">
          <h1 class="text__header">{{ $page.post.title }}</h1>
          <div :id="$page.post.title" v-html="md($page.post.fields.markdown)"></div>
        </section>
      </div>
    </div>
  </Layout>
</template>

<page-query>
query Post ($id: String! $visible: true) {
  post(id: $id) {
    title
    path
    id
    fields{
      markdown
    }
  }
}
</page-query>

<script>
import marked from "marked";

marked.setOptions({
  headerIds: false
});

export default {
  metaInfo() {
    return {
      title: this.$page.post.title,
    }
  },
  methods: {
    md(m) {
      try {
        return marked(m)
      } catch (err) {
        return m;
      }
    }
  }
};
</script>
