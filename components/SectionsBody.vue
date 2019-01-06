<template>
  <div>
    <Section 
      v-for='section in sections'
      :key='section.fields.pos'
      :title='section.fields.title'
      :text='section.fields.innerContent'
      :cardInfo="section.fields.cardInfo"
      />
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
