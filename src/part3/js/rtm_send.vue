<template>
    <div>
        <span v-if="loaded && !sending" class="can_send">加载成功</span>
    </div>
</template>
<script>
    export default {
        data(){
            return {
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
            window.send_msg=(msg,uid)=>{
                this.msg = msg
                this.remote_uid = uid
                console.log(msg)
//                Vue.nextTick(()=>{
//                    this.send()
//                })
                return this.send()
            }

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
                    this.client.login({ token: self.token, uid: self.uid }).then(() => {
                    console.log('AgoraRTM client login success');
            }).catch(err => {
                    console.log('AgoraRTM client login failure', err);
            });
            }).then(()=>{
                this. loaded =true
            })

        },
        methods:{
            send(){
                this.sending = true
                this.client.sendMessageToPeer(
                        { text: this.msg }, // 符合 RtmMessage 接口的参数对象
                        this.remote_uid, // 远端用户 ID
                ).then(sendResult => {
                    this.sending = false
                    if (sendResult.hasPeerReceived) {
                        /* 远端用户收到消息的处理逻辑 */
                    } else {
                        /* 服务器已接收、但远端用户不可达的处理逻辑 */
                    }
            }).catch(error => {
                    /* 发送失败的处理逻辑 */
                });
            }
        }
    }
</script>
<style>

</style>