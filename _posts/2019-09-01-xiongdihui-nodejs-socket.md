---
layout: post
title:  "基于nodejs和socket实现聊天室"
date:   2019-09-01
categories: Node.js
tags: Node.js note
---

* content
{:toc}

基于nodejs和socket实现聊天室









# 介绍和原理
1. 用http协议完成不了聊天室 ，因为如果浏览器不发送请求，服务器端不会主动发送消息，所以要用`web socket`协议
2. `web socket`协议：WebSocket是一种协议，与HTTP协议一样位于应用层，都是TCP/IP协议的子集。HTTP协议是单向通信协议，只有客户端发起HTTP请求，服务端才会返回数据。而WebSocket协议是双向通信协议，在建立连接之后，客户端和服务器都可以主动向对方发送或接受数据。WebSocket协议建立的前提需要借助HTTP协议，建立连接之后，持久连接的双向通信就与HTTP协议无关了
3. 准备：客户端、服务器、node.js
4. 服务器功能：接受客户端消息、广播消息
5. 客户端功能：发送消息、接受服务器发送过来的消息
6. 客户端的发送是基于`http`协议，消息的发送和请求都是基于`websocket`协议，在`npm`里下载`socket`，下载完成后，文件里会多一个`node_modules`的文件夹，这是一些这个项目的依赖模块

## 一、 先搭建一个服务器
1. 步骤
    * 要先引入一个http模块
    * 创建服务器并监听端口号
2. 代码：
```
var http = require('http'); //引入http模块
var server = http.createServer(function (req,res) {
    res.end('hello world');
}).listen(2000); //监听端口
```

3. 分析Node.js 的 HTTP 服务器：
    * 第一行请求（require）Node.js 自带的 http 模块，并且把它赋值给 http 变量。
    * 接下来我们调用 http 模块提供的函数：`createServer` 。这个函数会返回 一个对象，这个对象有一个叫做 `listen` 的方法，这个方法有一个数值参数， 指定这个 HTTP 服务器监听的端口号。

## 二、搭建客户端
1. 步骤
    * 新建一个HTML文件当作客户端页面
    * 引入一个fs文件系统模块
    * 在服务端用`fs.readFileSync`读取客户端页面
2. 代码
```
var fs = require("fs"); //引入 文件 系统模块
var html = fs.readFileSync("./client.html");
```
3. 分析：
    * 第一行请求（require）Node.js 自带的 fs 模块，并且把它赋值给 fs 变量。
    * 调用fs模块中的同步读文件方法

## 三、引入socket.io模块
1. 步骤
    * 引入一个socket.io模块
    * http服务与ws服务进行相关联，返回io服务实例
2. 代码
```
var ws = require('socket.io');//引入socket.io模块
var io = ws(server);        //http服务与ws服务进行相关联，返回io服务实例
```

## 四、建立连接，监听客户端接入
1. 步骤
    * 监听客户端接入
    * 在控制台返回信息有新用户进入房间
2. 代码
```
io.on('connection',function (socket) {
    //发生在用户连接io服务器的时候
    console.log('有新用户进入房间');
});
```

## 五、服务器接收客户端消息
1. 步骤
    * 接收消息：一定是在建立连接之内
    * socket参数，负责对消息进行处理
2. 代码
```
socket.on('message',function (obj) {
        //接收客户端消息
        io.emit('message',obj);//emit是主动发送事件，发给所有已经连接的客户端
    });
```

## 六、客户端开发
1. 步骤
    * 引入`socket.io`插件
    * 连接到服务器，引入地址
2. 代码
```
<script type="text/javascript" 
        src="https://wulv5.com/js/socket.io.min.js"></script>
        <script type="text/javascript">
        var socket = io.connect("/");//连接聊天室io服务器    

        </script>
```

## 七、客户端发送消息给服务器
1. 步骤
    * 得到文本框内容
    * 监听鼠标点击事件发送消息
    * 验证文本框有没有消息
2. 代码
```
var oText = document.getElementById('text'),
    oBtn = document.getElementById('btn');

        oBtn.onclick = function () {
            var mes = oText.value;
            if(!mes){
                return;
            }
            socket.send(mes);//如果文本框内有内容 那么就发送消息去服务器
        }
```

## 八、客户端接收消息并输出
1. 步骤
    * 输出服务端发送过来的消息
2. 代码
```
socket.on('message',function (mes) {
            //输出服务端发送过来得消息
            var div = document.createElement("div");
            div.innerText = mes;
            document.body.appendChild(div);
            });
```






