# RTM发送消息

[测试网址](http://voice.enjoyst.com/rtm) `http://voice.enjoyst.com/rtm`。如下截图

![Image](./_static/rtm_msg.png)

上部用于浏览器端调用rtm webclient进行本地发送消息。*不能给自己发送消息*,只能发消息给其他用户。

下部分是向后台发送消息，可以发送给任何人。

数据流向
``` mermaid::

    graph TD
    A[Client] -->|send message via http| B(Logic)
    B --> C{rabbitMq}
    C -->|One| D[rtm client on backend]
    D -->|RTM| E[User]
```