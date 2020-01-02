<template>
    <div class="com-rtc-send">
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
    </div>
</template>
<script>
    export default {
        props:['ctx'],
        data(){
            return {
                parStore:ex.vueParStore(this),
                uid: ''+parseInt( Math.random()*100000000 ),
                appid:'',
                token:'',
                client:'',
                mp3_url:'',
                channel:'',
                started:false,
                user_count:0,
            }
        },
        mounted(){
            this.$on('ready-send-order',()=>{
                this.channel=''
                this.token = ''
                this.mp3_url=''
                this.appid = ''
                this.started=false

                this.parStore.option.sender_list.push(this)
            })

            this.$emit('ready-send-order')

        },
        methods:{
            updateclient(){
                var self =this
                return new Promise((resolve,reject) =>{
                            $.get('/dapi/agora/rtc-option?channel='+this.channel+'&uid='+this.uid,function(resp){
                            self.token = resp.data.token
                            self.appid = resp.data.appID
                            resolve()
                        })
            }).then(()=>{
                    self.client = AgoraRTC.createClient({mode: "rtc", codec: "h264"})
                return new Promise((resolve,reject)=>{
                            self.client.init(self.appid, function () {
                            console.log("init success");
                            resolve()
                        }, function(err) {
                            console.error("client join failed", err)
                        })
            })
            })
            },
            debug_log(msg){
                ex.director_call('rtc_front_log',{msg:msg,level:'DEBUG',uid:this.uid})
            },
            send(){
                this.debug_log('开始更新client信息，创建频道:'+this.channel)
                this.updateclient().then(()=>{
                    this.debug_log('开始加入频道'+this.channel)
                    return this.join()
                }).then(()=>{
                    return this.publish()
                }).then(()=>{
                    this.regist_event()
                return this.success_publish()
            }).then(()=>{
                    this.debug_log('有用户接入，开始播放录音')
                    this.onstart()
            })
            },
            join(){
                var self=this
                return new Promise((resolve,reject)=>{
                            this.client.join(this.token , this.channel, this.uid ,  (uid)=> {
                            console.log("join channel: " + this.channel + " success, uid: " + uid);
                            resolve()
                        }, function(err) {
                            console.error("client join failed", err)
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
                        console.log("Failed to start audio mixing. " + err);
                    }
                });

                var p1 = new Promise((resolve,reject)=>{
                            self.localStream.on("audioMixingPlayed",function(){
                                self.debug_log('加载录音完成!')
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
                self.started = true
                self.localStream.unmuteAudio()
                self.localStream.resumeAudioMixing()
            },
            regist_event(){
                var self = this
                self.client.on("peer-leave", () => {
                    console.log('有人退出了。')
                    self.user_count -=1
                    if(self.user_count<=0){
                        console.log('所有人都退出了，现在退出')

    //                        self.localStream.stopAllEffects()
                        self.localStream.muteAudio()
                        self.localStream.stopAudioMixing()
                        self.client.leave()
                        this.debug_log('所有人都退出了频道，现在退出')
                        self.$emit('ready-send-order')
                    }
                })
                setTimeout(()=>{
                    if(! self.started){
                        // 长时间无人接听，退出拨打
                        self.localStream.muteAudio()
                        self.localStream.stopAudioMixing()
                        self.client.leave()
                        this.debug_log('长时间无人接听，退出拨打!')
                        self.$emit('ready-send-order')
                    }
                },1000*30)
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