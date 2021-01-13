---
layout: post
title:  "node.js socket命令含义"
date:   2019-09-05
categories: Node.js
tags: Node.js note
---

* content
{:toc}

node.js socket命令含义






# node.js socket命令含义
## 一、 服务端
1. io.on('connection',function(socket));
监听客户端连接,回调函数会传递本次连接的socket

2. io.sockets.emit('String',data);
给所有客户端广播消息

3. io.sockets.socket(socketid).emit('String', data);
给指定的客户端发送消息

4. socket.on('String',function(data));
监听客户端发送的信息

5. socket.emit('String', data);
给该socket的客户端发送消息

## 二、客户端
1. 建立一个socket连接
```
var socket = io("ws://103.31.201.154:5555");
//连接聊天室io服务器，io服务器的根地址
```

2. 监听服务消息
```
socket.on('msg',function(data){
    socket.emit('msg', {rp:"fine,thank you"}); //向服务器发送消息
    console.log(data);
});
socket.on("String",function(data)) 
```
监听服务端发送的消息 Sting参数与服务端emit第一个参数相同

 
3. 监听socket断开与重连。
```
socket.on('disconnect', function() {
    console.log("与服务其断开");
});
socket.on('reconnect', function() {
    console.log("重新连接到服务器");
});
```























