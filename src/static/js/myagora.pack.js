/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./main.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "../../../../../../coblan/webcode/node_modules/babel-loader/lib/index.js?!../../../../../../coblan/webcode/node_modules/vue-loader/lib/index.js?!./rtc/rtc_send.vue?vue&type=script&lang=js&":
/*!*****************************************************************************************************************************************************************************!*\
  !*** D:/coblan/webcode/node_modules/babel-loader/lib??ref--1!D:/coblan/webcode/node_modules/vue-loader/lib??vue-loader-options!./rtc/rtc_send.vue?vue&type=script&lang=js& ***!
  \*****************************************************************************************************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n/* harmony default export */ __webpack_exports__[\"default\"] = ({\n  props: ['ctx'],\n  data: function data() {\n    return {\n      parStore: ex.vueParStore(this),\n      uid: '' + parseInt(Math.random() * 100000000),\n      appid: this.ctx.appid,\n      token: '',\n      client: '',\n      mp3_url: '',\n      channel: '',\n      started: false,\n      user_count: 0\n    };\n  },\n  mounted: function mounted() {\n    var _this = this;\n\n    this.$on('ready-send-order', function () {\n      _this.channel = '';\n      _this.token = '';\n      _this.mp3_url = '';\n      _this.started = false;\n\n      _this.parStore.option.sender_list.push(_this);\n    });\n    this.createClient().then(function () {\n      _this.$emit('ready-send-order');\n    });\n  },\n  methods: {\n    createClient: function createClient() {\n      var self = this;\n      self.client = AgoraRTC.createClient({\n        mode: \"rtc\",\n        codec: \"h264\"\n      });\n      return new Promise(function (resolve, reject) {\n        self.client.init(self.appid, function () {\n          console.log(\"init success\");\n          resolve();\n        }, function (err) {\n          console.error(\"client join failed\", err);\n          self.warning_log(\"\\u521D\\u59CB\\u5316client\\u5931\\u8D25:\".concat(err));\n        });\n      }); //                return new Promise((resolve,reject) =>{\n      //                            $.get('/dapi/agora/rtc-option?channel='+this.channel+'&uid='+this.uid,function(resp){\n      //                            self.token = resp.data.token\n      //                            self.appid = resp.data.appID\n      //                            resolve()\n      //                        })\n      //            }).then(()=>{\n      //                    self.client = AgoraRTC.createClient({mode: \"rtc\", codec: \"h264\"})\n      //                return new Promise((resolve,reject)=>{\n      //                            self.client.init(self.appid, function () {\n      //                            console.log(\"init success\");\n      //                            resolve()\n      //                        }, function(err) {\n      //                            console.error(\"client join failed\", err)\n      //                        })\n      //            })\n      //            })\n    },\n    debug_log: function debug_log(msg) {\n      ex.director_call('rtc_front_log', {\n        msg: msg,\n        level: 'DEBUG',\n        uid: this.uid\n      });\n    },\n    warning_log: function warning_log(msg) {\n      ex.director_call('rtc_front_log', {\n        msg: msg,\n        level: 'WARNING',\n        uid: this.uid\n      });\n    },\n    send: function send() {\n      var _this2 = this;\n\n      Promise.resolve().then(function () {\n        _this2.debug_log('开始加入频道' + _this2.channel);\n\n        return _this2.join();\n      }).then(function () {\n        return _this2.publish();\n      }).then(function () {\n        _this2.regist_event();\n\n        return _this2.success_publish();\n      }).then(function () {\n        _this2.debug_log('有用户接入，开始播放录音');\n\n        _this2.onstart();\n      });\n    },\n    join: function join() {\n      var _this3 = this;\n\n      var self = this;\n      return new Promise(function (resolve, reject) {\n        $.get('/dapi/agora/rtc-option?channel=' + _this3.channel + '&uid=' + _this3.uid, function (resp) {\n          self.token = resp.data.token;\n          resolve();\n        });\n      }).then(function () {\n        return new Promise(function (resolve, reject) {\n          _this3.client.join(_this3.token, _this3.channel, _this3.uid, function (uid) {\n            console.log(\"join channel: \" + _this3.channel + \" success, uid: \" + uid);\n            resolve();\n          }, function (err) {\n            console.error(\"client join failed\", err);\n          });\n        });\n      });\n    },\n    publish: function publish() {\n      var self = this;\n      return new Promise(function (resolve, reject) {\n        self.localStream = AgoraRTC.createStream({\n          streamID: self.uid,\n          audio: true,\n          video: false,\n          screen: false\n        });\n        self.localStream.init(function () {\n          console.log(\"初始化 local stream success\");\n          resolve();\n        }, function (err) {\n          console.error(\"初始化 local stream failed \", err);\n        });\n      }).then(function () {\n        // Publish the local stream\n        self.client.publish(self.localStream, function (err) {\n          console.log(\"发布 failed\");\n          console.error(err);\n        });\n      });\n    },\n    success_publish: function success_publish() {\n      var _this4 = this;\n\n      var self = this;\n      self.localStream.muteAudio();\n\n      if (/^http/.test(this.mp3_url)) {\n        var mp3_reach = '/relay?url=' + this.mp3_url;\n      } else {\n        var mp3_reach = this.mp3_url;\n      }\n\n      var options = {\n        cacheResource: true,\n        //                                        filePath: \"http://www.hochmuth.com/mp3/Haydn_Cello_Concerto_D-1.mp3\",\n        filePath: mp3_reach || '/static/Haydn_Cello_Concerto_D-1.mp3',\n        cycle: 1,\n        replace: true,\n        playTime: 0\n      };\n      self.localStream.startAudioMixing(options, function (err) {\n        if (err) {\n          self.warning_log(\"\\u64AD\\u653E\\u5F55\\u97F3\".concat(options.filePath, \"\\u9519\\u8BEF:\").concat(err));\n          console.log(\"Failed to start audio mixing. \" + err);\n        }\n      });\n      var p1 = new Promise(function (resolve, reject) {\n        self.localStream.on(\"audioMixingPlayed\", function () {\n          self.debug_log('加载录音完成!');\n\n          if (!self.started) {\n            self.localStream.pauseAudioMixing();\n            resolve();\n          }\n        });\n      });\n      var p2 = new Promise(function (resolve, reject) {\n        self.client.on(\"peer-online\", function () {\n          console.log('有人链接了。');\n          self.user_count += 1;\n\n          _this4.debug_log(\"新用户连接，当前连接数:\" + _this4.user_count);\n\n          if (!self.started) {\n            resolve(); // 播放音效\n            //                                    self.localStream.muteAudio()\n            //                                    self.localStream.playEffect({\n            //                                        soundId: 1,\n            ////                                        filePath: '/static/Haydn_Cello_Concerto_D-1.mp3'\n            //                                        filePath: 'http://www.hochmuth.com/mp3/Haydn_Cello_Concerto_D-1.mp3'\n            //                                    }, function(error) {\n            //                                        if (error) {\n            //                                            // 错误处理\n            //                                            return;\n            //                                        }\n            //                                        // 播放成功后的流程\n            //                                    });\n          }\n        });\n      });\n      return Promise.all([p1, p2]);\n    },\n    onstart: function onstart() {\n      this.debug_log(\"开始播放录音\" + this.user_count);\n      var self = this;\n      self.started = true;\n      self.localStream.unmuteAudio();\n      self.localStream.resumeAudioMixing();\n    },\n    regist_event: function regist_event() {\n      var _this5 = this;\n\n      var self = this;\n      self.client.on(\"peer-leave\", function () {\n        console.log('有人退出了。');\n        self.user_count -= 1;\n\n        if (self.user_count <= 0) {\n          console.log('所有人都退出了，现在退出'); //                        self.localStream.stopAllEffects()\n\n          self.localStream.muteAudio();\n          self.localStream.stopAudioMixing();\n          self.client.leave();\n\n          _this5.debug_log('所有人都退出了频道，现在退出');\n\n          self.$emit('ready-send-order');\n        }\n      });\n      setTimeout(function () {\n        if (!self.started) {\n          // 长时间无人接听，退出拨打\n          self.localStream.muteAudio();\n          self.localStream.stopAudioMixing();\n          self.client.leave();\n\n          _this5.debug_log('长时间无人接听，退出拨打!');\n\n          self.$emit('ready-send-order');\n        }\n      }, 1000 * 30);\n    }\n  }\n});\n\n//# sourceURL=webpack:///./rtc/rtc_send.vue?D:/coblan/webcode/node_modules/babel-loader/lib??ref--1!D:/coblan/webcode/node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "../../../../../../coblan/webcode/node_modules/babel-loader/lib/index.js?!../../../../../../coblan/webcode/node_modules/vue-loader/lib/index.js?!./rtc/rtc_trigger.vue?vue&type=script&lang=js&":
/*!********************************************************************************************************************************************************************************!*\
  !*** D:/coblan/webcode/node_modules/babel-loader/lib??ref--1!D:/coblan/webcode/node_modules/vue-loader/lib??vue-loader-options!./rtc/rtc_trigger.vue?vue&type=script&lang=js& ***!
  \********************************************************************************************************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n//\n//\n//\n/* harmony default export */ __webpack_exports__[\"default\"] = ({\n  data: function data() {\n    var parStore = ex.vueParStore(this);\n    Vue.set(parStore.option, 'sender_list', []);\n    return {\n      parStore: parStore,\n      task_list: []\n    };\n  },\n  mounted: function mounted() {\n    var self = this;\n\n    window.send_mp3 = function (channel, mp3_url) {\n      self.task_list.push({\n        channel: channel,\n        mp3_url: mp3_url\n      });\n    };\n\n    setInterval(self.pump, 500);\n  },\n  computed: {\n    sender_count: function sender_count() {\n      return this.parStore.option.sender_list.length;\n    }\n  },\n  methods: {\n    warning_log: function warning_log(msg) {\n      ex.director_call('rtc_front_log', {\n        msg: msg,\n        level: 'WARNING',\n        uid: 'trigger'\n      });\n    },\n    pump: function pump() {\n      if (this.task_list.length > 0) {\n        var sender = this.get_valid_sender();\n\n        if (sender) {\n          var task = this.task_list[0];\n          this.task_list.splice(0, 1);\n          sender.channel = task.channel;\n          sender.mp3_url = task.mp3_url;\n          sender.send();\n          this.pump();\n        } else {\n          this.warning_log('没有可用的sender');\n        }\n      } else {}\n    },\n    get_valid_sender: function get_valid_sender() {\n      if (this.parStore.option.sender_list.length > 0) {\n        var mm = this.parStore.option.sender_list[0];\n        this.parStore.option.sender_list.splice(0, 1);\n        return mm;\n      } else {}\n    }\n  }\n});\n\n//# sourceURL=webpack:///./rtc/rtc_trigger.vue?D:/coblan/webcode/node_modules/babel-loader/lib??ref--1!D:/coblan/webcode/node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "../../../../../../coblan/webcode/node_modules/css-loader/index.js!../../../../../../coblan/webcode/node_modules/vue-loader/lib/loaders/stylePostLoader.js!../../../../../../coblan/webcode/node_modules/sass-loader/lib/loader.js!../../../../../../coblan/webcode/node_modules/vue-loader/lib/index.js?!./rtc/rtc_send.vue?vue&type=style&index=0&id=68720f22&scoped=true&lang=scss&":
/*!**********************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** D:/coblan/webcode/node_modules/css-loader!D:/coblan/webcode/node_modules/vue-loader/lib/loaders/stylePostLoader.js!D:/coblan/webcode/node_modules/sass-loader/lib/loader.js!D:/coblan/webcode/node_modules/vue-loader/lib??vue-loader-options!./rtc/rtc_send.vue?vue&type=style&index=0&id=68720f22&scoped=true&lang=scss& ***!
  \**********************************************************************************************************************************************************************************************************************************************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("exports = module.exports = __webpack_require__(/*! ../../../../../../../coblan/webcode/node_modules/css-loader/lib/css-base.js */ \"../../../../../../coblan/webcode/node_modules/css-loader/lib/css-base.js\")();\n// imports\n\n\n// module\nexports.push([module.i, \".com-rtc-send[data-v-68720f22] {\\n  display: inline-block;\\n  width: 260px;\\n  border: 1px solid grey;\\n}\\n\", \"\"]);\n\n// exports\n\n\n//# sourceURL=webpack:///./rtc/rtc_send.vue?D:/coblan/webcode/node_modules/css-loader!D:/coblan/webcode/node_modules/vue-loader/lib/loaders/stylePostLoader.js!D:/coblan/webcode/node_modules/sass-loader/lib/loader.js!D:/coblan/webcode/node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "../../../../../../coblan/webcode/node_modules/css-loader/lib/css-base.js":
/*!*****************************************************************!*\
  !*** D:/coblan/webcode/node_modules/css-loader/lib/css-base.js ***!
  \*****************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("/*\n\tMIT License http://www.opensource.org/licenses/mit-license.php\n\tAuthor Tobias Koppers @sokra\n*/\n// css base code, injected by the css-loader\nmodule.exports = function() {\n\tvar list = [];\n\n\t// return the list of modules as css string\n\tlist.toString = function toString() {\n\t\tvar result = [];\n\t\tfor(var i = 0; i < this.length; i++) {\n\t\t\tvar item = this[i];\n\t\t\tif(item[2]) {\n\t\t\t\tresult.push(\"@media \" + item[2] + \"{\" + item[1] + \"}\");\n\t\t\t} else {\n\t\t\t\tresult.push(item[1]);\n\t\t\t}\n\t\t}\n\t\treturn result.join(\"\");\n\t};\n\n\t// import a list of modules into the list\n\tlist.i = function(modules, mediaQuery) {\n\t\tif(typeof modules === \"string\")\n\t\t\tmodules = [[null, modules, \"\"]];\n\t\tvar alreadyImportedModules = {};\n\t\tfor(var i = 0; i < this.length; i++) {\n\t\t\tvar id = this[i][0];\n\t\t\tif(typeof id === \"number\")\n\t\t\t\talreadyImportedModules[id] = true;\n\t\t}\n\t\tfor(i = 0; i < modules.length; i++) {\n\t\t\tvar item = modules[i];\n\t\t\t// skip already imported module\n\t\t\t// this implementation is not 100% perfect for weird media query combinations\n\t\t\t//  when a module is imported multiple times with different media queries.\n\t\t\t//  I hope this will never occur (Hey this way we have smaller bundles)\n\t\t\tif(typeof item[0] !== \"number\" || !alreadyImportedModules[item[0]]) {\n\t\t\t\tif(mediaQuery && !item[2]) {\n\t\t\t\t\titem[2] = mediaQuery;\n\t\t\t\t} else if(mediaQuery) {\n\t\t\t\t\titem[2] = \"(\" + item[2] + \") and (\" + mediaQuery + \")\";\n\t\t\t\t}\n\t\t\t\tlist.push(item);\n\t\t\t}\n\t\t}\n\t};\n\treturn list;\n};\n\n\n//# sourceURL=webpack:///D:/coblan/webcode/node_modules/css-loader/lib/css-base.js?");

/***/ }),

