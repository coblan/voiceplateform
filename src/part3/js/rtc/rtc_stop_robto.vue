<template>
    <div class="com-rtc-kick-robot">
        <h3>踢出机器人</h3>
        <div>
            <span>uid</span> <input type="text" v-model="row.uid">
        </div>
        <div>
            <span>频道</span> <input type="text" v-model="row.channel">
        </div>
        <button @click="kick_robot">提出机器人</button>
    </div>
</template>
<script>
    export default {
        prop:['ctx'],
        data(){
            return {
                row:{
                }
            }
        },
        methods:{
            kick_robot(){
                cfg.show_load()
                ex.post('/dapi/quit/robot',this.row).then(()=>{
                    cfg.hide_load()
                })
            }
        }
    }
</script>
<style lang="scss" scoped>
    .com-rtc-kick-robot{
        margin: 20px;
        padding: 20px;
        border: 1px solid grey;
    }
</style>