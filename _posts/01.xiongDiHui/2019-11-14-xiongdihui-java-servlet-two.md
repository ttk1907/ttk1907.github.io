---
layout: post
title:  "Java-Servlet第二天"
date:   2019-11-14
categories: Java
tags: Java note
---

* content
{:toc}

1. Servlet第2天：Servlet的生命周期、ServletConfig对象、调整Servlet创建时机、如何接收用户表单的参数、GET和POST的区别、乱码问题









# Java-Servlet第二天
## Java--Servlet--第2天
### Servlet的生命周期
1. 概念：指的是Servlet从创建到消亡的周期
    1. Servlet的创建时机：默认情况，当用户第一次访问Servlet的映射地址时，对象创建
    2. Servlet的消亡时机：tomcat关闭时或项目从tomcat删除时，Servlet被销毁
2. 三个方法的体现
    1. init()方法：此方法在对象创建后，执行
    2. service()方法：服务方法，当用户每一次访问时，执行，用于处理用户的请求，以及对用户进行响应
    2. destroy()方法：当tomcat关闭或项目从tomcat删除时 执行

### ServletConfig对象(了解)
1. 概念：是servlet的配置对象，每一个Servlet都拥有一个ServletConfig。我们在web.xml中进行Servlet配置时，可以向一个Servlet添加初始化的参数。这些参数以键值对的形式存储在ServletConfig中
2. 在web.xml中，向ServletConfig存储数据的格式

```xml
<servlet>
    ···
    <init-param>
        <param-name>键</param-name>
        <param-value>值</param-value>
    </init-param>
</servlet>
```

3. 在Servlet中得到ServletConfig对象的方式
    1. 在Servlet中，重写生命周期init(ServletConfig)方法，使用方法参数中的config对象
    2. 在Servlet的任意代码位置，通过getServletConfig();方法，得到对象
4. 从ServletConfig取出数据的格式
    1. String value = config对象.getInitParameter(String name);

### 调整Servlet创建时机(懒汉变饿汉)
1. 在web.xml中，配置servlet时

```xml
<servlet>
    <servlet-name...>
    <servlet-class...>
    <load-on-startup>数字</load-on-startup>
</servlet>
```

2. load-on-startup:
    1. 取值为数字:(默认值为-1)
        1. 当值为负数时：懒汉模式，第一次请求时加载
        2. 当值>=0时，描述的是请求的顺序，值越小越早加载
        3. 如果多个servlet值相同：按照web.xml中servlet的配置顺序自上而下加载

### 如何接收用户表单的参数
URL: http://网址?a=123&b=456  
GET请求的参数：在网址中，编写在？后，由1个或多个键值对组成，键与值之间使用等号连接，多个键值对之间使用&分割
1. 根据一个name，接收单个参数
    1. String value = request.getParameter(String name)
2. 根据一个name，接收一组参数
    2. String[] values = request.getParameterValues(String name)

### GET和POST的区别
1. GET请求：
    1. 请求的参数以键值对的方式存储在网址中，在网址中，编写在？后，由1个或多个键值对组成，键与值之间使用等号连接，多个键值对之间使用&分割
    2. 只能传输字符串类型的参数
    3. 网址的最大长度为4kb，通常支持的文字2048个文字
    4. 数据传输不安全
2. POST请求：
    1. 请求的数据以键值对的形式存储在请求体中
    2. 请求体是一个单独的数据包，较GET请求而言，安全
    3. 可以传输任意类型的数据
    4. 数据的大小，理论上是无上限的

### 乱码问题
1. 响应的乱码问题
    1. 方式一：针对浏览器，设置网页的内容类型，以及网页的编码格式：`response.setContentType("text/html;charset=utf-8");`
    2. 方式二：针对APP或公众号之类的需要纯文本类型的，设置网页的编码格式(因为没有设置网页内容类型为html，所以浏览器解析时也是乱码)：`response.setCharacterEncoding("utf-8");`
    3. 注意：解决响应乱码的代码必须运行在获取参数之前
2. 请求的乱码问题
    1. 格式一：
        1. 可用于tomcat8版本之前的GET请求乱码以及所有版本的POST请求乱码
        2. 解决方法：将乱码的文字，按照乱码的编码ISO-8859-1转换为字节数组，再按照正常的编码UTF-8组装为文字
    2. 格式二：
        1.  格式1解决乱码适用于参数较少的情况，如果参数过多，解决起来及其麻烦。tomcat为我们提供了设置请求体编码的方式
        2. 注意：只有POST请求，才有请求体
        3. 格式：request.setCharacterEncoding("UTF-8");
    3. 注意：解决请求乱码的代码必须运行在获取参数之前









