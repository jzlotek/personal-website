import { client } from './plugins/contentful';


async function getBlogEntriesData() {
  let { items } = await client.getEntries({
    content_type: 'markdownSection',
  });
  items = items.map(section => {
    return {
      route: `/blog/${section.fields.slug}`,
      payload: section.fields,
    };
  });

  return items;
}

module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: 'John Zlotek',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'John Zlotek\'s personal website' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href: 'https://use.fontawesome.com/releases/v5.6.3/css/all.css' }
    ]
  },
  generate: {
    routes: function (cb) {
      getBlogEntriesData()
        .then(res => {cb(null, res)})
        .catch(cb);
    },
  },
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#3B8070' },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}

