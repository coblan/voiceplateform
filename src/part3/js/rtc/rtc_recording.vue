<template>
    <div class="com-rtc-recording">
        <div>
            <span>频道</span>
            <input type="text" v-model="channel">
        </div>
        <div>
            <button @click="record">录制</button>
        </div>
    </div>
</template>
<script>
    export default {
        data(){
            return {
                channel:''
            }
        },
        methods:{
            record(){
                cfg.show_load()
                ex.director_call('recording_test',{channel:this.channel}).then(()=>{
                    cfg.hide_load()
                })
            }
        }
    }
</script>
<style scoped lang="scss">
    .com-rtc-recording{
        border: 1px solid grey;
        padding: 20px;
    }

</style>