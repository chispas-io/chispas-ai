// https://nightwatchjs.org/guide/configuration/nightwatch-configuration-file.html
module.exports = {
  // An array of folders (excluding subfolders) where your tests are located;
  // if this is not specified, the test source must be passed as the second argument to the test runner.
  src_folders: [],
  // See https://nightwatchjs.org/guide/concepts/page-object-model.html
  page_objects_path: [],
  // See https://nightwatchjs.org/guide/extending-nightwatch/adding-custom-commands.html
  custom_commands_path: ['nightwatch/custom-commands'],
  // See https://nightwatchjs.org/guide/extending-nightwatch/adding-custom-assertions.html
  custom_assertions_path: ['nightwatch/custom-assertions'],
  // See https://nightwatchjs.org/guide/extending-nightwatch/adding-plugins.html
  plugins: ['@nightwatch/vue'],
  // See https://nightwatchjs.org/guide/concepts/test-globals.html#external-test-globals
  globals_path: 'nightwatch/globals.js',
  vite_dev_server: {
    start_vite: false
  },
  webdriver: {},
  test_workers: {
    enabled: true,
    workers: 'auto'
  },
  test_settings: {
    default: {
      disable_error_log: false,
      launch_url: `http://localhost:${process.env.CI ? '4173' : '5173'}`,
      screenshots: {
        enabled: false,
        path: 'screens',
        on_failure: true
      },
      desiredCapabilities: {
        browserName: 'firefox'
      },
      webdriver: {
        start_process: true,
        server_path: ''
      }
    },
    safari: {
      desiredCapabilities: {
        browserName: 'safari',
        alwaysMatch: {
          acceptInsecureCerts: false
        }
      },
      webdriver: {
        start_process: true,
        server_path: ''
      }
    },
    firefox: {
      desiredCapabilities: {
        browserName: 'firefox',
        alwaysMatch: {
          acceptInsecureCerts: true,
          'moz:firefoxOptions': {
            args: [
              // '-headless',
              // '-verbose'
            ]
          }
        }
      },
      webdriver: {
        start_process: true,
        server_path: '',
        cli_args: [
          // very verbose geckodriver logs
          // '-vv'
        ]
      }
    },
  }
}
