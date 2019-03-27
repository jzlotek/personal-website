<template>
  <div class="main">
    <a class="nav-toggle" @click="toggleNav()">
      <i class="fas fa-align-right" :class="{hide: navVisible}"/>
      <i class="far fa-times-circle" :class="{hide: !navVisible}"/>
    </a>
    <section class="nav-outer">
      <Nav/>
    </section>
    <section class="main-container">
      <nuxt/>
    </section>
  </div>
</template>

<script>
import { mapMutations, mapState } from 'vuex';

import { TOGGLE_NAV, NAV_VISIBLE } from '../store';

import Nav from '../components/Nav';

export default {
  name: 'Default',
  components: {
    Nav,
  },
  computed: {
    ...mapState({
      navVisible: NAV_VISIBLE,
    })
  },
  methods: {
    ...mapMutations({
      toggleNav: TOGGLE_NAV,
    }),
  }
}
</script>


<style lang="scss">
@import '../scss/1-global/1-global';

.main {
  background-color: $background;
  height: 100vh;
  
  @include breakpoint(desktop) {
    display: grid;
    grid-auto-columns: 20% 80%;
  }

  &-container {
    height: 100vh;
    background-color: $background-dark;
    grid-column-start: 2;
  }
}

.nav {

  &-toggle {
    display: none;
    transition: 0.5ms;

    @include breakpoint(mobile) {
      display: flex;
      position: absolute;
      margin: 20px;
      font-size: 50px;
      right: 0;
    }

    i {
      transition-duration: 0.3s;
    }

    .hide {
      display: none;
    }
  }

  &-outer {
    height: 100vh;
    display: flex;

    @include breakpoint(mobile) {
      display: none;
      width: 100%;
      background-color: $background;

      &.nav-visible {
        display: flex;
        position: absolute;
      }
    }

    @include breakpoint(desktop) {
      grid-column-start: 1;
    }
  }
}
</style>

