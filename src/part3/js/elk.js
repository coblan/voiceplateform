window.elk={
    debug(data){
        var post_data={
            '@timestamp':new Date(),
            'level': 'DEBUG',
            'host': 'web',
            'message': data
        }
        elk_input(post_data)
    }
}
function elk_input(data){
    var query_data={

    }
    $.ajax({
        url: 'http://enjoyst.com:10820/voice_rtm_msg',
        type: 'PUST',
        //contentType: 'application/json; charset=UTF-8',
        crossDomain: true,
        dataType: 'json',
        data: JSON.stringify(data),
        beforeSend: function (xhr) {
            xhr.setRequestHeader ("Authorization", "Basic " + btoa("elastic:he27375089"));
        },
        success: function(response) {
            alert(response)

        },

        error: function(jqXHR, textStatus, errorThrown) {
            var jso = jQuery.parseJSON(jqXHR.responseText);
            alert('section', 'error', '(' + jqXHR.status + ') ' + errorThrown + ' --<br />' + jso.error);
        }
    });
}