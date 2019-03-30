<template>
  <Layout>
    <div class="content">
      <div class="content-text">
        <section class="content-text__section">
          <h1 class="text__header">
            Hi!
          </h1>
          <p class="text__p">
            I'm John Zlotek. I am a computer science graduate student at Drexel
            University.
          </p>
        </section>
        <section class="content-text__section">
          <p class="text__p">
            I enjoy coffee, coding, and technology.
          </p>
        </section>
        <section class="content-text__section">
          <p class="text__p">
            I am currently a teching assistant for CS265 (Advanced Programming
            Techniques) at Drexel.
          </p>
        </section>
      </div>
      <CircleLinksContainer />
    </div>
  </Layout>
</template>

<script>
import CircleLinksContainer from "../components/CircleLinksContainer";

export default {
  metaInfo: {
    title: 'Home'
  },
  components: {
    CircleLinksContainer
  }
};
</script>