/***/ "../../../../../../coblan/webcode/node_modules/style-loader/addStyles.js":
/*!****************************************************************!*\
  !*** D:/coblan/webcode/node_modules/style-loader/addStyles.js ***!
  \****************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("/*\n\tMIT License http://www.opensource.org/licenses/mit-license.php\n\tAuthor Tobias Koppers @sokra\n*/\nvar stylesInDom = {},\n\tmemoize = function(fn) {\n\t\tvar memo;\n\t\treturn function () {\n\t\t\tif (typeof memo === \"undefined\") memo = fn.apply(this, arguments);\n\t\t\treturn memo;\n\t\t};\n\t},\n\tisOldIE = memoize(function() {\n\t\treturn /msie [6-9]\\b/.test(self.navigator.userAgent.toLowerCase());\n\t}),\n\tgetHeadElement = memoize(function () {\n\t\treturn document.head || document.getElementsByTagName(\"head\")[0];\n\t}),\n\tsingletonElement = null,\n\tsingletonCounter = 0,\n\tstyleElementsInsertedAtTop = [];\n\nmodule.exports = function(list, options) {\n\tif(typeof DEBUG !== \"undefined\" && DEBUG) {\n\t\tif(typeof document !== \"object\") throw new Error(\"The style-loader cannot be used in a non-browser environment\");\n\t}\n\n\toptions = options || {};\n\t// Force single-tag solution on IE6-9, which has a hard limit on the # of <style>\n\t// tags it will allow on a page\n\tif (typeof options.singleton === \"undefined\") options.singleton = isOldIE();\n\n\t// By default, add <style> tags to the bottom of <head>.\n\tif (typeof options.insertAt === \"undefined\") options.insertAt = \"bottom\";\n\n\tvar styles = listToStyles(list);\n\taddStylesToDom(styles, options);\n\n\treturn function update(newList) {\n\t\tvar mayRemove = [];\n\t\tfor(var i = 0; i < styles.length; i++) {\n\t\t\tvar item = styles[i];\n\t\t\tvar domStyle = stylesInDom[item.id];\n\t\t\tdomStyle.refs--;\n\t\t\tmayRemove.push(domStyle);\n\t\t}\n\t\tif(newList) {\n\t\t\tvar newStyles = listToStyles(newList);\n\t\t\taddStylesToDom(newStyles, options);\n\t\t}\n\t\tfor(var i = 0; i < mayRemove.length; i++) {\n\t\t\tvar domStyle = mayRemove[i];\n\t\t\tif(domStyle.refs === 0) {\n\t\t\t\tfor(var j = 0; j < domStyle.parts.length; j++)\n\t\t\t\t\tdomStyle.parts[j]();\n\t\t\t\tdelete stylesInDom[domStyle.id];\n\t\t\t}\n\t\t}\n\t};\n}\n\nfunction addStylesToDom(styles, options) {\n\tfor(var i = 0; i < styles.length; i++) {\n\t\tvar item = styles[i];\n\t\tvar domStyle = stylesInDom[item.id];\n\t\tif(domStyle) {\n\t\t\tdomStyle.refs++;\n\t\t\tfor(var j = 0; j < domStyle.parts.length; j++) {\n\t\t\t\tdomStyle.parts[j](item.parts[j]);\n\t\t\t}\n\t\t\tfor(; j < item.parts.length; j++) {\n\t\t\t\tdomStyle.parts.push(addStyle(item.parts[j], options));\n\t\t\t}\n\t\t} else {\n\t\t\tvar parts = [];\n\t\t\tfor(var j = 0; j < item.parts.length; j++) {\n\t\t\t\tparts.push(addStyle(item.parts[j], options));\n\t\t\t}\n\t\t\tstylesInDom[item.id] = {id: item.id, refs: 1, parts: parts};\n\t\t}\n\t}\n}\n\nfunction listToStyles(list) {\n\tvar styles = [];\n\tvar newStyles = {};\n\tfor(var i = 0; i < list.length; i++) {\n\t\tvar item = list[i];\n\t\tvar id = item[0];\n\t\tvar css = item[1];\n\t\tvar media = item[2];\n\t\tvar sourceMap = item[3];\n\t\tvar part = {css: css, media: media, sourceMap: sourceMap};\n\t\tif(!newStyles[id])\n\t\t\tstyles.push(newStyles[id] = {id: id, parts: [part]});\n\t\telse\n\t\t\tnewStyles[id].parts.push(part);\n\t}\n\treturn styles;\n}\n\nfunction insertStyleElement(options, styleElement) {\n\tvar head = getHeadElement();\n\tvar lastStyleElementInsertedAtTop = styleElementsInsertedAtTop[styleElementsInsertedAtTop.length - 1];\n\tif (options.insertAt === \"top\") {\n\t\tif(!lastStyleElementInsertedAtTop) {\n\t\t\thead.insertBefore(styleElement, head.firstChild);\n\t\t} else if(lastStyleElementInsertedAtTop.nextSibling) {\n\t\t\thead.insertBefore(styleElement, lastStyleElementInsertedAtTop.nextSibling);\n\t\t} else {\n\t\t\thead.appendChild(styleElement);\n\t\t}\n\t\tstyleElementsInsertedAtTop.push(styleElement);\n\t} else if (options.insertAt === \"bottom\") {\n\t\thead.appendChild(styleElement);\n\t} else {\n\t\tthrow new Error(\"Invalid value for parameter 'insertAt'. Must be 'top' or 'bottom'.\");\n\t}\n}\n\nfunction removeStyleElement(styleElement) {\n\tstyleElement.parentNode.removeChild(styleElement);\n\tvar idx = styleElementsInsertedAtTop.indexOf(styleElement);\n\tif(idx >= 0) {\n\t\tstyleElementsInsertedAtTop.splice(idx, 1);\n\t}\n}\n\nfunction createStyleElement(options) {\n\tvar styleElement = document.createElement(\"style\");\n\tstyleElement.type = \"text/css\";\n\tinsertStyleElement(options, styleElement);\n\treturn styleElement;\n}\n\nfunction createLinkElement(options) {\n\tvar linkElement = document.createElement(\"link\");\n\tlinkElement.rel = \"stylesheet\";\n\tinsertStyleElement(options, linkElement);\n\treturn linkElement;\n}\n\nfunction addStyle(obj, options) {\n\tvar styleElement, update, remove;\n\n\tif (options.singleton) {\n\t\tvar styleIndex = singletonCounter++;\n\t\tstyleElement = singletonElement || (singletonElement = createStyleElement(options));\n\t\tupdate = applyToSingletonTag.bind(null, styleElement, styleIndex, false);\n\t\tremove = applyToSingletonTag.bind(null, styleElement, styleIndex, true);\n\t} else if(obj.sourceMap &&\n\t\ttypeof URL === \"function\" &&\n\t\ttypeof URL.createObjectURL === \"function\" &&\n\t\ttypeof URL.revokeObjectURL === \"function\" &&\n\t\ttypeof Blob === \"function\" &&\n\t\ttypeof btoa === \"function\") {\n\t\tstyleElement = createLinkElement(options);\n\t\tupdate = updateLink.bind(null, styleElement);\n\t\tremove = function() {\n\t\t\tremoveStyleElement(styleElement);\n\t\t\tif(styleElement.href)\n\t\t\t\tURL.revokeObjectURL(styleElement.href);\n\t\t};\n\t} else {\n\t\tstyleElement = createStyleElement(options);\n\t\tupdate = applyToTag.bind(null, styleElement);\n\t\tremove = function() {\n\t\t\tremoveStyleElement(styleElement);\n\t\t};\n\t}\n\n\tupdate(obj);\n\n\treturn function updateStyle(newObj) {\n\t\tif(newObj) {\n\t\t\tif(newObj.css === obj.css && newObj.media === obj.media && newObj.sourceMap === obj.sourceMap)\n\t\t\t\treturn;\n\t\t\tupdate(obj = newObj);\n\t\t} else {\n\t\t\tremove();\n\t\t}\n\t};\n}\n\nvar replaceText = (function () {\n\tvar textStore = [];\n\n\treturn function (index, replacement) {\n\t\ttextStore[index] = replacement;\n\t\treturn textStore.filter(Boolean).join('\\n');\n\t};\n})();\n\nfunction applyToSingletonTag(styleElement, index, remove, obj) {\n\tvar css = remove ? \"\" : obj.css;\n\n\tif (styleElement.styleSheet) {\n\t\tstyleElement.styleSheet.cssText = replaceText(index, css);\n\t} else {\n\t\tvar cssNode = document.createTextNode(css);\n\t\tvar childNodes = styleElement.childNodes;\n\t\tif (childNodes[index]) styleElement.removeChild(childNodes[index]);\n\t\tif (childNodes.length) {\n\t\t\tstyleElement.insertBefore(cssNode, childNodes[index]);\n\t\t} else {\n\t\t\tstyleElement.appendChild(cssNode);\n\t\t}\n\t}\n}\n\nfunction applyToTag(styleElement, obj) {\n\tvar css = obj.css;\n\tvar media = obj.media;\n\n\tif(media) {\n\t\tstyleElement.setAttribute(\"media\", media)\n\t}\n\n\tif(styleElement.styleSheet) {\n\t\tstyleElement.styleSheet.cssText = css;\n\t} else {\n\t\twhile(styleElement.firstChild) {\n\t\t\tstyleElement.removeChild(styleElement.firstChild);\n\t\t}\n\t\tstyleElement.appendChild(document.createTextNode(css));\n\t}\n}\n\nfunction updateLink(linkElement, obj) {\n\tvar css = obj.css;\n\tvar sourceMap = obj.sourceMap;\n\n\tif(sourceMap) {\n\t\t// http://stackoverflow.com/a/26603875\n\t\tcss += \"\\n/*# sourceMappingURL=data:application/json;base64,\" + btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap)))) + \" */\";\n\t}\n\n\tvar blob = new Blob([css], { type: \"text/css\" });\n\n\tvar oldSrc = linkElement.href;\n\n\tlinkElement.href = URL.createObjectURL(blob);\n\n\tif(oldSrc)\n\t\tURL.revokeObjectURL(oldSrc);\n}\n\n\n//# sourceURL=webpack:///D:/coblan/webcode/node_modules/style-loader/addStyles.js?");

/***/ }),

