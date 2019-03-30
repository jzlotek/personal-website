<template>
  <div class="main">
    <a class="nav-toggle" @click="toggleNav()">
      <i class="fas fa-align-right fa-icon" :class="{ hide: navVisible }" />
    </a>
    <section class="nav-outer" :class="{ 'nav-visible': navVisible }">
      <Nav />
    </section>
    <section class="main-container">
      <slot />
    </section>
  </div>
</template>

<script>
import { mapMutations, mapState } from "vuex";

import { TOGGLE_NAV, NAV_VISIBLE } from "../store";

import Nav from "../components/Nav";

export default {
  name: "Default",
  components: {
    Nav
  },
  computed: {
    ...mapState({
      navVisible: NAV_VISIBLE
    })
  },
  methods: {
    ...mapMutations({
      toggleNav: TOGGLE_NAV,
    })
  }
};
</script>

<style lang="scss">
@import "../scss/1-global/1-global";

.main {
  background-color: $background;
  height: 100vh;

  @include breakpoint(desktop) {
    display: grid;
    grid-auto-columns: 20vw auto;
  }

  &-container {
    height: 100vh;
    background-color: $background-dark;
    grid-column-start: 2;
    overflow-y: auto;
  }
}

.nav {
  &-toggle {
    display: none;
    transition: 0.5ms;

    @include breakpoint(mobile) {
      display: flex;
      position: absolute;
      z-index: 1000;
      margin: 20px;
      font-size: 50px;
      top: 0;
      right: 0;
    }

    i {
      transition-duration: 0.3s;
    }
  }

  &-outer {
    height: 100vh;
    display: flex;

    @include breakpoint(mobile) {
      position: absolute;
      z-index: 5000;
      width: 100vw;
      background-color: $background;
      opacity: 0;
      transform: translate(-100vw);

      &.nav-visible {
        transition: all 0.3s linear;
        transform: translate(0);
        opacity: 1;
      }
    }

    @include breakpoint(desktop) {
      grid-column-start: 1;
    }
  }
}

.hide {
  display: none;
}

.content {
  height: 100vh;
  display: block;
  width: 100%;

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
