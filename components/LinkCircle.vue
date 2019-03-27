<template>
    <div class="link-outer">
        <a class="link__a" target="_blank" :href="url">
            <i :class="icon"/>
        </a>
    </div>
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
        display: grid;
        justify-content: center;
        height: 20px;
        width: 20px;
        color: $link-selected;
        & i {
            font-size: 20px;
        }
    }
    &-outer {
        display: grid;
        justify-content: center;
        width: 20px;
        height: 20px;
        border-radius: 100px;
        background-color: bisque;    
    }
}
</style>
