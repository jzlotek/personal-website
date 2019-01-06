<template>
  <div>
    <nuxt/>
  </div>
</template>

<style lang="scss">
@import '../scss/1-global/constants';

html {
  font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
  background: $bg;
}

p {
  color: $font2;
}

i {
  font-size: 10em;
  padding: 0 20px;
}

*, *:before, *:after {
  box-sizing: border-box;
  margin: 0;
}

a {
  color: $accent;
  &:hover {
    color: $accent2;
  }
}

</style>

