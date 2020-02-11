<template>
    <div>
        <span>RTM频道:</span>
        <span v-text="ctx.channel"></span>
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
                msg:'',
                remote_uid:'',
                recieved:'',
                loaded:false,
                sending:false,
            }
        },
        mounted(){
          this.init()
        },
        methods:{
            init(){

                var self =this
                new Promise((resolve,reject) =>{
                    $.get('/dapi/agora/rtm-option?channel=mychanel&uid='+this.uid,function(resp){
                    self.token = resp.data.token
                    self.appid = resp.data.appID
                    resolve()
                    })
                }).then(()=>{
                    self. client = AgoraRTM.createInstance(this.appid);
                    self.client.on('ConnectionStateChanged', (newState, reason) => {
                        console.log('on connection state changed to ' + newState + ' reason: ' + reason);
                    });
                    self.client.on('MessageFromPeer', ({ text }, peerId) => { // text 为消息文本，peerId 是消息发送方 User ID
                            /* 收到点对点消息的处理逻辑 */
                            console.log(text)
                        self.recieved = text
                    });
                }).then(()=>{
                        return new Promise((resolve,reject)=>{
                            this.client.login({ token: self.token, uid: self.uid }).then(() => {
                                console.log('AgoraRTM client login success');
                                resolve()
                            }).catch(err => {
                                    console.log('AgoraRTM client login failure', err);
                            });
                        })

                }).then(()=>{
                        this. loaded =true
                        const channel = this.client.createChannel(this.ctx.channel);
                        channel.join().then(() => {
                            /* 加入频道成功的处理逻辑 */
                            this.parStore.vc.debug_log("机器人加入"+ this.ctx.channel +"频道成功")
                        }).catch(error => {
                            /* 加入频道失败的处理逻辑 */
                            this.parStore.vc.warning_log("机器人加入"+ this.ctx.channel +"频道失败")
                        });
                })
            },
        }
    }
</script>