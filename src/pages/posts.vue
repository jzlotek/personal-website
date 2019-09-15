<template>
  <Layout>
    <div class="content">
      <div class="content-text">
        <section class="content-text__section">
          <h1 class="text__header">
            Posts
          </h1>
          <ul>
            <li v-for="(item, index) in $page.allPost.edges" :key="index">
              <NavLink
                :v-if="item.node.visible"
                :path="`${item.node.path}`"
                :title="item.node.title"
              />
              <!-- <p class="text__p">
                {{ item.sys.createdAt }}
              </p> -->
            </li>
          </ul>
        </section>
      </div>
    </div>
  </Layout>
</template>

<page-query>
{
  allPost{
    edges{
      node{
        id
        title
        path
      }
    }
  }
}
</page-query>

<script>
import marked from "marked";
import NavLink from "../components/NavLink";

export default {
  name: "Posts",
  metaInfo: {
    title: 'Posts'
  },
  components: {
    NavLink
  },
};
</script>
