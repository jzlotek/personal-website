<template>
    <div class="content">
        <div class="content-text">
        <section class="content-text__section">
            <h1 class="text__header">
            About this site
            </h1>
            <p class="text__p">
                This site was made using Vue.js and vuex and statically generated with Nuxt.js.
            </p>
        </section>
        <section class="content-text__section">
            <p class="text__p">
                FontAwesome is supplying the amazing icons.
            </p>
        </section>
        <section class="content-text__section">
            <p class="text__p">
                It is deployed through Netlify and stored on GitHub with dynamic content through contentful.
            </p>
        </section>
        </div>
        <CircleLinksContainer />
    </div>
</template>

<script>
import CircleLinksContainer from '../components/CircleLinksContainer';

export default {
    name: 'About',
    components: {
        CircleLinksContainer,
    }
}
</script>

<style>

</style>