/***/ "../../../../../../coblan/webcode/node_modules/style-loader/index.js!../../../../../../coblan/webcode/node_modules/css-loader/index.js!../../../../../../coblan/webcode/node_modules/vue-loader/lib/loaders/stylePostLoader.js!../../../../../../coblan/webcode/node_modules/sass-loader/lib/loader.js!../../../../../../coblan/webcode/node_modules/vue-loader/lib/index.js?!./rtc/rtc_send.vue?vue&type=style&index=0&id=68720f22&scoped=true&lang=scss&":
/*!******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** D:/coblan/webcode/node_modules/style-loader!D:/coblan/webcode/node_modules/css-loader!D:/coblan/webcode/node_modules/vue-loader/lib/loaders/stylePostLoader.js!D:/coblan/webcode/node_modules/sass-loader/lib/loader.js!D:/coblan/webcode/node_modules/vue-loader/lib??vue-loader-options!./rtc/rtc_send.vue?vue&type=style&index=0&id=68720f22&scoped=true&lang=scss& ***!
  \******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("// style-loader: Adds some css to the DOM by adding a <style> tag\n\n// load the styles\nvar content = __webpack_require__(/*! !../../../../../../../coblan/webcode/node_modules/css-loader!../../../../../../../coblan/webcode/node_modules/vue-loader/lib/loaders/stylePostLoader.js!../../../../../../../coblan/webcode/node_modules/sass-loader/lib/loader.js!../../../../../../../coblan/webcode/node_modules/vue-loader/lib??vue-loader-options!./rtc_send.vue?vue&type=style&index=0&id=68720f22&scoped=true&lang=scss& */ \"../../../../../../coblan/webcode/node_modules/css-loader/index.js!../../../../../../coblan/webcode/node_modules/vue-loader/lib/loaders/stylePostLoader.js!../../../../../../coblan/webcode/node_modules/sass-loader/lib/loader.js!../../../../../../coblan/webcode/node_modules/vue-loader/lib/index.js?!./rtc/rtc_send.vue?vue&type=style&index=0&id=68720f22&scoped=true&lang=scss&\");\nif(typeof content === 'string') content = [[module.i, content, '']];\n// add the styles to the DOM\nvar update = __webpack_require__(/*! ../../../../../../../coblan/webcode/node_modules/style-loader/addStyles.js */ \"../../../../../../coblan/webcode/node_modules/style-loader/addStyles.js\")(content, {});\nif(content.locals) module.exports = content.locals;\n// Hot Module Replacement\nif(false) {}\n\n//# sourceURL=webpack:///./rtc/rtc_send.vue?D:/coblan/webcode/node_modules/style-loader!D:/coblan/webcode/node_modules/css-loader!D:/coblan/webcode/node_modules/vue-loader/lib/loaders/stylePostLoader.js!D:/coblan/webcode/node_modules/sass-loader/lib/loader.js!D:/coblan/webcode/node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "../../../../../../coblan/webcode/node_modules/vue-loader/lib/loaders/templateLoader.js?!../../../../../../coblan/webcode/node_modules/vue-loader/lib/index.js?!./rtc/rtc_send.vue?vue&type=template&id=68720f22&scoped=true&":
