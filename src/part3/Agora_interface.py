from helpers.director.shortcut import director_view
from django.conf import settings
import time

from . Agora.RtcTokenBuilder import RtcTokenBuilder
@director_view('agora/token')
def get_token():
    appID = settings.AGORA.get('appID')
    appCertificate = settings.AGORA.get('appCertificate')
    channelName='test_channel'
    userAccount=987654321
    Role_Attendee = 2
    privilegeExpiredTs = time.time() + 600
    token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    print("Token with user account: {}".format(token))
    return token