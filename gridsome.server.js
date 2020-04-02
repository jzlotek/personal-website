const client = require('./src/plugins/contentful');
require('dotenv').config();
// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api

// Changes here requires a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

async function getRoutes() {
  const entries = await client.getEntries({
    content_type: "markdownSection"
  });

  const items = entries.items;
  const routeList = items.map((section) => {
      return {
        route: `/posts/${section.fields.slug}`,
        payload: section.fields,
      };
    })

  return routeList;
}

module.exports = function (api) {
  api.loadSource(async store => {
    const routes = await getRoutes();
    const contentType = store.addContentType({
      typeName: 'Post',
      route: '/posts/:id'
    })

    for (const item of routes) {
      contentType.addNode({
        id: item.payload.slug,
        title: item.payload.title,
        path: item.route,
        fields: {
          markdown: item.payload.markdown
        }
      })
    }
  })
}