/*!***********************************************************************************************************************************************************************************************************************************!*\
  !*** D:/coblan/webcode/node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!D:/coblan/webcode/node_modules/vue-loader/lib??vue-loader-options!./rtc/rtc_send.vue?vue&type=template&id=68720f22&scoped=true& ***!
  \***********************************************************************************************************************************************************************************************************************************/
/*! exports provided: render, staticRenderFns */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"render\", function() { return render; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"staticRenderFns\", function() { return staticRenderFns; });\nvar render = function() {\n  var _vm = this\n  var _h = _vm.$createElement\n  var _c = _vm._self._c || _h\n  return _c(\"div\", { staticClass: \"com-rtc-send\" }, [\n    _c(\"div\", [\n      _c(\"span\", [_vm._v(\"appID\")]),\n      _vm._v(\" \"),\n      _c(\"span\", { domProps: { textContent: _vm._s(_vm.appid) } })\n    ]),\n    _vm._v(\" \"),\n    _c(\"div\", [\n      _c(\"span\", [_vm._v(\"uid\")]),\n      _vm._v(\" \"),\n      _c(\"input\", {\n        directives: [\n          {\n            name: \"model\",\n            rawName: \"v-model\",\n            value: _vm.uid,\n            expression: \"uid\"\n          }\n        ],\n        attrs: { type: \"text\", disabled: \"\" },\n        domProps: { value: _vm.uid },\n        on: {\n          input: function($event) {\n            if ($event.target.composing) {\n              return\n            }\n            _vm.uid = $event.target.value\n          }\n        }\n      })\n    ]),\n    _vm._v(\" \"),\n    _c(\"div\", [\n      _c(\"span\", [_vm._v(\"token\")]),\n      _vm._v(\" \"),\n      _c(\"input\", {\n        directives: [\n          {\n            name: \"model\",\n            rawName: \"v-model\",\n            value: _vm.token,\n            expression: \"token\"\n          }\n        ],\n        attrs: { type: \"text\", disabled: \"\" },\n        domProps: { value: _vm.token },\n        on: {\n          input: function($event) {\n            if ($event.target.composing) {\n              return\n            }\n            _vm.token = $event.target.value\n          }\n        }\n      })\n    ]),\n    _vm._v(\" \"),\n    _c(\"div\", [\n      _c(\"span\", [_vm._v(\"状态\")]),\n      _vm._v(\" \"),\n      _vm.started\n        ? _c(\"span\", { staticStyle: { color: \"#0ff537\" } }, [_vm._v(\"在线\")])\n        : _c(\"span\", [_vm._v(\"离线\")])\n    ]),\n    _vm._v(\" \"),\n    _c(\"div\", [\n      _c(\"span\", [_vm._v(\"人数\")]),\n      _vm._v(\" \"),\n      _c(\"span\", { domProps: { textContent: _vm._s(_vm.user_count) } })\n    ]),\n    _vm._v(\" \"),\n    _c(\"div\", [\n      _c(\"span\", [_vm._v(\"url\")]),\n      _vm._v(\" \"),\n      _c(\"span\", { domProps: { textContent: _vm._s(_vm.mp3_url) } })\n    ]),\n    _vm._v(\" \"),\n    _c(\"div\", [\n      _c(\"span\", [_vm._v(\"channel\")]),\n      _vm._v(\" \"),\n      _c(\"span\", { domProps: { textContent: _vm._s(_vm.channel) } })\n    ])\n  ])\n}\nvar staticRenderFns = []\nrender._withStripped = true\n\n\n\n//# sourceURL=webpack:///./rtc/rtc_send.vue?D:/coblan/webcode/node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!D:/coblan/webcode/node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "../../../../../../coblan/webcode/node_modules/vue-loader/lib/loaders/templateLoader.js?!../../../../../../coblan/webcode/node_modules/vue-loader/lib/index.js?!./rtc/rtc_trigger.vue?vue&type=template&id=6a1b240e&":
/*!**************************************************************************************************************************************************************************************************************************!*\
  !*** D:/coblan/webcode/node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!D:/coblan/webcode/node_modules/vue-loader/lib??vue-loader-options!./rtc/rtc_trigger.vue?vue&type=template&id=6a1b240e& ***!
  \**************************************************************************************************************************************************************************************************************************/
