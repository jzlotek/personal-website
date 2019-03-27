<template>
    <li class="nav-link"><nuxt-link :to="path">{{ title }} <i v-if="$route.path === path" class="fas fa-chevron-left"/></nuxt-link></li>
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
    }
}
</script>

<style lang="scss">
@import '../scss/1-global/constants';

.nav-link {
    padding: 20px 10px 20px;
    line-height: 30px;

    & .nuxt-link-exact-active.nuxt-link-active {
        color: $link-selected;
    }
}
</style>
