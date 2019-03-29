<template>
  <section class="nav-container">
    <ul class="nav-ul">
      <NavLink path="/" title="Home" />
      <NavLink path="/posts" title="Posts" />
      <NavLink path="/about" title="About" />
    </ul>
    <a class="nav-toggle" @click="toggleNav()">
      <i class="far fa-times-circle fa-icon" :class="{ hide: !navVisible }" />
    </a>
  </section>
</template>

<script>
import { mapMutations, mapState } from "vuex";

import { TOGGLE_NAV, NAV_VISIBLE } from "../store";

import NavLink from "./NavLink";

export default {
  name: "Nav",
  components: {
    NavLink
  },
  computed: {
    ...mapState({
      navVisible: NAV_VISIBLE
    })
  },
  methods: {
    ...mapMutations({
      toggleNav: TOGGLE_NAV
    })
  }
};
</script>

<style lang="scss">
@import "../scss/1-global/constants";
@import "../scss/1-global/breakpoints";
.nav {
  &-container {
    display: grid;
    align-content: center;

    @include breakpoint(mobile) {
      width: 100vw;
    }
    @include breakpoint(desktop) {
      min-width: 225px;
    }
  }
}
</style>
