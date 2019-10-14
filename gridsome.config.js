// This is where project configuration and plugin options are located. 
// Learn more: https://gridsome.org/docs/config

// Changes here requires a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

module.exports = {
  siteName: 'John Zlotek\'s Site',
  siteDescription: 'John Zlotek\'s personal website',
  plugins: [
      {
        use: 'gridsome-plugin-pwa',
        options: {
            title: 'johnzlotek.xyz',
            startUrl: '/',
            display: 'standalone',
            statusBarStyle: 'default',
            manifestPath: 'manifest.json',
            serviceWorkerPath: 'service-worker.js',
            shortName: 'jzxyz',
            themeColor: '#666600',
            backgroundColor: '#ffffff',
            icon: 'src/favicon.png'
        }
    }
  ],
}