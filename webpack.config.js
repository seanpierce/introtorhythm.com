const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = (env, argv) => ({
    watch: argv.mode === 'development' ? true : false,
    context: __dirname,
    entry: './assets/js/index',
    output: {
        path: path.resolve('./assets/bundles/'),
        filename: 'app.js'
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new VueLoaderPlugin(),
    ],

    performance: { 
        hints: false 
    },

    module: {
        rules:  [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            }
        ],
    },
    resolve: {
        alias: {vue: 'vue/dist/vue.js'}
    },

});
