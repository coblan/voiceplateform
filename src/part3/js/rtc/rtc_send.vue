<template>
    <div class="com-rtc-send">
        <span v-if="loaded" class="can_recieve">能够接受消息</span>
        <div>
            <span>appID</span>
            <span v-text="appid"></span>
        </div>
        <div>
            <span>uid</span>
            <input type="text" v-model="uid" disabled>
        </div>
        <div>
            <span>token</span>
            <input type="text" v-model="token" disabled>
        </div>
        <div>
            <span>状态</span>
            <span v-if="started" style="color: #0ff537">在线</span>
            <span v-else>离线</span>
        </div>
        <div>
            <span>人数</span>
            <span v-text="user_count"></span>
        </div>
        <div>
            <span>url</span>
            <span v-text="mp3_url"></span>
        </div>
        <div>
            <span>channel</span>
            <span v-text="channel"></span>
        </div>

        <rtc_rtc v-if="channel" :ctx="{channel:channel,par:this}"></rtc_rtc>
    </div>
</template>
<script>
/*{"doc":"test_js.md"}
*
* ### RTC机器人
*
* 机器人用于后台服务器向用户拨打语音电话，留言等。机器人加入频道，与频道内的用户通话。
* * 30s无人接听就退出频道
* * 语音最长不能超过5分钟，否则机器人自动退出
*
* 机器人具备接听后端消息功能，如果后端发送stop_channel 消息过来，机器人退出。
*
* 机器人退出后，后端进程会重新刷新页面。
* */
import rtc_rtc from './rtc_rtm.vue'
    export default {
        props:['ctx'],
        components:{
            rtc_rtc
        },
        data(){
            var childStore = new Vue()
            childStore.vc = this
            return {
                parStore:ex.vueParStore(this),
                childStore:childStore,
                uid: ''+parseInt( Math.random()*100000000 ),
                appid:this.ctx.appid,
                token:'',
                client:'',
                mp3_url:'',
                tone_list:[],
                channel:'',
                started:false,
                has_person_join:false,
                playing:false,
                user_count:0,
                loaded:false,
                finish_callback:'',
                mp3_length:60*1000,
                search_args:ex.parseSearch(),
                src_uid:'',
            }
        },
        mounted(){

//            ex.stompListen("/exchange/center.topic/backend.timely.message",function(data){
//                console.log(data.body)
//                var msg_dc = JSON.parse(data.body)
//                if(msg_dc.EventType==1){
//                    rootStore.$emit("todolist_updated")
//                }
//            })

            window.send_mp3 = (dc,callback)=>{
                debugger
                var channel= dc.channel
                var tone_list = dc.tone_list
                var src_uid = dc.src_uid
                ex.stompInit({url: this.ctx.websocket.url,user:this.ctx.websocket.user,pswd:this.ctx.websocket.pswd});
                ex.stompListen("/exchange/rtc-robot.stop/"+channel,(data)=>{
                    console.log(data.body)
                    this.debug_log(`[${channel}]接收到后台退出频道消息`)
                    this.$emit('finish-task')
//                    var msg_dc = JSON.parse(data.body)

                })

                this.debug_log('播放语音数据:'+JSON.stringify(tone_list))

                this.channel = channel
                this.src_uid = src_uid
//                this.mp3_url = mp3_url
                if( tone_list.length ==0){
                    // 测试时用
                    this.tone_list = [{url:'/static/Haydn_Cello_Concerto_D-1.mp3',before_second:0}]
                }else{
                    this.tone_list = tone_list
                }

                this.finish_callback= callback
                this.send()
            }
            window.reload_page = ()=>{
                location.reload()
            }
            this.$on('finish-task',()=>{
                if(this.finish_callback){
                    this.finish_callback()
                }

            })
            this.loaded=true

        },
        methods:{
            load_mp3(mp3_url){
                    var self = this
                    self.localStream.muteAudio()
                    if(/^http/.test(mp3_url) ){
                        var mp3_reach ='/relay?url='+mp3_url
                    }else{
                        var mp3_reach = mp3_url
                    }

                    var options = {
                        cacheResource: true,
                        //                                        filePath: "http://www.hochmuth.com/mp3/Haydn_Cello_Concerto_D-1.mp3",
                        filePath: mp3_reach || '/static/Haydn_Cello_Concerto_D-1.mp3',
                        cycle: 1,
                        replace: true,
                        playTime: 0
                    }
                    self.localStream.startAudioMixing(options, function (err) {
                        if (err) {
                            self.warning_log(`播放录音${options.filePath}错误:${err}`)
                            console.log("Failed to start audio mixing. " + err);
                        }
                    });
                    var p1 = new Promise((resolve,reject)=>{
                                self.localStream.on("audioMixingPlayed",function(){
                                self.debug_log('加载录音完成!')
                                if(! self.playing){
                                    var mp3_length =  self.localStream.getAudioMixingDuration();
                                    self.localStream.pauseAudioMixing()
                                    resolve(mp3_length)
                                }
                            })
                })
                return p1
            },
            play( tone_obj,has_person_promise){
                var mp3_url = tone_obj.url
                var second = tone_obj.before_second
                var p1 = this.load_mp3(mp3_url)
                var p2 = new Promise((resolve,reject)=>{
                    setTimeout(resolve,1000*second)
                })
                return Promise.all([p1,p2,has_person_promise]).then((values)=>{
                     this.playing = true
                    this.childStore.$emit('play-tone-obj',tone_obj)
                     this.onstart()
                    var mp3_length = values[0]
                    return new Promise((resolve,reject)=>{
                        setTimeout(()=>{
                            this.stopPlay()
                            resolve()
                        },mp3_length)
                    })
                })
            },
            pump(index, has_person_promise ){
                /*
                * @has_person_promise 判断是否有用户连接
                * */
                if(index >=  this.tone_list.length){
                    this.$emit('finish-task')
                    return
                }
                var tone_obj = this.tone_list[index]
                this.debug_log(`播放第${index}个tone,等待时间${tone_obj.before_second}`)
                return this.play(tone_obj ,has_person_promise).then(()=>{

                    return this.pump(index+1,has_person_promise)
                })
            },
            createClient(){
                var self =this
                self.client = AgoraRTC.createClient({mode: "rtc", codec: "h264"})

                return new Promise((resolve,reject)=>{
                            self.client.init(self.appid, function () {
                            console.log("init success");
                            resolve()
                        }, function(err) {
                            console.error("client join failed", err)
                            self.warning_log(`初始化client失败:${err}`)
                        })
                })
            },
            debug_log(msg){
                ex.director_call('rtc_front_log',{msg:msg,level:'DEBUG',proc_name:this.search_args.proc_name,})
            },
            warning_log(msg){
                ex.director_call('rtc_front_log',{msg:msg,level:'WARNING',proc_name:this.search_args.proc_name,})
            },
            send(){
                var self =this
               return this.createClient(). then(()=>{
                    this.debug_log('开始加入频道'+this.channel)
                    return this.join()
                }).then(()=>{
                    return this.publish()
                }).then(()=>{
                    var has_person_promise = self.regist_event()
                    this.pump(0,has_person_promise)
//                return this.success_publish()
            })
//            .then(()=>{
//                    this.debug_log('有用户接入，开始播放录音,'+this.mp3_length+'秒后，机器人退出')
//                    this.onstart()
//                    setTimeout(()=>{
//                        this.$emit('finish-task')
//                    },this.mp3_length)
//            })

            },
            join(){
                var self=this
               return new Promise((resolve,reject) =>{
                            $.get('/dapi/agora/rtc-option?channel='+this.channel+'&uid='+this.uid,function(resp){
                            self.token = resp.data.token
                            resolve()
                        })
                 }).then(()=>{
                    return new Promise((resolve,reject)=>{
                        this.client.join(this.token , this.channel, this.uid ,  (uid)=> {
                        console.log("join channel: " + this.channel + " success, uid: " + uid);
                        resolve()
                    }, function(err) {
                            console.error("client join failed", err)
                        })
                    })
                })
            },
            publish(){
                var self = this

                return new Promise((resolve,reject)=>{
                    self.localStream = AgoraRTC.createStream({
                    streamID: self.uid,
                    audio: true,
                    video: false,
                    screen: false,
                })

                self.localStream.init(function () {
                    console.log("初始化 local stream success");
                    resolve()
                }, function (err) {
                    console.error("初始化 local stream failed ", err);
                })
            }).then(()=>{
                    // Publish the local stream
                    self.client.publish(self.localStream, function (err) {
                    console.log("发布 failed");
                    console.error(err);
                })

            })
            },
            success_publish(){
                // 废弃
                var self = this
                self.localStream.muteAudio()
                if(/^http/.test(this.mp3_url) ){
                    var mp3_reach ='/relay?url='+this.mp3_url
                }else{
                    var mp3_reach = this.mp3_url
                }

                var options = {
                    cacheResource: true,
                    //                                        filePath: "http://www.hochmuth.com/mp3/Haydn_Cello_Concerto_D-1.mp3",
                    filePath: mp3_reach || '/static/Haydn_Cello_Concerto_D-1.mp3',
                    cycle: 1,
                    replace: true,
                    playTime: 0
                }
                self.localStream.startAudioMixing(options, function (err) {
                    if (err) {
                        self.warning_log(`播放录音${options.filePath}错误:${err}`)
                        console.log("Failed to start audio mixing. " + err);
                    }
                });

                var p1 = new Promise((resolve,reject)=>{
                            self.localStream.on("audioMixingPlayed",function(){
                                self.debug_log('加载录音完成!')
                                self.mp3_length =  self.localStream.getAudioMixingDuration();
                                if(! self.started){
                                    self.localStream.pauseAudioMixing()
                                    resolve()
                                }
                        })
                     })
                var p2 = new Promise((resolve,reject)=>{
                    self.client.on("peer-online",()=> {
                    console.log('有人链接了。')
                self.user_count += 1
                this.debug_log("新用户连接，当前连接数:"+this.user_count)
                if (!self.started) {
                    resolve()
                    // 播放音效
                    //                                    self.localStream.muteAudio()
                    //                                    self.localStream.playEffect({
                    //                                        soundId: 1,
                    ////                                        filePath: '/static/Haydn_Cello_Concerto_D-1.mp3'
                    //                                        filePath: 'http://www.hochmuth.com/mp3/Haydn_Cello_Concerto_D-1.mp3'
                    //                                    }, function(error) {
                    //                                        if (error) {
                    //                                            // 错误处理
                    //                                            return;
                    //                                        }
                    //                                        // 播放成功后的流程
                    //                                    });



                }
            })
            })
                return Promise.all([p1,p2])

            },
            onstart(){
                this.debug_log("开始播放录音"+this.user_count)
                var self = this
                self.localStream.unmuteAudio()
                self.localStream.setAudioMixingPosition(0)
                self.localStream.resumeAudioMixing()

            },
            stopPlay(){
                var self=this
                self.playing=false
                self.localStream.muteAudio()
                self.localStream.stopAudioMixing()
            },
            close(){
                var self=this
                self.localStream.muteAudio()
                self.localStream.stopAudioMixing()
                self.localStream.close()
                self.client.leave()
            },
            regist_event(){
                var self = this
                self.client.on("peer-leave", () => {
                    console.log('有人退出了。')
                    self.user_count -=1
                    console.log('有人退出频道，当前用户数${self.user_count}')
                    if(self.user_count<=0){

                        self.close()
                        this.debug_log('所有人都退出了频道，现在退出')
//                        self.$emit('ready-send-order')
                        self.$emit('finish-task')
                    }
                })
                setTimeout(()=>{
                    if(! self.has_person_join){
                        // 长时间无人接听，退出拨打
                        self.close()
                        this.debug_log('长时间无人接听，退出拨打!')
//                        self.$emit('ready-send-order')
                        self.$emit('finish-task')
                    }
                },1000*30)

                var has_person_promise = new Promise((resolve,reject)=>{
                            self.client.on("peer-online",()=> {
                            self.has_person_join=true
                            console.log('有人链接了。')
                            self.user_count += 1
                            this.debug_log("新用户连接，当前连接数:"+this.user_count)
                            resolve()
                        })
                    })

                return has_person_promise
            }
        }
    }
</script>

<style scoped lang="scss">
.com-rtc-send{
    display: inline-block;
    width: 260px;
    border: 1px solid grey;
}

</style>