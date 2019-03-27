<template>
  <div class="content">
    <div class="content-text">
      <section class="content-text__section">
        <h1 class="text__header">
          Hi!
        </h1>
        <p class="text__p">
          I'm John Zlotek. I am a computer science graduate student at Drexel University.
        </p>
      </section>
      <section class="content-text__section">
        <p class="text__p">
          I enjoy coffee, coding, and technology.
        </p>
      </section>
      <section class="content-text__section">
        <p class="text__p">
          I am currently a teching assistant for CS265 (Advanced Programming Techniques) at Drexel.
        </p>
      </section>
    </div>
    <CircleLinksContainer />
  </div>
</template>

<script>
import { client } from '../plugins/contentful';
import CircleLinksContainer from '../components/CircleLinksContainer';

export default {
  components: {
    CircleLinksContainer,
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
@import '../scss/1-global/breakpoints';

.content {
  height: 100vh;
  display: block;

  @include breakpoint(desktop) {
    position: relative;
  }

  &-text {
    display: grid;
    grid-column-gap: 20px;
    grid-row-gap: 20px;
    grid-template-columns: 1fr;
    justify-content: center;
    padding: 150px 50px 0px;

    &__section {

    }
  }
}
</style>

