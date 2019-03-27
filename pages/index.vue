<template>
  <div>Home
    <LinkCircle
      icon="fab fa-github"
      url="https://github.com/jzlotek"
    />
  </div>
</template>

<script>
import { client } from '../plugins/contentful';
import LinkCircle from '../components/LinkCircle';

export default {
  components: {
    LinkCircle,
  },
  asyncData ({env}) {
    return client.getEntries({
          content_type: 'section',
          order: 'fields.pos',
      }).then((sections) => {
      return {
        sections: sections.items
      }
    }).catch(e => console.error(e))
  },
}
</script>

<style lang="scss">
@import '../scss/1-global/constants';
@import '../scss/1-global/_breakpoints.scss';
</style>

