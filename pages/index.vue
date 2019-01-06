<template>
  <section class="main">
    <section class="container">
      <div>
        <h1 class="title">
          John Zlotek
        </h1>
      </div>
    </section>
    <sections-body :sections="sections"/>
  </section>
</template>

<script>
import SectionsBody from '~/components/SectionsBody.vue';
import { createClient } from '../plugins/contentful';

const client = createClient();

export default {
  components: {
    SectionsBody
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

.container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.subcontainer {
  margin: 10vh 10vw;
}

.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; /* 1 */
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: $font;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: $font2;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.subsubtitle {
  font-size: 32px;
}

.links {
  padding-top: 15px;
}
</style>

