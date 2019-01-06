<template>
  <section class="container">
    <div :id="slug" class="subcontainer">
      <h1 class=" section__title title">{{title}}</h1>
      <p class="section__text subtitle">{{text}}</p>
      <div v-if="cardInfo">
        <Cards :cards="cardInfo"/>
      </div>
      <div v-if="file">
          <img :src="file.fields.file.url"/>
      </div>
    </div>
  </section>
</template>

<script>
import Cards from './Cards.vue';

export default {
  name: 'Section',
  components: {
    Cards,
  },
  props: {
    title: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      required: false,
    },
    cardInfo: {
      type: Array,
      required: false
    },
    slug: {
      type: String,
      required: true
    },
    file: {
      type: Object,
      required: false
    }
  }
};
</script>

<style lang="scss" scoped>
.section {
  &__title {
    text-align: left;
    padding-bottom: 1vh;
    font-size: 50px;
  }
  &__text{
    text-align: left;
    font-size: 25px;
  }
}

img {
  width: 100%;
}
</style>
