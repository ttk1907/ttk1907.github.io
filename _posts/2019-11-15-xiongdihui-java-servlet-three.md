---
layout: post
title:  "Java-Servlet第三天"
date:   2019-11-15
categories: Java
tags: Java note
---

* content
{:toc}

1. Servlet第3天：编程习惯、线程安全问题、请求的转发、请求的重定向
2. Servlet第4天：HttpServletRequest类、ServletContext上下文、会话跟踪、Cookie技术、Session技术









# Java-Servlet第三天
## Java--Servlet--第3天
### 编程习惯
1. 编程习惯：先将要用的方法写在dao接口中

### 线程安全问题
1. Servlet的service方法，每次被请求时，调用
2. 这个调用比较特殊，是在新的子线程中调用的，当servlet方法执行完毕，子线程死亡了
3. 可以简单的理解为：service方法每次执行都是一个新的线程
4. [加锁的操作](https://ttk1907.github.io/2019/10/30/xiongdihui-java-note-eleven/)
```java
Object o = new Object();//相当于一把锁
synchronized(o){
    想要加锁的代码块;
}
```

### 请求的转发
1. 概念：一个web组件将未处理完毕的请求，通过tomcat转交给另一个web组件处理
2. 步骤
    1. 获取请求转发器：RequestDispatcher rd = request.getRequestDispatcher("转发的地址");
    2. 通过转发器发起转发：rd.forward(request,response);
3. 转发流程
    1. 当浏览器访问服务中的comcat时
    2. tomcat将请求信息，与响应工具进行封装，传递给我们的Servlet的service方法进行处理
    3. 我们在service方法中，得到转发器，通过请求转发器告知tomcat，请求转发的地址
    4. tomcat接收到请求转发需求，会重新封装请求信息，将请求对象与响应对象传递给转发地址的Servlet的service方法进行处理
4. 特点
    1. 转发过程中，多个Servlet之间共享一份请求信息，共享一个响应对象
    2. 转发只能发生在同一个服务器中(转发无法实现跨域)
    3. 无论转发发生多少次，对于浏览器来说，只发起过一次请求，并且只接到了一次响应
    4. 相对于重定向来说，效率更高
5. 注意： 
    1. 在一次用户的操作中，可以无限制的进行转发和重定向，但是记住：一定要存在出口
    2. 当servlet的请求已经被转发/重定向后，在此servlet后续的代码中不能再进行响应

### 请求的重定向
1. 概念：响应时，告知浏览器新的请求地址，浏览器接收到自动请求新的地址
2. 步骤
    1. 回复重定向地址：response.sendRedirect("重定向地址");
3. 重定向流程
    1. 当浏览器访问服务时，服务器对浏览器响应一个302的状态码，以及一个location的地址
    2. HTTP协议约定，当浏览器接收到302状态码时，会自动寻找location地址，并发起新的请求(相当于控制用户浏览器，自动完成页面的跳转操作)
4. 特点
    1. 重定向会产生新的请求和新的响应
    2. 使用重定向，可以在多个服务器之间发生(可以跨域操作)
    3. 浏览器地址栏的内容会发生改变
    4. 请对于请求转发而言，效率较低
5. 注意： 
    1. 在一次用户的操作中，可以无限制的进行转发和重定向，但是记住：一定要存在出口
    2. 当servlet的请求已经被转发/重定向后，在此servlet后续的代码中不能再进行响应

## Java--Servlet--第4天
### HttpServletRequest类
1. 常用操作
    1. 获取访问的客户端的ip地址:`String ip = request.getRemoteAddr();`
    2. 获取客户端访问的地址(有可能因为服务器映射了多个域名,多个用户的访问地址不同):`request.getRequestURI();`
    3. 获取服务器的名称(通常获取的是ip):`request.getServerName();`
    4. 获取端口号:`request.getServerPort();`
    5. 获取请求的方式:`String method = request.getMethod();`
    6. 获取get请求的参数列表(网址中?后面的部分):`String params = request.getQueryString();`
2. 三个将请求对象作为数据容器使用的方法:
    1. 存储数据:`request.setAttribute(String key,Object value);`
    2. 获取数据:`Object value = request.getAttribute(String key);`
    3. 删除数据:`request.removeAttribute(String key);`

### ServletContext上下文
1. ServletContext类 
    1. 每一个Servlet都是一个独立的用于处理请求的对象,为了便于多个Servlet之间的数据交流.JavaWeb提供了一个上下文对象ServletContext!
    2. 我们在任何的Servlet代码中,都可以获得这个ServletContext对象,且每一个Servlet获取的都是同一份ServletContext对象.
    3. 上下文对象,类似于我们SE所学习的MAP集合,是一个键值对的容器
    4. 作用:ServletContext是Servlet之间通信的桥梁,用于多个Servlet之间信息的共享
2. 如何从Servlet中得到ServletContext对象
    1. 语法格式:ServletContext context = getServletContext();
3. ServletContext的常用方法
    1. 存储数据:`context.setAttribute(String key,Object value);`
    2. 获取数据:`Object value = context.getAttribute(String key);`
    3. 删除数据:`context.removeAttribute(String key);`
    4. 获取项目运行时的文件夹绝对路径:`String path = context.getRealPath("/");`
4. 注意:
    1. 因为一个项目中只有一个ServletContext对象,且在项目启动时创建了,项目销毁时销毁,所以我们在一次项目启动的过程中,一个Servlet存储的数据,任何Servlet都可以获取到

### 会话跟踪(状态管理)
1. 概念:Http协议是无状态的,我们的服务器在与客户端进行交互时,没有记忆,有两种方式来实现状态管理
    1. Cookie技术:将状态,存储到客户端中
    2. Session技术:将id存储在客户端中,将状态存储在服务器中

### Cookie技术
1. 实现步骤以及原理
    1. 当服务器向客户端响应时,可以向响应头部加入Cookie,每一个Cookie表是一个键值对.
    2. 浏览器在接收到响应后,如果存在Cookie,则会将Cookie存储在文本文件中(.txt)
        1. 存储时,会存储的信息有:服务的域,路径,Cookie键,Cookie值,存储时长
    3. 当浏览器向客户端请求时,会遍历Cookie文本文件,将匹配新请求地址的Cookie携带上,放在请求头部,发送给服务器!
        1. Cookie匹配的规则:当Cookie存储的域相同时,路径匹配时才会将Cookie发送给服务器
2. 如何创建Cookie
    1. Cookie在Java中的体现就是一个表示键值对的Java类,类名为:Cookie
    2. 格式:`Cookie cookie = new Cookie(String name,String value);`
3. 如何将Cookie添加到响应头部
    1. 通过响应对象,将Cookie添加到响应头部
    2. 格式:`response.addCookie(Cookie cookie);`
    3. 一次响应,可以添加n个Cookie,如果浏览器中已经存储过与某个Cookie的name相同的Cookie,再次存储时会覆盖value
4. 如何从请求头部得到之前存储过的所有Cookie
    1. 因为一个域何路径下,可能存在多个Cookie,所以获取的不是单个Cookie,而是一个数组:`Cookie[] cookies = request.getCookies();`
    2. 如果从未存储过,则返回的数组值是null;
5. 得到Cookie后,如何取出其中的键和值
    1. 获取Cookie的键:`String name = cookie.getName();`
    2. 获取Cookie的值:`String value = cookie.getValue();`
6. 如何调整Cookie存储时长
    1. 格式:`cookie.setMaxAge(int 秒);`
    2. 传入的值:
        1. 负数:默认-1,表示浏览回话结束时删除
        2. 正数:存活的秒数
        3. 0:经常用于覆盖一个cookie时使用,作用为0秒后删除(立即删除)    
7. Cookie存储时,路径解决的问题
    1. 路径匹配的规则
        1. Cookie的替换:只能由相同域,相同的路径完成替换
        2. Cookie的获取:只能由相同域,相同的路径或子路径获取
    2. 例如:
        1. A地址:localhost/x/a.do
        2. B地址:localhost/x/b.do
        3. C地址:localhost/c.do
        4. A存储数据时:a/b可以获取,a/b可以替换,c不能获取也不能替换
        5. C存储数据时:a/b/c可以获取,c可以替换
    3. Cookie的路径问题,经常影响我们的开发,JavaWeb给我们提供了一个Cookie的方法,用于设置Cookie的路径,通常我们会将Cookie的路径设置为/(根路径)
    4. 语法格式:`cookie.setPath("/");`
8. Cookie的优缺点
    1. 缺点
        1. Cookie存储的数据类型有限制,只能是字符串
        2. 数据存储的大小有限制,最大为4kb
        3. 数据存储在用户的计算机上,不安全
        4. 受限于用户的浏览器设置,当浏览器禁止使用Cookie时,Cookie就无法在存储了
    2. 优点
        1. 数据存储在客户端,分散了服务器的压力

### Session技术
1. 概念:基于Cookie实现的技术,是Java中的一个键值对的容器,就像我们常用的MAP集合
2. 技术原理
    1. 浏览器访问服务器时,服务器可以选择创建的Session对象.
    2. Session对象在创建时,会生成一个id,我们称其为sessionid,sessionid是session的密钥,是唯一的!
    3. Session创建完毕后,会自动将sessionid以cookie的形式存储到用户的浏览器中.
    4. 当浏览器再次访问服务器时,会自动携带sessionid发送给服务器
    5. 服务器得到sessionid后,会去匹配找到对应的session对象,供用户使用.
3. 如何获取session对象
    1. 在Java中,session是一个Java对象,对象的类型为:HttpSession
    2. 获取Session对象的格式
        1. 无参方法:`HttpSession session = request.getSession();`内部调用了一参方法,且传入true
        2. 一参方法:`HttpSession session = request.getSession(boolean isNew);`
        3. 用于获取session参数:
            1. true:根据当前浏览器传入的sessionid,寻找session对象并返回,如果不存在,则创建新的session并返回
            2. false:根据当前浏览器传入的sessionid,寻找session对象并返回,如果不存在,则返回null;
4. session的常用方法
    1. 存储数据:`session.setAttribute(String key,Object value);`
    2. 获取数据:`Object value = session.getAttribute(String key);`
    3. 删除数据:`session.removeAttribute(String key);`
    4. 销毁session(应用场景:退出登录):`session.invalidate();`
5. Session的存活时长
    1. Session的默认时长为:30分钟
    2. 指的是:举例用户的上一次访问大于30分钟后,session自动删除
    3. 设置session时长:
        1. 修改单个session的时长:`session.setMaxInactiveInterval(int 秒);`
        2. 修改tomcat下,所有的session的默认时长:独立环境:寻找tomcat/conf/web.xml文件
        3. 修改web.xml中session-config节点`<session-config><session-timeout>数值分钟</session-timeout></session-config>`
6. session的优缺点
    1. 优点:
        1. 数据存储在服务器中,安全
        2. session存储时的值类型为:Object,可以存储任意类型数据
        3. 可存储的数据大小,理论上是无上限的
    2. 缺点:数据在服务器的内存中存储,内存通常是有限的,会对服务器造成大量的压力,很容易耗尽服务器资源
7. Cookie技术和Session技术不是互斥的
    1. Cookie和session是结合使用的
    2. 通常:
        1. 对于安全不敏感的数据,建议使用Cookie存储
        2. 对于安全敏感的数据.建议使用session存储
        3. 对于安全敏感,且较大的数据,存储在数据库























