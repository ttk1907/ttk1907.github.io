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















 
















