var path = require( 'path' );
//var ExtractTextPlugin = require("extract-text-webpack-plugin");
//const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

var webpack = require('D:/coblan/webcode/node_modules/webpack')

//const VueLoaderPlugin = require('D:/coblan/webcode/node_modules/vue-loader/lib/plugin')
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports =
{
    mode: 'production',//'development', //
    //context:__dirname,
    entry: {
        myagora:'./main.js',
    },
    output: {
        path:path.resolve(__dirname, '../static/js'),
        filename: '[name].pack.js'
    },
    watch: true,
    resolve:{
        alias: {
            jb_admin: path.resolve(__dirname,"../../case/jb_admin/js")
        },
        modules:["D:/coblan/webcode/node_modules"],
    },
    resolveLoader: {
        //moduleExtensions:["D:/coblan/webcode/node_modules"],
        modules: ["D:/coblan/webcode/node_modules"],
        //resolver:["D:/coblan/webcode/node_modules"],
    },

    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.m?js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets:[
                            require.resolve('@babel/preset-env')
                        ]

                    }
                },
            },
            {
                test: /\.scss$/,
                use: [{
                    loader: "style-loader" // creates style nodes from JS strings
                }, {
                    loader: "css-loader" // translates CSS into CommonJS
                }, {
                    loader: "sass-loader" // compiles Sass to CSS
                }]
            },
            {
                test: /\.less$/,
                use: [{
                    loader: 'style-loader' // creates style nodes from JS strings
                }, {
                    loader: 'css-loader' // translates CSS into CommonJS
                }, {
                    loader: 'less-loader' // compiles Less to CSS
                }]
            }
        ]

    },
    plugins: [
        //new webpack.optimize.UglifyJsPlugin({  //压缩包
        //     compress: {
        //       warnings: false
        //     },
        //    sourceMap: true,
        //    mangle: false
        //}),

        new VueLoaderPlugin(),


        //new UglifyJSPlugin()
        //new webpack.DefinePlugin({
        //'process.env.NODE_ENV': JSON.stringify('production'),
        //}),
    ]
}