/*! exports provided: render, staticRenderFns */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"render\", function() { return render; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"staticRenderFns\", function() { return staticRenderFns; });\nvar render = function() {\n  var _vm = this\n  var _h = _vm.$createElement\n  var _c = _vm._self._c || _h\n  return _c(\"div\", [\n    _vm._v(\"trigger 样例 \"),\n    _c(\"span\", { domProps: { textContent: _vm._s(_vm.sender_count) } })\n  ])\n}\nvar staticRenderFns = []\nrender._withStripped = true\n\n\n\n//# sourceURL=webpack:///./rtc/rtc_trigger.vue?D:/coblan/webcode/node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!D:/coblan/webcode/node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "../../../../../../coblan/webcode/node_modules/vue-loader/lib/runtime/componentNormalizer.js":
/*!************************************************************************************!*\
  !*** D:/coblan/webcode/node_modules/vue-loader/lib/runtime/componentNormalizer.js ***!
  \************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"default\", function() { return normalizeComponent; });\n/* globals __VUE_SSR_CONTEXT__ */\n\n// IMPORTANT: Do NOT use ES2015 features in this file (except for modules).\n// This module is a runtime utility for cleaner component module output and will\n// be included in the final webpack user bundle.\n\nfunction normalizeComponent (\n  scriptExports,\n  render,\n  staticRenderFns,\n  functionalTemplate,\n  injectStyles,\n  scopeId,\n  moduleIdentifier, /* server only */\n  shadowMode /* vue-cli only */\n) {\n  // Vue.extend constructor export interop\n  var options = typeof scriptExports === 'function'\n    ? scriptExports.options\n    : scriptExports\n\n  // render functions\n  if (render) {\n    options.render = render\n    options.staticRenderFns = staticRenderFns\n    options._compiled = true\n  }\n\n  // functional template\n  if (functionalTemplate) {\n    options.functional = true\n  }\n\n  // scopedId\n  if (scopeId) {\n    options._scopeId = 'data-v-' + scopeId\n  }\n\n  var hook\n  if (moduleIdentifier) { // server build\n    hook = function (context) {\n      // 2.3 injection\n      context =\n        context || // cached call\n        (this.$vnode && this.$vnode.ssrContext) || // stateful\n        (this.parent && this.parent.$vnode && this.parent.$vnode.ssrContext) // functional\n      // 2.2 with runInNewContext: true\n      if (!context && typeof __VUE_SSR_CONTEXT__ !== 'undefined') {\n        context = __VUE_SSR_CONTEXT__\n      }\n      // inject component styles\n      if (injectStyles) {\n        injectStyles.call(this, context)\n      }\n      // register component module identifier for async chunk inferrence\n      if (context && context._registeredComponents) {\n        context._registeredComponents.add(moduleIdentifier)\n      }\n    }\n    // used by ssr in case component is cached and beforeCreate\n    // never gets called\n    options._ssrRegister = hook\n  } else if (injectStyles) {\n    hook = shadowMode\n      ? function () { injectStyles.call(this, this.$root.$options.shadowRoot) }\n      : injectStyles\n  }\n\n  if (hook) {\n    if (options.functional) {\n      // for template-only hot-reload because in that case the render fn doesn't\n      // go through the normalizer\n      options._injectStyles = hook\n      // register for functioal component in vue file\n      var originalRender = options.render\n      options.render = function renderWithStyleInjection (h, context) {\n        hook.call(context)\n        return originalRender(h, context)\n      }\n    } else {\n      // inject component registration as beforeCreate hook\n      var existing = options.beforeCreate\n      options.beforeCreate = existing\n        ? [].concat(existing, hook)\n        : [hook]\n    }\n  }\n\n  return {\n    exports: scriptExports,\n    options: options\n  }\n}\n\n\n//# sourceURL=webpack:///D:/coblan/webcode/node_modules/vue-loader/lib/runtime/componentNormalizer.js?");

