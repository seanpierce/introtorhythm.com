const path = require('path');

module.exports = {
    watch: true,
    entry: './index.js',
    output: {
        filename: 'app.js',
        path: path.resolve(__dirname, "../assets/dist"),
    }
}