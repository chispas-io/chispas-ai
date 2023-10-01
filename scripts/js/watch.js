const esbuild = require('esbuild');
const config = require('./config');

esbuild.context(config)
  .then((context) => {
    context.watch()
      .then(() => {
        console.log("Watching files ✨");
      });
  });
