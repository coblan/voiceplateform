
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
    "call/end"	:part3.Agora_interface.end_call,
    "call/msg"	:part3.Agora_interface.get_voice_msg,
    "call/recieve"	:part3.Agora_interface.recieve,
    "invite/robot"	:part3.Agora_interface.invite_robot,
    "call/robot"	:part3.Agora_interface.call_robot,
    "quit/robot"	:part3.Agora_interface.quit_robot,
    "agora/token"	:part3.Agora_interface.get_token,
    "agora/rtc-option"	:part3.Agora_interface.get_option,
    "agora/rtm-option"	:part3.Agora_interface.get_option,
}