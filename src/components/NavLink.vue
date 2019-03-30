<template>
    <li class="nav-link">
        <g-link :to="path">
            {{ title }} <i v-if="(path === '/' && $route.path === path) || ($route.path.includes(path) && path !== '/')" class="fas fa-chevron-left"/>
        </g-link>
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
