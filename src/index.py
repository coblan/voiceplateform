
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
    # 通过记录管理界面
    "callrecord"	:maindb.admin_callrecord.CallRecordPage,
    "config"	:maindb.admin_config.ConfigFormPage,
    # 模拟api管理界面
    "mockapi"	:maindb.admin_mockapi.MockapiPage,
    # 拨打任务管理界面
    "calltask"	:maindb.admin_calltask.CallTaskPage,
    "voicemsg"	:maindb.admin_voicemsg.VoicemsgPage,
    "frontlog"	:maindb.admin_frontlog.FrontLogPage,
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
    
    "calltask"	:maindb.admin_calltask.CallTaskPage.tableCls,
    "calltask.edit"	:maindb.admin_calltask.CallTaskForm,
    "calltask/list"	:maindb.admin_calltask.UserCallTask,
    
    "callrecord"	:maindb.admin_callrecord.CallRecordPage.tableCls,
    
    "callevent-tab"	:maindb.admin_callrecord.CallEventTab,
    "config"	:maindb.admin_config.ConfigFormPage.fieldsCls,
    
    "mockapi"	:maindb.admin_mockapi.MockapiPage.tableCls,
    "mockapi.edit"	:maindb.admin_mockapi.MockapiForm,
    "voicemsg"	:maindb.admin_voicemsg.VoicemsgPage.tableCls,
    "frontlog"	:maindb.admin_frontlog.FrontLogPage.tableCls,
    "frontlog.edit"	:maindb.admin_frontlog.FrontLogForm,
    
     #"/hello/test"	:maindb.admin_mockapi.dyn_mock_api,
}
director_views = {
    # 系统内部使用
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
    
    # 拨打接口
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
    
    
    # 获取拒接语音 [不使用了,现在从app后台获取]
    "account/get-reject-tone"	:maindb.admin_accountinfo.get_reject_tone,
    
    # 更新定时任务
    "calltask/update"	:maindb.admin_calltask.update_calltask,
    "calltask/delete"	:maindb.admin_calltask.delete_call_task,
  
    "system/config"	:maindb.admin_config.get_config,
    
    # 模拟测试接口
    "mock"	:maindb.admin_mockapi.dyn_mock_api,
    
    # 获取rtc 的token
    "agora/rtc-option"	:part3.Agora_interface.get_rtc_option,
    "agora/rtm-option"	:part3.Agora_interface.get_rtm_option,
    
    # 该接口废弃，使用 agora/rtc-option 获取
    "agora/token"	:part3.Agora_interface.get_token,
    
    # 用于机器人测试
    "robot_receive_call"	:part3.agora_process_page.robot_test.send_sss,
    "robot_call_user"	:part3.agora_process_page.robot_test.sss,
    "recording_test"	:part3.agora_process_page.robot_test.recording_test,
    # rtc uid 映射，暂时未使用
    "call/rtcmap"	:maindb.admin_callrecord.user_rtc_map,
    # 前端上传前端日志
    "put-log"	:maindb.admin_frontlog.put_log,
   
}

sim_signal = {
    "call.call"	:[maindb.signal.call_call],
    "call.enter"	:[maindb.signal.call_start],
    "call.quit"	:[maindb.signal.call_quit],
    "call.end"	:[maindb.signal.call_end],
}

web_page_dc = {
    "rtc-send"	:part3.agora_process_page.rtc_send.RTCSendPage,
    "rtm-send"	:part3.agora_process_page.rtm_send.RTMSendPage,
    # 机器人测试页面
    "rtc-robot"	:part3.agora_process_page.robot_test.RobotTestPage,
    # 总控制台
    "p"	:maindb.pc_page.panel.PanelPage,
}