/***/ }),

/***/ "./main.js":
/*!*****************!*\
  !*** ./main.js ***!
  \*****************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _rtc_rtc_send_vue__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./rtc/rtc_send.vue */ \"./rtc/rtc_send.vue\");\n/* harmony import */ var _rtc_rtc_trigger_vue__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./rtc/rtc_trigger.vue */ \"./rtc/rtc_trigger.vue\");\n\n\nVue.component('com-rtc-trigger', _rtc_rtc_trigger_vue__WEBPACK_IMPORTED_MODULE_1__[\"default\"]);\nVue.component('com-rtc-send', function (resolve, reject) {\n  ex.load_js('https://cdn.agora.io/sdk/release/AgoraRTCSDK-3.0.0.js').then(function () {\n    resolve(_rtc_rtc_send_vue__WEBPACK_IMPORTED_MODULE_0__[\"default\"]);\n  });\n}); //import * as pig from './elk'\n\n//# sourceURL=webpack:///./main.js?");

/***/ }),

/***/ "./rtc/rtc_send.vue":
/*!**************************!*\
  !*** ./rtc/rtc_send.vue ***!
  \**************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _rtc_send_vue_vue_type_template_id_68720f22_scoped_true___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./rtc_send.vue?vue&type=template&id=68720f22&scoped=true& */ \"./rtc/rtc_send.vue?vue&type=template&id=68720f22&scoped=true&\");\n/* harmony import */ var _rtc_send_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./rtc_send.vue?vue&type=script&lang=js& */ \"./rtc/rtc_send.vue?vue&type=script&lang=js&\");\n/* empty/unused harmony star reexport *//* harmony import */ var _rtc_send_vue_vue_type_style_index_0_id_68720f22_scoped_true_lang_scss___WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./rtc_send.vue?vue&type=style&index=0&id=68720f22&scoped=true&lang=scss& */ \"./rtc/rtc_send.vue?vue&type=style&index=0&id=68720f22&scoped=true&lang=scss&\");\n/* harmony import */ var _coblan_webcode_node_modules_vue_loader_lib_runtime_componentNormalizer_js__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../../../../../../coblan/webcode/node_modules/vue-loader/lib/runtime/componentNormalizer.js */ \"../../../../../../coblan/webcode/node_modules/vue-loader/lib/runtime/componentNormalizer.js\");\n\n\n\n\n\n\n/* normalize component */\n\nvar component = Object(_coblan_webcode_node_modules_vue_loader_lib_runtime_componentNormalizer_js__WEBPACK_IMPORTED_MODULE_3__[\"default\"])(\n  _rtc_send_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_1__[\"default\"],\n  _rtc_send_vue_vue_type_template_id_68720f22_scoped_true___WEBPACK_IMPORTED_MODULE_0__[\"render\"],\n  _rtc_send_vue_vue_type_template_id_68720f22_scoped_true___WEBPACK_IMPORTED_MODULE_0__[\"staticRenderFns\"],\n  false,\n  null,\n  \"68720f22\",\n  null\n  \n)\n\n/* hot reload */\nif (false) { var api; }\ncomponent.options.__file = \"rtc/rtc_send.vue\"\n/* harmony default export */ __webpack_exports__[\"default\"] = (component.exports);\n\n//# sourceURL=webpack:///./rtc/rtc_send.vue?");

