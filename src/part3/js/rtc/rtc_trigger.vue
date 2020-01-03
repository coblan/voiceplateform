<template>
    <div>trigger 样例 <span v-text="sender_count"></span>
        <div class="can_recieve" v-if="can_recieve">可以接受消息</div>
        <div class="process_over" v-if="process_over">处理完成</div>
    </div>
</template>
<script>
    export default {
        data(){
            var parStore = ex.vueParStore(this)
            Vue.set(parStore.option,'sender_list',[])
            return {
                parStore:parStore,
                task_list:[],
                can_recieve:false,
                process_over:false,
            }
        },
        mounted(){
            var self =this

            window.send_mp3 = function(channel,mp3_url){
                self.task_list.push({channel:channel,mp3_url:mp3_url})
            }
            window.reload_page= function(){
                location.reload()
            }
            this.can_recieve=true
            setInterval(self.pump,500)
            this.parStore.$on('finish-task',this.check_need_refresh)
        },
        computed:{
            sender_count(){
                return this.parStore.option.sender_list.length
            }
        },
        methods:{
            check_need_refresh(){
                if(this.parStore.option.sender_list.length == 0){
                    this.debug_log('任务完成.返回python控制')
//                    location.reload()
                    this.process_over=true
                }
            },
            warning_log(msg){
                ex.director_call('rtc_front_log',{msg:msg,level:'WARNING',uid:'trigger'})
            },
            debug_log(msg){
                ex.director_call('rtc_front_log',{msg:msg,level:'DEBUG',uid:'trigger'})
            },

            pump(){
                if(this.task_list.length >0 ){
                    var sender = this.get_valid_sender()
                    if(sender){
                        var task = this.task_list[0]
                        this.task_list.splice(0,1)
                        sender.channel = task.channel
                        sender.mp3_url = task.mp3_url
                        sender.send()

                        this.pump()
                    }else{
                       this.warning_log('没有可用的sender')
                    }
                }else {

                }

            },
            get_valid_sender(){
                if(this.parStore.option.sender_list.length > 0 ){
                    var mm =this.parStore.option.sender_list[0]
                    this.parStore.option.sender_list.splice(0,1)
                    return mm
                }else {

                }
            }
        }
    }
</script>