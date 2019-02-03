<template>
    <div>
      <div>
        <ul>
          <li v-for="item in sections" :key="item">
              <nuxt-link :to="`/blog/${item.fields.slug}`">{{ item.fields.title }}</nuxt-link>
          </li>
        </ul>
      </div>
    </div>
</template>

<script>
import marked from 'marked';
import { client } from './../../plugins/contentful';

export default {
  asyncData ({env}) {
    return client.getEntries({
      content_type: 'markdownSection',
    }).then((sections) => {
    return {
      sections: sections.items
    }
    }).catch(e => console.error(e))
  },
  methods: {
    sectionMD(md) {
      try {
        return marked(md);
      } catch (err) {
        return md;
      }
    }
  }
}
</script>

<style>

</style>
