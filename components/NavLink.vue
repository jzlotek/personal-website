<template>
    <li class="nav-link">
        <nuxt-link :to="path">
            {{ title }} <i v-if="$route.path === path" class="fas fa-chevron-left"/>
        </nuxt-link>
    </li>
</template>

<script>
export default {
    name: 'NavLink',
    props: {
        title: {
            type: String,
            required: true,
        },
        path: {
            type: String,
            required: true,
        }
    },
}
</script>

<style lang="scss">
@import '../scss/1-global/constants';
@import '../scss/1-global/breakpoints';

.nav-link {
    padding: 20px 10px;
    line-height: 30px;

    @include breakpoint(mobile) {
        text-align: right;
        font-size: 40px;
        line-height: 40px;
    }

    & .nuxt-link-exact-active.nuxt-link-active {
        color: $link-selected;
    }
}
</style>
