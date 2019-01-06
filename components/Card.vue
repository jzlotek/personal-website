<template>
    <div class="card">
        <div class="card__inner">
            <h2 class="subsubtitle subtitle">{{ title }}</h2>
            <p>{{ text }}</p>
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

.card {
    display: inline-flex;
    height: 300px;
    width: 300px;
    margin: 10px;
    border-radius: 10px;    
    background: $ink;
}
.card__inner {
    display: inline-block;
}
</style>

