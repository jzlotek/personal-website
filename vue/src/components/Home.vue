<template>
  <div class="vue-container">
    <router-view/>

    <!-- <div class='p-wrapper'>
      <p>
        John Zlotek
      </p>
    </div>
    <Particles/> -->
  </div>
</template>

<style lang="scss" scoped>
@import '../scss/1-global/1-global';

#particles {
  display: block;
  height: 100%;
  width: 100%;
}

.p-wrapper {
  position: absolute;
  padding: calc(50vh - 1.5em) calc(30vw);
  font-size: 3em;
  pointer-events: none;

  & p {
    margin: 0;
    padding: 0 ;
    width: 40vw;
    background: $embers;
    border-radius: 4px;
    text-align: center;
  }
}

</style>

<script>
import Particles from '@/components/Particles.vue'

export default {
  name: 'Home',
  components: {
    Particles
  }
}
</script>
