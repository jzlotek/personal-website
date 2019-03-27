const contentful = require('contentful');
const cf = require('../.contentful.json')

const config = {
  space: cf.CONTENTFUL_SPACE_ID,
  accessToken: cf.CONTENTFUL_ACCESS_TOKEN,
};

export const client = contentful.createClient(config);