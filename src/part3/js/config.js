ex.assign(cfg,{
    search_args:ex.parseSearch(),
    debug_log(msg){
        ex.director_call('rtc_front_log',{msg:msg,level:'DEBUG',proc_name:this.search_args.proc_name,})
    },
    warning_log(msg){
        ex.director_call('rtc_front_log',{msg:msg,level:'WARNING',proc_name:this.search_args.proc_name,})
    },
})