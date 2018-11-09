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

  html {
    font-family: monaco, 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #c9c9c9;
    background: #101b24;
    height: 100%;
    width: 100%;
    margin: 0;
    padding: 0;
  }

  a {
    text-decoration: none;
  }

  .nav-open {
    & .vue-container {
      filter: blur(5px);
    }
  }
  .vue-container {
    height: 100vh;
    width: 100%;
  }
</style>