/***/ }),

/***/ "./rtc/rtc_send.vue?vue&type=script&lang=js&":
/*!***************************************************!*\
  !*** ./rtc/rtc_send.vue?vue&type=script&lang=js& ***!
  \***************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _coblan_webcode_node_modules_babel_loader_lib_index_js_ref_1_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_send_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! -!../../../../../../../coblan/webcode/node_modules/babel-loader/lib??ref--1!../../../../../../../coblan/webcode/node_modules/vue-loader/lib??vue-loader-options!./rtc_send.vue?vue&type=script&lang=js& */ \"../../../../../../coblan/webcode/node_modules/babel-loader/lib/index.js?!../../../../../../coblan/webcode/node_modules/vue-loader/lib/index.js?!./rtc/rtc_send.vue?vue&type=script&lang=js&\");\n/* empty/unused harmony star reexport */ /* harmony default export */ __webpack_exports__[\"default\"] = (_coblan_webcode_node_modules_babel_loader_lib_index_js_ref_1_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_send_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_0__[\"default\"]); \n\n//# sourceURL=webpack:///./rtc/rtc_send.vue?");

/***/ }),

/***/ "./rtc/rtc_send.vue?vue&type=style&index=0&id=68720f22&scoped=true&lang=scss&":
/*!************************************************************************************!*\
  !*** ./rtc/rtc_send.vue?vue&type=style&index=0&id=68720f22&scoped=true&lang=scss& ***!
  \************************************************************************************/
/*! no static exports found */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _coblan_webcode_node_modules_style_loader_index_js_coblan_webcode_node_modules_css_loader_index_js_coblan_webcode_node_modules_vue_loader_lib_loaders_stylePostLoader_js_coblan_webcode_node_modules_sass_loader_lib_loader_js_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_send_vue_vue_type_style_index_0_id_68720f22_scoped_true_lang_scss___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! -!../../../../../../../coblan/webcode/node_modules/style-loader!../../../../../../../coblan/webcode/node_modules/css-loader!../../../../../../../coblan/webcode/node_modules/vue-loader/lib/loaders/stylePostLoader.js!../../../../../../../coblan/webcode/node_modules/sass-loader/lib/loader.js!../../../../../../../coblan/webcode/node_modules/vue-loader/lib??vue-loader-options!./rtc_send.vue?vue&type=style&index=0&id=68720f22&scoped=true&lang=scss& */ \"../../../../../../coblan/webcode/node_modules/style-loader/index.js!../../../../../../coblan/webcode/node_modules/css-loader/index.js!../../../../../../coblan/webcode/node_modules/vue-loader/lib/loaders/stylePostLoader.js!../../../../../../coblan/webcode/node_modules/sass-loader/lib/loader.js!../../../../../../coblan/webcode/node_modules/vue-loader/lib/index.js?!./rtc/rtc_send.vue?vue&type=style&index=0&id=68720f22&scoped=true&lang=scss&\");\n/* harmony import */ var _coblan_webcode_node_modules_style_loader_index_js_coblan_webcode_node_modules_css_loader_index_js_coblan_webcode_node_modules_vue_loader_lib_loaders_stylePostLoader_js_coblan_webcode_node_modules_sass_loader_lib_loader_js_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_send_vue_vue_type_style_index_0_id_68720f22_scoped_true_lang_scss___WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_coblan_webcode_node_modules_style_loader_index_js_coblan_webcode_node_modules_css_loader_index_js_coblan_webcode_node_modules_vue_loader_lib_loaders_stylePostLoader_js_coblan_webcode_node_modules_sass_loader_lib_loader_js_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_send_vue_vue_type_style_index_0_id_68720f22_scoped_true_lang_scss___WEBPACK_IMPORTED_MODULE_0__);\n/* harmony reexport (unknown) */ for(var __WEBPACK_IMPORT_KEY__ in _coblan_webcode_node_modules_style_loader_index_js_coblan_webcode_node_modules_css_loader_index_js_coblan_webcode_node_modules_vue_loader_lib_loaders_stylePostLoader_js_coblan_webcode_node_modules_sass_loader_lib_loader_js_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_send_vue_vue_type_style_index_0_id_68720f22_scoped_true_lang_scss___WEBPACK_IMPORTED_MODULE_0__) if(__WEBPACK_IMPORT_KEY__ !== 'default') (function(key) { __webpack_require__.d(__webpack_exports__, key, function() { return _coblan_webcode_node_modules_style_loader_index_js_coblan_webcode_node_modules_css_loader_index_js_coblan_webcode_node_modules_vue_loader_lib_loaders_stylePostLoader_js_coblan_webcode_node_modules_sass_loader_lib_loader_js_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_send_vue_vue_type_style_index_0_id_68720f22_scoped_true_lang_scss___WEBPACK_IMPORTED_MODULE_0__[key]; }) }(__WEBPACK_IMPORT_KEY__));\n /* harmony default export */ __webpack_exports__[\"default\"] = (_coblan_webcode_node_modules_style_loader_index_js_coblan_webcode_node_modules_css_loader_index_js_coblan_webcode_node_modules_vue_loader_lib_loaders_stylePostLoader_js_coblan_webcode_node_modules_sass_loader_lib_loader_js_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_send_vue_vue_type_style_index_0_id_68720f22_scoped_true_lang_scss___WEBPACK_IMPORTED_MODULE_0___default.a); \n\n//# sourceURL=webpack:///./rtc/rtc_send.vue?");

/***/ }),

