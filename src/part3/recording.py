'''
./recorder_local --appId <你的 App ID> --channel <频道名> --uid 0 --channelProfile <0 通信模式，1 直播模式> --appliteDir Agora_Recording_SDK_for_Linux_FULL/bin
'''
'''
./recorder_local --appId 303156d224e44881a00af9cabc9e10d8 --channel sss --uid 0 --channelProfile 0 --appliteDir /usr/src/recording/bin --lowUdpPort 10860 --highUdpPort 10890
'''

./recorder_local --appId 303156d224e44881a00af9cabc9e10d8 --channel lala --uid 123 --channelKey 006303156d224e44881a00af9cabc9e10d8IABOKATw7IO2mvwvuei/PU1R7rQe/BRebONC62/cwmymGNVDXOrSY0iIEAAsNaID5PRXXgEAAQC8pVZe  --appliteDir ~/agoracore/Agora_Recording_SDK_for_Linux_FULL/bin --lowUdpPort 14000 --highUdpPort 15000 --recordFileRootDir /userfile/recording/data1

docker container run -p 14000-15000:14000-15000 -p 1080:1080 -p 25000:25000 -it agora_recording:v1 bash