<template>
    <div id="cards">
        <Card 
            v-for="(card, index) in cards"
            :key="index"
		    :title="card.title"
		    :text="card.text"
            :icon="card.icon"
            :link="card.link"
            />
    </div>
</template>

<script>
import Card from './Card';

export default {
    name: "Cards",
    components: {
        Card,
    },
    props: {
        cards: {
            type: Array,
            required: true
        }
    }
}
</script>

<style lang="scss">
.cards {
    width: 100%;
}
</style>
