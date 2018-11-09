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
@import '../scss/breakpoints';

@mixin hover-transition($property: color, $timing: 0.25s, $timing-function: ease-in-out) {
  transition: $property $timing $timing-function;
}

.nav-wrapper {
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  position: fixed;
  display: none;
  box-shadow: inset 0 0 0 100vh rgba(255,255,255,0.3);

  .nav-open & {
    display: block;
  }

  & .nav-inner {
    height: inherit;
    margin: 50px;
    background: rgba(50,50,50,0.3);

    & .nav-ul {
      padding: 0;
      margin: 0;

      & .nav-li {
        @include hover-transition($property: background);

        display: inline-block;
        width: 100%;
        list-style: none;
        border-radius: 4px;
        &:hover,
        &:focus {
          background: darkgray;

          & .nav-link {
            color: red;
          }
        }

        & .nav-link {
          @include hover-transition();

          padding: 15px 30px;
          font-size: 3em;

          @include breakpoint(tablet) {
            font-size: 4em;
          }

          color: grey;
          text-decoration: none;
        }
      }
    }
  }
}

@include breakpoint(desktop) {
  .nav-wrapper {
    display: block;

    & .nav-inner {

      & .nav-ul {

        & .nav-li {

          & .nav-link {
          }
        }
      }
    }
  }
}

</style>
