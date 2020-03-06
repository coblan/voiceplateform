<template>
    <div>
        <h3>定时任务投送</h3>
    <div>
        <span>发送UID</span> <input type="text" v-text="row.src_uid">
    </div>
     <div>
            <span>接收UID</span> <input type="text" v-text="row.dst_uid"> <span>数组格式,例如:[1234,456]</span>
     </div>

      <div>
            <span>拨打时间</span> <input type="text"  v-model="row.call_time"> <span>(格式:2020-03-06 22:22:50)</span>
     </div>

      <div>
          <span>任务taskid</span> <input type="text" v-model="row.taskid"> <span>app后台对应的taskid</span>
      </div>
        <button @click="puttask">发布任务</button>
    </div>
</template>
<script>
    export default {
        props:['ctx'],
        data(){
            return {
                row:{}
            }
        },
        methods:{
            puttask(){
                cfg.show_load()
                ex.post('/dapi/calltask/update',this.row).then(()=>{
                    cfg.hide_load()

                })
            }
        }
    }
</script>