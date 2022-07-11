/* eslint-disable no-param-reassign */
const debug = process.env.NODE_ENV !== "production";

module.exports = {
  reactStrictMode: true,
  exportPathMap() {
    return {
      "/": { page: "/" },
      "/deepmatcher": { page: "/deepmatcher" },
      "/finished": { page: "/finished" },
      "/pandas": { page: "/pandas" },
      "/postprocessing": { page: "/postprocessing" },
    };
  },
  assetPrefix: !debug ? "/interoperaNit/" : "",
  webpack: (config) => {
    config.module.rules = config.module.rules.map((rule) => {
      if (rule.loader === "babel-loader") {
        rule.options.cacheDirectory = false;
      }
      return rule;
    });
    return config;
  },
};
