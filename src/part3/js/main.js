import rtc_send  from './rtc/rtc_send.vue'
import rtc_trigger  from './rtc/rtc_trigger.vue'

Vue.component('com-rtc-trigger',rtc_trigger)
Vue.component('com-rtc-send', (resolve,reject)=>{
    ex.load_js('https://cdn.agora.io/sdk/release/AgoraRTCSDK-3.0.0.js').then(()=>{
        resolve(rtc_send)
    })
})


//import * as pig from './elk'