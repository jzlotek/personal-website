const contentful = require("contentful");
let c = null;

if (process.env.CONTENTFUL_ACCESS_TOKEN && process.env.CONTENTFUL_SPACE_ID) {
  const config = {
    space: String(process.env.CONTENTFUL_SPACE_ID).trim(),
    accessToken: String(process.env.CONTENTFUL_ACCESS_TOKEN).trim()
  };
  c = contentful.createClient(config);
}

export const client = c;
