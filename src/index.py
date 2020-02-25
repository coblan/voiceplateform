
import maindb
import part3
import helpers
page_dc = {
    "kv"	:helpers.director.admin_kv.KvTablePage,
    "kv.edit"	:helpers.director.admin_kv.KvFormPage,
    "del_rows"	:helpers.director.fields.delpage.DelPage,
    "log"	:helpers.director.log.logpage.LogPage,
    "user"	:helpers.director.admin.UserTablePage,
    "user.edit"	:helpers.director.admin.UserFormPage,
    "group"	:helpers.director.admin.GroupTablePage,
    "group.edit"	:helpers.director.admin.GroupFormPage,
    "permit.edit"	:helpers.director.admin.PermitFormPage,
    "group_human"	:helpers.director.admin.GroupGroup,
    "group_human.edit"	:helpers.director.access.assem_group.AssemGroupPage,
    "jb_user"	:helpers.case.jb_admin.admin.UserPage,
    "jb_group"	:helpers.case.jb_admin.admin.GroupPage,
    "accountinfo"	:maindb.admin_accountinfo.AccountInfoPage,
    "callrecord"	:maindb.admin_callrecord.CallRecordPage,
    "config"	:maindb.admin_config.ConfigFormPage,
    
    "mockapi"	:maindb.admin_mockapi.MockapiPage,
}
director = {
    "permit.programer"	:helpers.director.admin.PermitPage.PermitTable,
    "permit.programer.edit"	:helpers.director.admin.PermitFormPage.PermitForm,
    "jb_user"	:helpers.case.jb_admin.admin.UserPage.tableCls,
    "jb_user.edit"	:helpers.case.jb_admin.admin.UserFields,
    "user.picker"	:helpers.case.jb_admin.admin.UserPicker,
    "jb_group"	:helpers.case.jb_admin.admin.GroupPage.tableCls,
    "jb_group.edit"	:helpers.case.jb_admin.admin.GroupForm,
    "authuser.regist"	:helpers.authuser.admin_regist.RegistFormPage.fieldsCls,
    "accountinfo"	:maindb.admin_accountinfo.AccountInfoPage.tableCls,
    "accountinfo.edit"	:maindb.admin_accountinfo.AccountForm,
    
    "calltask"	:maindb.admin_calltask.CallTaskPage,
    "calltask.edit"	:maindb.admin_calltask.CallTaskForm,
    "calltask/list"	:maindb.admin_calltask.UserCallTask,
    
    "callrecord"	:maindb.admin_callrecord.CallRecordPage.tableCls,
    
    "callevent-tab"	:maindb.admin_callrecord.CallEventTab,
    "config"	:maindb.admin_config.ConfigFormPage.fieldsCls,
    
    "mockapi"	:maindb.admin_mockapi.MockapiPage.tableCls,
    "mockapi.edit"	:maindb.admin_mockapi.MockapiForm,
    
     "/hello/test"	:maindb.admin_mockapi.dyn_mock_api,
}
director_views = {
    "d.save_row"	:helpers.director.dapi.save_row,
    "d.get_row"	:helpers.director.dapi.get_row,
    "get_row"	:helpers.director.dapi.get_row,
    "d.get_rows"	:helpers.director.dapi.get_rows,
    "d.save_rows"	:helpers.director.dapi.save_rows,
    "save_rows"	:helpers.director.dapi.save_rows,
    "d.get_head_context"	:helpers.director.dapi.get_head_context,
    "d.director_element_call"	:helpers.director.dapi.director_element_call,
    "do_login"	:helpers.authuser.admin_login.Login.run,
    "do_logout"	:helpers.authuser.admin_login.do_logout,
    "authuser.changepswd"	:helpers.authuser.admin_pswd.changepswd,
    
    # 早期测试api
    "celery_send_msg"	:part3.Agora_interface.celery_send_msg,
    "try_send_mp3"	:part3.Agora_interface.try_send_mp3,
    "rtc_front_log"	:part3.agora_process_page.Agora_elk.rtc_front_log,
    
    # 
    "account/update"	:maindb.admin_accountinfo.update_account_info,
    "account/reject-tone"	:maindb.admin_accountinfo.upload_reject_tone,
    "call/user"	:part3.Agora_interface.call_user,
    "call/msg"	:part3.Agora_interface.get_voice_msg,
    "call/token"	:part3.Agora_interface.recieve,
    "call/heartbeat"	:maindb.admin_callrecord.refresh_call_record,
    "call/event"	:maindb.admin_callrecord.event_call_record,
      
    "invite/robot"	:part3.Agora_interface.invite_robot,
    "call/robot"	:part3.Agora_interface.call_robot,
    "quit/robot"	:part3.Agora_interface.quit_robot,
    "agora/token"	:part3.Agora_interface.get_token,
    "agora/rtc-option"	:part3.Agora_interface.get_option,
    "agora/rtm-option"	:part3.Agora_interface.get_option,
    
    "account/get-reject-tone"	:maindb.admin_accountinfo.get_reject_tone,
    
    # 更新定时任务
    "calltask/update"	:maindb.admin_calltask.update_calltask,
    "calltask/delete"	:maindb.admin_calltask.delete_call_task,
  
    "system/config"	:maindb.admin_config.get_config,
    
     "dyn_mock_api"	:maindb.admin_mockapi.dyn_mock_api,
   
}

sim_signal = {
    "call.call"	:[maindb.signal.call_call],
    "call.enter"	:[maindb.signal.call_start],
    "call.quit"	:[maindb.signal.call_quit],
    "call.end"	:[maindb.signal.call_end],
}



=========2020-02-25 15:40:27.003926==========
