<template>
    <a class="link__a" target="_blank" :href="url">
        <i :class="icon"/>
    </a>
</template>

<script>
export default {
    name: 'LinkCircle',
    props: {
        icon: {
            required: true,
        },
        url: {
            type: String,
            required: true,
        },
    },
}
</script>

<style lang="scss">
@import '../scss/1-global/constants';

.link {
    &__a {
        color: $link-selected;
        & i {
            font-size: 50px;
        }
    }
}
</style>
