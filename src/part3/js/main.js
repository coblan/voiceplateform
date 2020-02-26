import * as cfg from  './config'
import rtc_send  from './rtc/rtc_send.vue'
import rtc_trigger  from './rtc/rtc_trigger.vue'
import rtm_send  from './rtm_send.vue'
import  rtc_robto_test from  './rtc/rtc_robot_test.vue'

Vue.component('com-robot-receive',rtc_robto_test)

Vue.component('com-rtc-trigger',rtc_trigger)
Vue.component('com-rtc-send', (resolve,reject)=>{
    ex.load_js_list(['https://cdn.agora.io/sdk/release/AgoraRTCSDK-3.0.0.js',
        '/static/agora/agora-rtm-sdk-1.2.1.js'])
        .then(()=>{
        resolve(rtc_send)
    })
})

Vue.component('com-rtm-send',(resolve,reject)=>{
    ex.load_js('/static/agora/agora-rtm-sdk-1.2.1.js').then(()=>{
        resolve(rtm_send)
    })
})