/***/ "./rtc/rtc_send.vue?vue&type=template&id=68720f22&scoped=true&":
/*!*********************************************************************!*\
  !*** ./rtc/rtc_send.vue?vue&type=template&id=68720f22&scoped=true& ***!
  \*********************************************************************/
/*! exports provided: render, staticRenderFns */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _coblan_webcode_node_modules_vue_loader_lib_loaders_templateLoader_js_vue_loader_options_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_send_vue_vue_type_template_id_68720f22_scoped_true___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! -!../../../../../../../coblan/webcode/node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!../../../../../../../coblan/webcode/node_modules/vue-loader/lib??vue-loader-options!./rtc_send.vue?vue&type=template&id=68720f22&scoped=true& */ \"../../../../../../coblan/webcode/node_modules/vue-loader/lib/loaders/templateLoader.js?!../../../../../../coblan/webcode/node_modules/vue-loader/lib/index.js?!./rtc/rtc_send.vue?vue&type=template&id=68720f22&scoped=true&\");\n/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, \"render\", function() { return _coblan_webcode_node_modules_vue_loader_lib_loaders_templateLoader_js_vue_loader_options_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_send_vue_vue_type_template_id_68720f22_scoped_true___WEBPACK_IMPORTED_MODULE_0__[\"render\"]; });\n\n/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, \"staticRenderFns\", function() { return _coblan_webcode_node_modules_vue_loader_lib_loaders_templateLoader_js_vue_loader_options_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_send_vue_vue_type_template_id_68720f22_scoped_true___WEBPACK_IMPORTED_MODULE_0__[\"staticRenderFns\"]; });\n\n\n\n//# sourceURL=webpack:///./rtc/rtc_send.vue?");

/***/ }),

/***/ "./rtc/rtc_trigger.vue":
/*!*****************************!*\
  !*** ./rtc/rtc_trigger.vue ***!
  \*****************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _rtc_trigger_vue_vue_type_template_id_6a1b240e___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./rtc_trigger.vue?vue&type=template&id=6a1b240e& */ \"./rtc/rtc_trigger.vue?vue&type=template&id=6a1b240e&\");\n/* harmony import */ var _rtc_trigger_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./rtc_trigger.vue?vue&type=script&lang=js& */ \"./rtc/rtc_trigger.vue?vue&type=script&lang=js&\");\n/* empty/unused harmony star reexport *//* harmony import */ var _coblan_webcode_node_modules_vue_loader_lib_runtime_componentNormalizer_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../../../../../../coblan/webcode/node_modules/vue-loader/lib/runtime/componentNormalizer.js */ \"../../../../../../coblan/webcode/node_modules/vue-loader/lib/runtime/componentNormalizer.js\");\n\n\n\n\n\n/* normalize component */\n\nvar component = Object(_coblan_webcode_node_modules_vue_loader_lib_runtime_componentNormalizer_js__WEBPACK_IMPORTED_MODULE_2__[\"default\"])(\n  _rtc_trigger_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_1__[\"default\"],\n  _rtc_trigger_vue_vue_type_template_id_6a1b240e___WEBPACK_IMPORTED_MODULE_0__[\"render\"],\n  _rtc_trigger_vue_vue_type_template_id_6a1b240e___WEBPACK_IMPORTED_MODULE_0__[\"staticRenderFns\"],\n  false,\n  null,\n  null,\n  null\n  \n)\n\n/* hot reload */\nif (false) { var api; }\ncomponent.options.__file = \"rtc/rtc_trigger.vue\"\n/* harmony default export */ __webpack_exports__[\"default\"] = (component.exports);\n\n//# sourceURL=webpack:///./rtc/rtc_trigger.vue?");

/***/ }),

/***/ "./rtc/rtc_trigger.vue?vue&type=script&lang=js&":
/*!******************************************************!*\
  !*** ./rtc/rtc_trigger.vue?vue&type=script&lang=js& ***!
  \******************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _coblan_webcode_node_modules_babel_loader_lib_index_js_ref_1_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_trigger_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! -!../../../../../../../coblan/webcode/node_modules/babel-loader/lib??ref--1!../../../../../../../coblan/webcode/node_modules/vue-loader/lib??vue-loader-options!./rtc_trigger.vue?vue&type=script&lang=js& */ \"../../../../../../coblan/webcode/node_modules/babel-loader/lib/index.js?!../../../../../../coblan/webcode/node_modules/vue-loader/lib/index.js?!./rtc/rtc_trigger.vue?vue&type=script&lang=js&\");\n/* empty/unused harmony star reexport */ /* harmony default export */ __webpack_exports__[\"default\"] = (_coblan_webcode_node_modules_babel_loader_lib_index_js_ref_1_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_trigger_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_0__[\"default\"]); \n\n//# sourceURL=webpack:///./rtc/rtc_trigger.vue?");

/***/ }),

/***/ "./rtc/rtc_trigger.vue?vue&type=template&id=6a1b240e&":
/*!************************************************************!*\
  !*** ./rtc/rtc_trigger.vue?vue&type=template&id=6a1b240e& ***!
  \************************************************************/
/*! exports provided: render, staticRenderFns */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _coblan_webcode_node_modules_vue_loader_lib_loaders_templateLoader_js_vue_loader_options_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_trigger_vue_vue_type_template_id_6a1b240e___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! -!../../../../../../../coblan/webcode/node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!../../../../../../../coblan/webcode/node_modules/vue-loader/lib??vue-loader-options!./rtc_trigger.vue?vue&type=template&id=6a1b240e& */ \"../../../../../../coblan/webcode/node_modules/vue-loader/lib/loaders/templateLoader.js?!../../../../../../coblan/webcode/node_modules/vue-loader/lib/index.js?!./rtc/rtc_trigger.vue?vue&type=template&id=6a1b240e&\");\n/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, \"render\", function() { return _coblan_webcode_node_modules_vue_loader_lib_loaders_templateLoader_js_vue_loader_options_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_trigger_vue_vue_type_template_id_6a1b240e___WEBPACK_IMPORTED_MODULE_0__[\"render\"]; });\n\n/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, \"staticRenderFns\", function() { return _coblan_webcode_node_modules_vue_loader_lib_loaders_templateLoader_js_vue_loader_options_coblan_webcode_node_modules_vue_loader_lib_index_js_vue_loader_options_rtc_trigger_vue_vue_type_template_id_6a1b240e___WEBPACK_IMPORTED_MODULE_0__[\"staticRenderFns\"]; });\n\n\n\n//# sourceURL=webpack:///./rtc/rtc_trigger.vue?");

/***/ })

/******/ });