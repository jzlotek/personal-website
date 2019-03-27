<template>
    <section class="nav-container">
        <ul class="nav-ul">
            <NavLink path='/' title='Home'/>
            <NavLink path='/about' title='About'/>
        </ul>
    </section>
</template>

<script>
import NavLink from './NavLink';

export default {
    name: 'Nav',
    components: {
        NavLink,
    },
}
</script>

<style lang="scss">
@import '../scss/1-global/constants';
@import '../scss/1-global/breakpoints';
.nav {
    &-container {
        // position: absolute;
        @include breakpoint(desktop) {
            display: grid;
            align-content: center;
            min-width: 150px;
        }
    }
}

</style>
