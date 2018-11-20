<template>
  <div id="app">
    <!-- <router-view/> -->
    <nav-bar/>
    <home/>
    <resume/>
  </div>
</template>

<script>
import NavBar from './components/NavBar'
import Resume from './components/Resume'
import Home from './components/Home'

export default {
  name: 'App',
  components: {
    NavBar,
    Resume,
    Home
  }
}
</script>

<style lang='scss'>
@import './scss/1-global/1-global';
  body {
    margin: 0;
  }
  html {
    font-family: monaco, 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: $font;
    background: $bg;
    height: 100%;
    width: 100%;
    margin: 0;
    padding: 0;
    scroll-behavior: smooth;
    // scroll-snap-type: y proximity;
    // overflow-y: scroll;
  }

  a {
    text-decoration: none;
  }

  .nav-open {
    @include breakpoint(tablet) {
      & .vue-container {
        filter: blur(5px);
      }
    }
  }
  .vue-container {
    height: 100vh;
    width: 100%;
    // scroll-snap-align: start;
  }
</style>
