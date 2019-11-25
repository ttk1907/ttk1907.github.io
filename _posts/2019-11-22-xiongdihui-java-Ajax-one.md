---
layout: post
title:  "Ajax第一天"
date:   2019-11-22
categories: Ajax
tags: Ajax note
---

* content
{:toc}

1. Ajax第1天：GET请求的使用步骤、POST请求的使用步骤、GSON.jar
1. Ajax第2天：ajax函数、get函数与post函数、getJSON函数、Load与缓存问题








# Ajax第一天
## Ajax第1天
### 简介
1. 作用:一种用于网页异步请求的技术,用于与服务器进行异步交互以及局部页面的刷新

### GET请求的使用步骤
1. 创建一个异步请求的对象:`var xhr = new XMLHttpRequest();`
2. 设置请求的方式,以及请求的地址:`xhr.open("GET","请求地址");`
3. 设置请求结果产生时的事件处理函数(当请求状态发生改变时,执行的函数)
    1. 此方法在一次ajax中,会执行五次,分别表示五种状态
    2. 每次的状态值,从xhr.readyState属性中得到
    3. 状态值:
        1. 值为0:请求初始化中,他的触发,在new对象时,此方法不会执行
        2. 值为1:请求正在发送,它的触发在open函数执行时,此方法如果在open前指定,则状态发生时方法执行
        3. 值为2:请求发送完毕
        4. 值为3:服务器开始响应
        5. 值为4:响应完毕,内容已经得到了
    4. 请求也存在状态码,例如:404表示资源找不到,500表示服务器内部错误,200表示成功,302表示重定向
    5. 请求状态码,通过xhr.status得到,如果200表示请求成功

    ```java
xhr.onreadystatechange = function(){
    if (xhr.readyState == 4) {
        if (xhr.status == 200) {
            成功得到结果
            得到的结果,在xhr.responseText中,是文本内容
        }else{
            请求失败
            提示失败
        }
    }
}

    ```

4. 发送请求:`xhr.send(null)`,null是参数,因为get方法在网址上拼接了参数,所以传null

### POST请求的使用步骤
1. 创建一个异步请求的对象:`var xhr = new XMLHttpRequest();`
2. 设置请求的方式,以及请求的地址:`xhr.open("POST","请求地址");`
3. 设置请求结果产生时的事件处理函数(当请求状态发生改变时,执行的函数,同GET方法)
4. 设置请求头部:`xhr.setRequestHeader("content-type","application/x-www-form-urlencoded")`
5. 发送请求:`xhr.send(参数列表)`

### 注意:使用IE浏览器8操作上述的案例
1. GET或POST请求,都需要修改第1步:`var xhr = new ActiveXObject("Microsoft.XMLHTTP");`

### GSON.jar
1. 作用:
    1. 将Java中的对象快速的转换为JSON格式的字符串
    2. 将JSON格式的字符串,转换为Java的对象
2. 将Java中的对象快速的转换为JSON格式的字符串转换步骤:
    1. 引入jar包
    2. 在需要转换的JSON字符串的位置编写如下代码即可:
    3. String json = new Gson().toJSON(要转换的对象);
    4. 案例:

    ```java
    Book b = BookDao.find();
    String json = new Gson().toJSON(b);
    System.out.println(json);
    ```        

3. 将JSON格式的字符串,转换为Java的对象的转换步骤
    1. 引入jar包
    2. 在需要转换Java对象的位置,编写如下代码:
    3. 对象 = new GSON().fromJson(JSON字符串,对象类型.class);
    4. 案例:

    ```java
String json = "{ "id":1,"name":"ttk","age":18}";
User user = new Gson().fromJson(json,User.class);
System.out.println(user);
    ```

## Ajax第2天
### ajax函数
1. 函数名称:`$.ajax`
2. 参数列表:长度为1,需要传递一个对象
3. 通常传递到参数1的对象,我们使用JSON格式传输,属性与值描述如下:

```java
{
    url:"请求的地址",
    type:"请求方式GET/POST...",
    async:"默认true,表示异步请求",
    data:"请求的参数,格式与网址?后的格式一致",
    dataType:"TEXT/JSON",//表示服务器返回的数据类型.如果编写JSON , 我们接收到的数据 就是一个对象
    success:function(data){
            //当服务器请求成功时, 这里执行
            //参数data就是响应的内容.
            //  当dataType的值为TEXT时,  data是一个string类型的数据
            //  当dataType的值为JSON时,  data是一个对象.
        },
    error:function(){
        //当服务器返回的状态码不再200-299的范围 , 则表示失败, 这里执行
    }
}
```

### get函数与post函数
1. 两个函数的格式, 完全一致, 一个用于GET请求, 一个用于POST请求.
2. 函数名称:`$.get`,`$.post`
3. 参数列表:
    1. 列表长度为4:
    2. 参数1. url :请求地址
    3. 参数2. data:请求时携带的参数,与网址?后的参数格式一致.
    4. 参数3. success:当请求成功时,处理的函数
    5. 参数4. 响应的数据类型:TEXT/JSON
4. 格式示例:`$.get("s1.do","",function(data){},"JSON");`

### getJSON函数
1. 函数名称:`$.getJSON`
2. 参数列表:
    1. 参数列表长度为3
    2. 参数1.url:请求地址
    3. 参数2.data:请求时携带的参数,与网页?后的参数格式一致
    4. 参数3.success:当请求成功时,处理的函数.
3. 案例:

```jsp
<h3>快递查询2</h3>
<input placeholder="请输入快递单号"><button onclick="x1()">查询</button>
<script type="text/javascript">
    function x1(){
        $("#ul1").html("");
        //1.    得到用户输入的快递单号
        var number = $("input").val();
        //2.    发送ajax请求
        layer.msg("拼命查询中...",{icon:16,shade:0.01});
        $.getJSON("s2.do","number="+number,function(data){
            if(data.status == 0){
                //查询成功
                var arr = data.result.list;
                for(var i=0;i<arr.length;i++){
                    var $li = $("<li>时间:"+arr[i].time+"<br>进度:"+arr[i].status+"</li>");
                    $("#ul1").append($li);
                }
            }else{
                //查询失败
                layer.msg("很遗憾, 查询失败了");
            }
        });
    }
</script>
<ul id="ul1">
</ul>
```

### Load与缓存问题
1. jquery对象.load:通过jquery对象,调用load函数,将服务器返回的内容,直接嵌入到元素的内部,使用load函数访问的服务器通常返回的不是JSON,而是html标签
2. 函数名称:`$obj.load`
3. 参数列表:
    1. 参数列表长度为3
    2. 参数1.url:请求地址
    3. 参数2.data:请求时携带的参数,与网页?后的参数格式一致
    4. 参数3.success:当请求成功时,处理的函数.
4. 案例:

    ```html
<script type="text/javascript">
    $(function(){
        $("button").click(function(){
            $("#div1").load("s1.do","",function(data){});
        });
    });
</script>
<body>
    <button>刷新数据</button>
    <div id="div1"></div>
</body>
    ```

### ajax请求数据缓存问题
1. 在操作ajax时,浏览器对ajax请求的结果缓存以后,当我们再次向这个地址发起ajax时,浏览器有可能不会再请求服务器,采用上一次的缓存
2. 解决缓存问题:需要先明白缓存的原理,浏览器是按照网址进行缓存的,比如:浏览器不会将百度的缓存给到京东.所以,我们想要浏览器不使用缓存,只需要保证网址不重复就可以了
3. 格式:给请求地址字符串,添加一个时间戳参数
4. 例如:`$.load("s1.do","time="new Date().getTime(),function(){})`

 
















