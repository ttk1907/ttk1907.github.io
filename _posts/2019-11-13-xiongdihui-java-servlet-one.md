---
layout: post
title:  "Java-Servlet第一天"
date:   2019-11-13
categories: Java
tags: Java note
---

* content
{:toc}

1. Servlet第1天：HTTP协议、HttpServlet类









# Java-Servlet第一天
## Java--Servlet--第1天
### HTTP协议
1. HTTP协议：超文本传输协议，是一个应用层的网络传输协议
2. 特点：
    1. 简单，快速
    2. 无连接协议，每次连接服务器只处理一次客户端的请求，处理完毕，立即断开
    3. 无状态协议
    4. 支持多种不同的数据提交方式
    5. 数据传输很灵活，支持任意数据类型
3. 协议的组成部分
    1. 请求
        1. 请求头：请求头部的信息，由一个个键值对组成，描述的是有关客户端的信息
        2. 请求体：GET请求没有请求体，当请求方式为POST时，存在请求体，请求体是用于存储数据的数据容器
        3. 请求空行：请求头部与请求体之间的一行空白
        4. 请求行：描述了请求的方式，有一个个键值对组成，描述的是：远端服务器地址，以及所使用的协议版本等信息
    2. 响应
        1. 响应头：响应头部的信息，由一个个键值对组成，描述的时有关服务器的信息
        2. 响应体：服务器给客户端回复的主体内容
        3. 响应行：描述了响应的协议版本，响应状态码，以及响应成功或失败的相关解释

### HttpServlet类
1. 知乎：servlet的本质是什么，它是如何工作的？
2. 答：
    1. 这个提问的最大一个bug，就是以为servlet是很复杂的东西，事实上，servlet就是一个Java接口，interface! 打开idea，ctrl + shift + n，搜索servlet，就可以看到是一个只有5个方法的interface!
![servlet](/assets/servlet.jpg)
    2. 所以，提问中说的网络协议、http什么的，servlet根本不管！也管不着！
    3. 那servlet是干嘛的？很简单，接口的作用是什么？规范呗！servlet接口定义的是一套处理网络请求的规范，所有实现servlet的类，都需要实现它那五个方法，其中最主要的是两个生命周期方法 init()和destroy()，还有一个处理请求的service()，也就是说，所有实现servlet接口的类，或者说，所有想要处理网络请求的类，都需要回答这三个问题：
        1. 你初始化时要做什么
        2. 你销毁时要做什么
        3. 你接受到请求时要做什么
    4. 这是Java给的一种规范！servlet是一个规范，那实现了servlet的类，就能处理请求了吗？答案是，不能。你可以随便谷歌一个servlet的hello world教程，里面都会让你写一个servlet，相信我，你从来不会在servlet中写什么监听8080端口的代码，servlet不会直接和客户端打交道！
    5. 那请求怎么来到servlet呢？答案是servlet容器，比如我们最常用的tomcat，同样，你可以随便谷歌一个servlet的hello world教程，里面肯定会让你把servlet部署到一个容器中，不然你的servlet压根不会起作用。tomcat才是与客户端直接打交道的家伙，他监听了端口，请求过来后，根据url等信息，确定要将请求交给哪个servlet去处理，然后调用那个servlet的service方法，service方法返回一个response对象，tomcat再把这个response返回给客户端
3. 使用步骤
    1. 编写一个类，继承自HttpServlet
    2. 重写父类的service(HttpServletRequest request,HttpServletResponse response)方法
    3. 在service方法中对用户进行响应
    4. 注意：所有的jar文件都要存在web-inf中的lib文件夹中

4. 案例

```java
public class demo extends HttpServlet {
    /**
     * @param request:请求对象，包含了请求相关的所有信息
     * @param response:响应对象，tomcat提供的用于给客户端响应内容的各种工具
     */
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //1. 设置响应的编码格式以及响应的内容类型
        resp.setContentType("text/html;charset=utf-8");
        //2. 获取用于打印响应体的打印流
        PrintWriter pw = resp.getWriter();
        pw.println("<h1>今晚打老虎！！！</h1>");
        pw.flush();
    }
}
```

5. 将编写好的servlet映射到一个网址上
    1. web3.0之前版本：修改项目中的配置文件xml
    
    ```xml
    <!-- 1. servlet节点，用于将servlet类告知tomcat -->
    <servlet>
        <servlet-name>任意标识符,给servlet起别名</servlet-name>
        <servlet-class>包名.类名</servlet-class>
    </servlet>
    <!-- 2. servlet-mapping,通过别名告知tomcat,某servlet的映射网址
    映射网址，通常以/开头，例如：/demo1，访问网址：http://ip地址:端口号/项目名/demo1 -->
    <servlet-mapping>
        <servlet-name>要添加映射网络的别名<servlet-name>
        <url-pattern>映射的网址</url-pattern>
    </servlet-mapping>       
    ```

    2. web3.0+版本:`加一个注解
@WebServlet("/hello2")`


























