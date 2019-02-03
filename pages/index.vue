<template>
  <section class="main">
    <section class="container parallax">
      <div>
        <h1 class="title title__main">
          John Zlotek
        </h1>
      </div>
    </section>
    <sections-body :sections="sections"/>
    <Footer/>
  </section>
</template>

<script>
import SectionsBody from '~/components/SectionsBody.vue';
import Footer from '~/components/Footer.vue';
import { client } from '../plugins/contentful';


export default {
  components: {
    SectionsBody,
    Footer
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

.container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  background-color: $bg;

  &__half {
    border-radius: 0;
    min-height: 50vh;
  }
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
  background-color: $bg;
  border-radius: 10px;

  &__main {
    padding: 20px;
    margin: 20px;
  }

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

.parallax {
  background: linear-gradient(135deg, $accent, $accent2);
  height: 20vh;
  width: 100vw;

  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>

