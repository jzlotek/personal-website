<template>
  <div class="content">
    <div class="content-text">
      <section class="content-text__section">
        <h1 class="text__header">
          Posts
        </h1>
        <ul>
          <li v-for="item in sections" :key="item">
            <NavLink
              :path="`/posts/${item.fields.slug}`"
              :title="item.fields.title"
            />
            <p class="text__p">
              {{ item.sys.createdAt }}
            </p>
          </li>
        </ul>
      </section>
    </div>
  </div>
</template>

<script>
import marked from "marked";
import NavLink from "../../components/NavLink";
import { client } from "./../../plugins/contentful";

export default {
  name: "Posts",
  components: {
    NavLink
  },
  async asyncData({ env, payload }) {
    if (payload) {
      console.log("has payload");
      return {
        sections: payload.items
      };
    }
    if (!client) {
      console.log("no client");
      return {};
    }
    return client
      .getEntries({
        content_type: "markdownSection"
      })
      .then(sections => {
        return {
          sections: sections.items
        };
      })
      .catch(e => console.error(e));
  }
};
</script>

<style></style>
