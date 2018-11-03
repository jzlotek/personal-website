<template>
  <div id="app">
    <!-- <router-view/> -->
    <home/>
    <resume/>
    <nav-bar/>
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

<style>
  html {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
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

  .vue-container {
    height: 100vh;
    width: 100%;
  }
</style>
