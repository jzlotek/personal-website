<template>
    <div class="card">
        <div class="card__inner">
            <h2 class="subsubtitle subtitle">{{ title }}</h2>
            <p class="card__text">{{ text }}</p>
            <a v-if="link" :href="link" target="_blank">
                <i v-if="icon" :class="icon"/>
                <p v-else>Click Here</p>
            </a>
            <i v-else-if="icon" :class="icon"/>
        </div>
    </div>
</template>

<script>
export default {
    name: "Card",
    props: {
        icon: {
        },
		text: {
        },
		title: {
        },
        link: {
        },
    },
}
</script>

<style lang="scss" scoped>
@import '../scss/1-global/constants';
@import '../scss/1-global/breakpoints';

.card {
    display: inline-flex;
    height: 300px;
    width: 300px;
    margin: 10px;
    border-radius: 10px;    
    background: $bg2;
    padding: 10px;
    @include breakpoint(mobile) {
        height: 100px;
        width: 100%;
    }

}
.card__inner {
    display: inline-block;
    @include breakpoint(mobile) {
        display: grid;
        text-align: left;
        grid-template-columns: auto auto;
        justify-content: center;
        align-content: center;
        h2 {
            display: none;
        }
        .card__text {
            font-size: 14px;
            grid-column-start: 2;
            grid-column-end: 3;
            grid-row-start: 1;
            grid-row-end: 2;
        }
        a {
            display: flex;
            text-decoration: none;
            grid-column-start: 1;
            grid-column-end: 2;
            grid-row-start: 1;
            grid-row-end: 2;
        }
        i {
            margin: auto;
            font-size: 50px;
        }
    }
}
</style>

