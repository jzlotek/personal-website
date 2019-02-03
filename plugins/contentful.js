const contentful = require('contentful');

const config = {
  space: env.CONTENTFUL_SPACE_ID,
  accessToken: env.CONTENTFUL_ACCESS_TOKEN,
};

export const client = contentful.createClient(config);