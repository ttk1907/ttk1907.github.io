---
layout: post
title:  "Java-JSP第二天"
date:   2019-11-19
categories: Java
tags: Java note
---

* content
{:toc}

1. JSP第2天：include、JSP的内置对象、JSP的四大域对象、useBean动作、setProperty动作、getProperty动作









# Java-JSP第二天
## Java--JSP--第2天
### include
1. include指令
    1. 作用:用于将一个JSP或HTML文件引入到另一个JSP中
    2. 格式:`<%@ include file = "引入的路径"%>`
2. include动作
    1. 作用:用于将一个JSP或HTML文件引入到另一个JSP中
    2. 格式:`<jsp:include page="引入的路径" flush="true"/>`
3. 二者的区别
    1. include指令:在JSP文件的转换时期,将被引入的JSP文件嵌入到include指令的位置,然后统一编译执行(最终生成了一个.java文件)
    2. include动作:在JSP程序的转换时期,被引入的文件不会嵌入到include动作的位置,而是等客户端请求时,再临时将被引入的文件以额外的servlet的方式加载到响应中(最终生成多个.java文件)

### JSP的内置对象(隐含对象)
1. 内置对象指的是:JSP引擎在转换JSP文件时,帮我们的代码在执行之前创建一些供我们使用的对象,内置对象具备大量的JSP中的常用功能,使用JSP内置对象可以大大的简化我们的开发流程
2. JSP的九大内置对象
    1. request:
        1. 类型:HttpServletRequest
        2. 作用:请求对象,包含了请求相关的信息和参数
    2. response:
        1. 类型:HttpServletResponse
        2. 作用:响应对象,包含了一些用于响应的功能
    3. out:
        1. 类型:JSPWriter
        2. 作用:是打印流,用于响应体中输出数据
    4. session:
        1. 类型:HttpSession
        2. 作用:会话对象,用于状态管理以及会话跟踪
    5. application:
        1. 类型:ServletContext
        2. 作用:Servlet的上下文,一个应用内存中同时只有一个上下文对象,用于多个Servlet/JSP之间通信
    6. config:
        1. 类型:ServletConfig
        2. 作用:Servlet的配置对象,用于配置一些初始的键值对信息
    7. pageContext:
        1. 类型:PageContext
        2. 作用:页面的上下文,每个JSP都拥有一个上下文对象,用于多段代码之间进行通信
        3. 使用场景:在自定义标签时会频繁使用到PageContext对象;或者是定义一个方法需要用到多个对象时,传一个pageContext对象就能解决问题. 
    8. exception:
        1. 类型:Throwable
        2. 作用:当页面的page指令中isErrorPage属性值为true时,才会存在此对象,用于收集错误信息!通常此对象为null.只有其他页面指定errorPage当前页面时,且其他页面发生BUG后,跳转到此页面时,对象才不为null.
    9. page:
        1. 类型:Object
        2. 作用:指当前JSP页面自身,在JSP引擎生成的代码中,page对象的赋值代码为:Object page = this;

### JSP的四大域对象
1. 域对象的作用:保存数据,获取数据,共享数据.
2. 概念:九大隐含对象中,包含了四个较为特殊的隐含对象,这四个对象我们称其为域对象,它们都具备存储数据/删除数据/获取数据的方法:
    1. 存储数据:`setAttribute(String key,Object value);`
    2. 获取数据:`Object value = getAttribute(String key);`
    3. 删除数据:`removeAttribute(String key);`
3. 这四个域对象,`域`指的是作用域!分别是:
    1. pageContext:页面的上下文   作用域:一个JSP页面
    2. request:请求对象           作用域:一次请求(请求可以被转发,一次请求可能包含多个JSP页面)
    3. session:会话对象           作用域:一次会话(一次会话可能包含多次请求)
    4. application:servlet上下文对象 作用域:一次服务(服务器的启动到关闭,一次服务可能包含多次会话)

### useBean动作
1. 作用:向四大域对象中,存储bean对象
2. 格式:  

```jsp
<jsp:useBean
    id="存储时的key"
    scope="page/request/session/application"
    class="要存储的对象类型">
</jsp:useBean>
案例:
    <jsp:useBean>id="p" scope="page" class="bean.Person"</jsp:useBean>
和
    Person p = new Person();
    pageContext.setAttribute("p",p);  
效果是一样的,就是往page上下文穿了个Person对象 
```  

### useBean+setProperty动作
1. 作用:向四大域对象中,存储bean对象,且设置属性值
2. 格式:  

```jsp
<jsp:setProperty name="存储时的key" property="属性名" value="属性值"/>
这个动作可以出现多次
案例:
<jsp:useBean
    id="p"
    scope="page"
    class="bean.Person">
</jsp:useBean>
<jsp:setProperty name="p" property="name" value="ttk"/>
<jsp:setProperty name="p" property="age" value="18"/>
```

3. 注意:如果setProperty动作中,property的值即是对象的属性名,又是我们用户请求的参数的名称的话,会自动将参数获取到并赋值给对象

### getProperty动作
1. 作用:从四大域对象中,取出某个对象的属性,并显示到网页中
2. 语法格式: 

```jsp
<jsp:getProperty name="对象的key" property="属性名">
案例
<jsp:useBean
    id="per"
    scope="page"
    class="bean.Person">
</jsp:useBean>
<jsp:setProperty name="per" property="name" value="ttk"/>
<jsp:getProperty name="per" property="name">
<jsp:getProperty name="per" property="age">
```


