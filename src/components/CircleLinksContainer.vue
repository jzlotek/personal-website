<template>
    <div class="links-container">
      <div class="links-outer">
        <LinkCircle
          icon="fab fa-github"
          url="https://github.com/jzlotek"
        />
        <LinkCircle
          icon="fab fa-linkedin"
          url="https://www.linkedin.com/in/john-m-zlotek-aa8609167/"
        />
        <LinkCircle
          icon="fas fa-file-pdf"
          url="https://github.com/jzlotek/resume/raw/master/resume.pdf"
        />
      </div>
    </div>
</template>

<script>
import LinkCircle from './LinkCircle';

export default {
    name: 'CircleLinksContainer',
    components: {
        LinkCircle,
    }
}
</script>

<style lang="scss">

.links {
  &-container {
    position: absolute;
    bottom: 20px;
    width: 100%;
  }

  &-outer {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    justify-content: center;
    justify-items: center;
  }
}
</style>
