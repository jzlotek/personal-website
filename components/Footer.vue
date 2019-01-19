<template>
  <div id="footer" class="footer">
    <p class="footer__text">&copy;{{ year() }} John Zlotek</p>
  </div>
</template>

<style lang="scss" scoped>
@import '../scss/1-global/constants';

.footer {
  bottom: 20px;

  &__text {
    text-align: center;
    background-color: $bg2;
    padding: 10px;
  }
}
</style>

<script>
export default {
  name: "Footer",
  methods: {
    year() {
      const d = new Date();
      return d.getFullYear();
    }
  },
}
</script>

