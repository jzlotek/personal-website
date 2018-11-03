<template>
    <div class='nav-wrapper'>
        <nav class="nav-inner">
            <ul class='nav-ul'>
                <li class='nav-li' v-for="link in links" :key="link.index">
                    <router-link class='nav-link' :to="link.path">{{link.name}}</router-link>
                </li>
            </ul>
        </nav>
    </div>
</template>

<script>
export default {
  name: 'NavBar',
  data () {
    return {
      links: [
        {
          'path': '#home',
          'name': 'Home',
          'index': 0
        },
        {
          'path': '#resume',
          'name': 'Resume',
          'index': 1
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
.nav-wrapper {
  & .nav-inner {
    & .nav-ul {
      padding: 0;
      margin: 0;
      & .nav-li {
        list-style: none;
        text-align: left;
        & .nav-link {
          text-decoration: none;
        }
      }
    }
  }
}

</style>
