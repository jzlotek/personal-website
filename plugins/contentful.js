const contentful = require('contentful');

let env;

try {
  env = require('../.contentful.json');
} catch (error) {
  env = {
    CONTENTFUL_SPACE_ID: process.env.CONTENTFUL_SPACE_ID,
    CONTENTFUL_ACCESS_TOKEN: process.env.CONTENTFUL_ACCESS_TOKEN
  }
}

const config = {
  space: env.CONTENTFUL_SPACE_ID,
  accessToken: env.CONTENTFUL_ACCESS_TOKEN,
};

module.exports = {
  createClient () {
    return contentful.createClient(config);
  }
}