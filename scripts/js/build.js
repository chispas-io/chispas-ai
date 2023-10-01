const esbuild = require('esbuild');
const config = require('./config');

esbuild.build(config)
  .then(() => {
    console.log("Done compiling ✨");
  });
