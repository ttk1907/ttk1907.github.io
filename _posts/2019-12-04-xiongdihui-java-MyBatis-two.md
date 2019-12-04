---
layout: post
title:  "Java-MyBatis第二天"
date:   2019-12-04
categories: MyBatis
tags: MyBatis note
---

* content
{:toc}

1. MyBatis第2天:Spring 和 Mybatis整合、、、、、、、










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
</bean>
```     






























