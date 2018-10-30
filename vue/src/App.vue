<template>
  <div id="app">
    <nav class="nav">
      <router-link to="/">Home</router-link>
      <router-link to="/resume">Resume</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
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
</style>
