<template>
  <div>
    <Section 
      v-for='(section, index) in sections'
      :key='section.fields.pos'
      :title='section.fields.title'
      :text='section.fields.innerContent'
      :cardInfo="section.fields.cardInfo"
      :slug="section.fields.slug"
      :file="section.fields.file"
      >
        <div class="container container__half parallax" v-if="index < sections.length - 1"></div>
      </Section>
  </div>
</template>

<script>
import Section from './Section.vue';

export default {
  name: 'SectionsBody',
  components: {
    Section,
  },
  props: {
    sections: {
      required: true,
      type: Array
    }
  },
};
</script>

<style>

</style>
