<template>
    <div>

        <div style="margin: 30px">
            <h3>接收机器人</h3>
            <div>
                <span>发送者</span>
                <input type="text" v-model="row.src">
            </div>
            <div>
                <span>接收者</span>
                <input type="text" v-model="row.dst">
            </div>
            <div>
                <span>频道</span>
                <input type="text" v-model="row.channel_name">
            </div>
            <button @click="send_receive">机器人接听电话</button>

        </div>

        <div style="margin: 30px">
            <h3>拨打机器人</h3>
            <div>
                <span>发送者</span>
                <input type="text" v-model="row.src">
            </div>
            <div>
                <span>接收者列表</span>
                <input type="text" v-model="row.dst_list">
            </div>
            <div>
                <span>频道</span>
                <input type="text" v-model="row.channel_name">
            </div>
            <div>
                <span>taskid</span>
                <input type="text" v-model="row.taskid">
            </div>

            <button @click="call_user">机器人拨打电话</button>
        </div>



    </div>
</template>
<script>
    export default {
        data(){
            return {
                row:{

                }
            }
        },
        methods:{
            send_receive(){
                ex.director_call('robot_receive_call',this.row)
            },
            call_user(){
                ex.director_call('robot_call_user',this.row)
            }
        }
    }
</script>