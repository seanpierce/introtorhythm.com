const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const isDevelopment = false;

module.exports = {
    watch: true,
    entry: ['./index.js', './index.scss'],
    output: {
        filename: 'app.js',
        path: path.resolve(__dirname, "../assets/dist"),
    },
    module: {
        rules: [
        {
            test: /\.module\.s(a|c)ss$/,
            loader: [
                {
                    loader: 'css-loader',
                    options: {
                    modules: true,
                    sourceMap: isDevelopment
                    }
                },
                {
                    loader: 'sass-loader',
                    options: {
                    sourceMap: isDevelopment
                    }
                }
                ]
            },
            {
                test: /\.s(a|c)ss$/,
                exclude: /\.module.(s(a|c)ss)$/,
                loader: [
                    isDevelopment ? 'style-loader' : MiniCssExtractPlugin.loader,
                    'css-loader',
                    {
                        loader: 'sass-loader',
                        options: {
                        sourceMap: isDevelopment
                        }
                    }
                ]
            }
        ],
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'app.css',
            chunkFilename: 'app.css'
        })
    ],
    resolve: {
        extensions: ['.js', '.scss']
    }
}