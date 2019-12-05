---
layout: post
title:  "Java-MyBatis第二天"
date:   2019-12-04
categories: Frame
tags: MyBatis note
---

* content
{:toc}

1. MyBatis第2天:Spring和Mybatis整合、第二种集成方案、SSM整合










# MyBatis第2天
## Spring 和 Mybatis 整合 
1. SqlSessionFactoryBean  
    1. 产生的是 SqlSessionFactory 类型的对象 , 最终能提供SqlSession
    2. 这个类型依赖于 dataSource 和 Sql 定义文件 
2. MapperFactoryBean 
    1. 产生的是Mapper的实现类
    2. 这个类型依赖于 SqlSessionFactory 和 Mapper接口    
3. 整合步骤
    1. 建立一个项目 , 导入jar包(mybatis.jar、mybatis-spring.jar、ojdbc14.jar、ioc、aop、dao、数据库连接池) , 拷贝Spring配置文件到src 
    2. 编写实体类
    3. 编写SQL定义文件 , 根据id 查询银行账户 
    4. 根据Mapper映射器规则编写DAO 接口
    5. 在Spring配置文件中配置 , SqlSessionFactoryBean : 依赖于dataSource 和 SQL 定义
    6. 在Spring配置文件中配置 MapperFactoryBean , 就可以产生DAO 的实现类
    7. 第6步只能实现一个DAO接口的,可以替换成批量产生Mapper实现类的组件
4. 通过自定义标注 控制接口产生实现类   
    1. 生成一个注解类
    2. 在整合步骤的第7步,可以额外添加一句话实现自定义注解,实现带注解的接口能实例化对象,不带注解的不能自动实例化 

```xml
<!--  创建SqlSessionFactory  -->
<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
    <property name="dataSource" ref="dataSource"/>
    <property name="mapperLocations" value="classpath:xdl/mapper/*.xml"/>
</bean>
<!--  创建Mapper的实现类  -->
<bean id="accountDao" class="org.mybatis.spring.mapper.MapperFactoryBean">
    <property name="sqlSessionFactory" ref="sqlSessionFactory"/>
    <property name="mapperInterface" value="xdl.mapper.AccountDAO"/>
</bean>
<!--  批量产生Mapper实现类的组件  -->
<bean  id="mapperScanner"  class="org.mybatis.spring.mapper.MapperScannerConfigurer">
    <property name="basePackage"  value="xdl.mapper"/>
 <!--  额外添加的一句话,实现4.的功能  -->
    <property name="annotationClass"  value="xdl.annotation.MyAnnotation"/>
</bean>
```     

## 第二种集成方案 
SqlSessionTemplate     
1. 建立一个项目 , 导入jar包(mybatis.jar、mybatis-spring.jar、ojdbc14.jar、ioc、aop、dao、数据库连接池) , 拷贝Spring配置文件到src 
2. 编写实体类
3. 编写SQL定义文件 , 根据id 查询银行账户 
4. 根据Mapper映射器规则编写DAO 接口
5. 在Spring配置文件中配置 , SqlSessionFactoryBean : 依赖于dataSource 和 SQL 定义
6. 编写DAO的实现类 , 实现DAO接口 , 并注入SqlSessionTemplate 类型的对象 。 这个对象依赖于sqlSessionFactory。利用SqlSessionTemplate 对应的API 完成操作。
7. 注意创建DAO实现类组件 , 需要组件扫描 

```xml
<!--  创建SqlSessionTemplate类型的对象  -->
<bean  id="sqlSessionTemplate"  class="org.mybatis.spring.mapper.SqlSessionTemplate">
    <constructor-org index="0" ref="sqlSessionFactory"/>
</bean>
<!-- 组件扫描  -->
<context:component-scan base-package="xdl"/>
```

## SSM整合
**以登录为例完成SSM架构的搭建** 
1. 将Mybatis 和 Spring 进行整合(以MapperScannerConfigurer最终提供Service)
    1. 建立一个项目 , 导入jar包(ioc、aop、dao、mvc、mybatis、mybatis-spring、数据库连接池、数据库驱动) , 拷贝spring配置文件到src下  
    2. 根据表 建立实体类 
    3. 编写SQL 定义文件 , 根据账号 和 密码进行查询 
    4. 编写DAO 接口 
    5. 在Spring 容器中创建 SqlSessionFactoryBean , 提供SqlSessionFactory , 依赖dataSource 和 Sql定义文件 
    6. 创建 MapperScannerConfigurer 批量产生DAO实现类 , 依赖于basePackage 和 SqlSessionFactory
    7. 编写Service类 , 提供业务方法 , 根据账号和密码进行登录 , 然后开启组件扫描 , 在容器中创建 Service 对应的对象测试 
2. [搭建基于标注的Spring MVC](https://ttk1907.github.io/2019/11/27/xiongdihui-java-Spring-three/#spring-mvc-%E7%9A%84%E7%BC%96%E7%A8%8B%E6%AD%A5%E9%AA%A42)
3. 编写控制器方法 , 让页面请求结合到控制器方法  
    1. 控制器方法中使用 Service 完成登录 , 根据结果 做页面跳转 





















