---
layout: post
title:  "Java-JSP第一天"
date:   2019-11-18
categories: Java
tags: Java note
---

* content
{:toc}

1. JSP第1天：简介、JSP、JSP三大指令、page指令、制定项目全局错误页面










# Java-JSP第一天
## Java--JSP--第1天
### 简介
1. JSP: Java Server Pages 是Java的动态网页技术

### JSP
1. 引擎原理:JSP引擎用于将JSP文件,转换为Servlet
    1. 在服务器启动时,JSP引擎读取JSP文件
    2. 将文件转换为Servlet的代码,并给Servlet添加映射地址为jsp的文件名
    3. 当用户浏览器访问jsp文件名称时,其实请求的不是jsp文件,而是生成的servlet
    4. servlet负责给浏览器进行响应
2. JSP语法结构
    1. JSP文件保存路径:web目录下
    2. JSP文件可以包含HTML代码,Java代码,以及JSP特有的标记
3. Java代码声明区
    1. 指的是Java的成员代码位置,在JSP声明区中编写的Java代码,会生成到servlet的成员位置
    2. 语法:`<%!这里用于编写Java代码,且会生成到声明区%>`
4. Java代码执行区
    1. 指的是Servlet的service方法中,用于每次请求都会执行
    2. 语法:`<%Java代码%>`
5. 表达式
    1. 用于快速的将Java代码中的变量输出到网页中
    2. 语法:`<%=变量名%>`
6. 注释
    1. 因为JSP文件包含了三种语法结构(Java/html/jsp)所以,三种语法结构的注释都可以起到注释的效果
    2. html注释:
        1. 格式:`<!-- html的注释 -->`
        2. 在JSP中,html的注释会被JSP引擎认为是HTML代码,会转换为`out.write("<!-- -->");`
    3. Java注释:
        1. 格式:单行`//`、多行`/* */`、文档`/** */`
        2. 在JSP中,Java的注释会被JSP引擎认为是Java代码,会原封不动的放到_jsp.java文件中
    4. JSP注释:
        1. 格式:`<%-- JSP注释 --%>`
        2. 在JSP引擎将JSP文件转换为.java文件时,会忽略JSP注释的部分

### JSP三大指令
1. 指令的格式:`<%@ 指令名称 属性名=值 属性名2==值 %>`

### page指令
1. 应用:用于设置页面
2. 完整格式:

```
<%@ page
1.基本用不上的
    language="java"
    extends="继承的类"
    buffer="数值|none" -- 缓冲大小,none表示不缓冲,默认是8kb
    session="true|false" -- true:自动创建session,false:表示不自动创建
    autoFlush="true|false" -- true:缓冲器自动清除,默认是true
    isThreadSafe="true|false" -- <%%>中的代码是否是同步的,true表示同步,默认是false
    ContentType="text/html;charset=utf-8" -- 内容类型以及编码格式
2.偶尔用一下
    errorPage="网页地址" -- 当JS代码出现错误,页面由指定的地址进行显示
    isErrorPage="true|false" -- true:当前页面是处理错误的页面.只有为true时,才可以查看异常信息
3.特别重要
    import="导包列表" -- 属性值是一个或多个导入的包,包于包之间使用逗号隔开
    %>
```

### 制定项目全局错误页面
1. 编写项目的web.xml

    ```
在根节点中,加入子节点:
    <error-page>
        <error-code>404</error-code>
        <location>处理404的页面地址</location>
    </error-page>
    ```
















