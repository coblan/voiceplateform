## rabbitmq

### 机器接听

```
exchange:"rtc-robot"
routing_key:"receive"
```

推送的json为
```
{'from':src,'to':dst,'channel':channel,}
```

### 机器人主动拨打

```
exchange:"rtc-robot"
routing_key:"call"
```

推送的json为

```
{'from':src,'to':dst_list,'channel':channel,'taskid':taskid}
```

### 机器人退出

```
exchange:"rtc-robot.stop"
routing_key:channel
```

推送的json为
```
{
    'channel':channel,
    'uid':uid ,  // 用户的ID，在机器人对打的情况下，机器人需要根据该uid是否为自己代表的用户。
}
```

