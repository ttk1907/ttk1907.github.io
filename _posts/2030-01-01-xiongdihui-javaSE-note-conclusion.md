---
layout: post
title:  "Java和数据库各阶段总结"
date:   2030-01-01
categories: Java
tags: Java note
---

* content
{:toc}

1. Java和数据库各阶段总结
2. 置顶以供查询笔记









# JavaSE阶段总结
## 一、Java入门篇-编程基础
1. [基础第1天](https://ttk1907.github.io/2019/10/16/xiongdihui-java-note-one/)：Java版本、开发环境
2. 基础第2天：变量、注释、API的使用、数据类型和转换
3. 基础第3天：运算符、分支结构
4. [基础第4天](https://ttk1907.github.io/2019/10/17/xiongdihui-java-note-two/)：循环结构
5. 基础第5天：一维数组、二维数组
6. JavaSE阶段第一个小阶段的总结

## 二、Java进阶篇-面向对象
1. [面向对象第1天](https://ttk1907.github.io/2019/10/18/xiongdihui-java-note-three/)：面向对象编程的概念、类、对象以及引用、成员方法
2. 面向对象第2天：构造方法和方法重载、this关键字、方法的传参和递归调用
3. [面向对象第3天](https://ttk1907.github.io/2019/10/21/xiongdihui-java-note-four/)：封装、static关键字、单例设计模式、继承
4. [面向对象第4天](https://ttk1907.github.io/2019/10/22/xiongdihui-java-note-five/)：继承、访问控制、final关键字
5. 面向对象第5天：多态、抽象类、接口
6. JavaSE阶段第二个小阶段的总结

## 三、Java深入篇-核心类库
1. [核心类库第1天](https://ttk1907.github.io/2019/10/23/xiongdihui-java-note-six/)：Object类、包装类和数学处理类
2. [核心类库第2天](https://ttk1907.github.io/2019/10/24/xiongdihui-java-note-seven/)：String类的常用方法、StringBuilder类和StringBuffer类、日期相关的类、多态的三种使用场合
3. [核心类库第3天](https://ttk1907.github.io/2019/10/25/xiongdihui-java-note-eight/)：集合结构、Collection集合、List集合、泛型机制
4. 核心类库第4天：Queue集合、Set集合、Map集合
5. [核心类库第5天](https://ttk1907.github.io/2019/10/28/xiongdihui-java-note-nine/)：异常机制、File类、IO流、FileOutputStream类
6. 核心类库第6天：FileInputStream类、BufferedWriter类、BufferedReader类、PrintStream类、ObjectOutputStream类、ObjectInputStream类、经验分享、transient关键字
7. [核心类库第7天](https://ttk1907.github.io/2019/10/29/xiongdihui-java-note-ten/)：线程
8. [核心类库第8天](https://ttk1907.github.io/2019/10/30/xiongdihui-java-note-eleven/)：线程的同步机制、网络编程常识、基于tcp协议的编程模型
9. [核心类库第9天](https://ttk1907.github.io/2019/10/31/xiongdihui-java-note-twelve/)：常用的设计原则、常用的设计模式、常用的查找算法、冒泡排序算法

# JavaWeb阶段总结
## 一、Java-Jdbc
1. [Jdbc第1天](https://ttk1907.github.io/2019/11/08/xiongdihui-java-database-one/)：DBC访问数据库的步骤、JDBC原理图
2. [Jdbc第2天](https://ttk1907.github.io/2019/11/11/xiongdihui-java-database-two/)：使用PreparedStatement 替换 Statement、工具类、配置文件、DAO
3. Jdbc第3天：JDBC事务的概念、JDBC事务操作格式、批处理、连接池、DBCPUtil工具类、数据库优化

## 二、Java-Servlet
1. [Servlet第1天](https://ttk1907.github.io/2019/11/13/xiongdihui-java-servlet-one/)：HTTP协议、HttpServlet类
2. [Servlet第2天](https://ttk1907.github.io/2019/11/14/xiongdihui-java-servlet-two/)：Servlet的生命周期、ServletConfig对象、调整Servlet创建时机、如何接收用户表单的参数、GET和POST的区别、乱码问题
3. [Servlet第3天](https://ttk1907.github.io/2019/11/15/xiongdihui-java-servlet-three/)：编程习惯、线程安全问题、请求的转发、请求的重定向
4. Servlet第4天：HttpServletRequest类、ServletContext上下文、会话跟踪、Cookie技术、Session技术

## 三、Java-JSP
1. [JSP第1天](https://ttk1907.github.io/2019/11/18/xiongdihui-java-JSP-one/)：简介、JSP、JSP三大指令、page指令、制定项目全局错误页面
2. [JSP第2天](https://ttk1907.github.io/2019/11/19/xiongdihui-java-JSP-two/)：include、JSP的内置对象、JSP的四大域对象、useBean动作、setProperty动作、getProperty动作
3. [JSP第3天](https://ttk1907.github.io/2019/11/20/xiongdihui-java-JSP-three/)：重写URL得到Session、EL表达式、EL表达式,取出数据的流程、taglib指令、JSTL标签库
4. [JSP第4天](https://ttk1907.github.io/2019/11/21/xiongdihui-java-JSP-four/)：过滤器、过滤器链、Listener

## 四、Ajax
1. [Ajax第1天](https://ttk1907.github.io/2019/11/22/xiongdihui-java-Ajax-one/)：GET请求的使用步骤、POST请求的使用步骤、GSON.jar
2. Ajax第2天：ajax函数、get函数与post函数、getJSON函数、Load与缓存问题

# Java框架阶段总结
## 一、Java-Spring
1. [Spring第1天](https://ttk1907.github.io/2019/11/25/xiongdihui-java-Spring-one/)：项目开发思路MVC、
Spring 框架的构成、什么是IOC、Spring 容器、使用Spring容器完成IOC的步骤、Spring容器创建对象的三种方式、Spring中对象的作用域、
Spring容器中的对象的初始化和销毁、bean对象的延迟实例化、什么是DI、DI的三种实现方式、组件扫描
2. [Spring第2天](https://ttk1907.github.io/2019/11/26/xiongdihui-java-Spring-two/)：参数的注入、Spring DAO、Spring DAO完成增删改查、自定义模板
3. [Spring第3天](https://ttk1907.github.io/2019/11/27/xiongdihui-java-Spring-three/)：Spring的声明式事务、Spring Web MVC、Spring MVC 的编程步骤、Spring MVC接受请求的参数
4. [Spring第4天](https://ttk1907.github.io/2019/11/28/xiongdihui-java-Spring-four/)：如何把控制器的数据传递给页面、中文参数乱码问题、拦截器
5. [Spring第5天](https://ttk1907.github.io/2019/11/29/xiongdihui-java-Spring-five/)：Spring 的异常处理、文件上传、Spring MVC的控制器方法 如何返回 JSON、rest、使用rest完成增加、使用rest完成更新
6. [Spring第6天](https://ttk1907.github.io/2019/12/02/xiongdihui-java-Spring-six/)：Spring AOP、AOP中涉及到概念、Spring 实现AOP的步骤、切点表达式的写法、AOP中的五种通知类型、基于标注的AOP实现、异常通知、环绕通知

## 二、Java-MyBatis
1. [MyBatis第1天](https://ttk1907.github.io/2019/12/03/xiongdihui-java-MyBatis-one/)：Mybatis的作用、MyBatis 框架的构成 、编写Mybatis程序、Mybatis多个参数的处理、Mapper映射器、分页的实现
2. [MyBatis第2天](https://ttk1907.github.io/2019/12/04/xiongdihui-java-MyBatis-two/)：Spring和Mybatis整合、第二种集成方案、SSM整合

# 数据库阶段总结
## 一、MySQL
1. [MySQL学习资料](https://ttk1907.github.io/2019/09/27/xiongdihui-Mysql-note/)：SQL语句的分类、库和表的基础操作、对数据的基础操作、MySQL中的存储引擎、数据类型、MySQL类型约束、修改表结构、MySQL中表的索引、MySQL中的分页

## 二、Oracle
1. [Oracle基础学习笔记1](https://ttk1907.github.io/2019/10/08/xiongdihui-oracle-note-one/)：常用指令、sql简介、scott用户表的结构、sql简单查询、限定查询、排序查询、综合练习
2. [Oracle基础学习笔记2](https://ttk1907.github.io/2019/10/09/xiongdihui-oracle-note-two/)：单行函数、多表查询、表的连接、数据集合操作
3. [Oracle基础学习笔记3](https://ttk1907.github.io/2019/10/10/xiongdihui-oracle-note-three/)：统计函数、分组统计、sql查询语句最终结构、where与having的区别、综合练习
4. [Oracle基础学习笔记4](https://ttk1907.github.io/2019/10/11/xiongdihui-oracle-note-four/)：子查询、复杂查询、增加数据、修改数据、删除数据、事务处理、认识死锁、数据伪列、约束条件

## 三、Redis(还需要学习)
1. [Redis基础学习笔记1](https://ttk1907.github.io/2019/10/14/xiongdihui-redis-note-one/)：NOSQL是什么、为什么需要NOSQL、NOSQL数据库的四大分类、NOSQL特点、Redis概述
2. [Redis基础学习笔记2](https://ttk1907.github.io/2019/10/15/xiongdihui-redis-note-two/)：常用命令


