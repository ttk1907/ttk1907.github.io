---
layout: post
title:  "Java-MyBatis第一天"
date:   2019-12-03
categories: MyBatis
tags: MyBatis note
---

* content
{:toc}

1. MyBatis第1天:Mybatis的作用、MyBatis 框架的构成 、编写Mybatis程序、Mapper映射器










# MyBatis第1天
## Mybatis的作用 
1. 它支持普通的SQL 操作 , 以及存储过程的调用 
2. 它是一个高级的ORM框架 (以面向对象的思想操作数据库)
3. 它封装了几乎所有的jdbc操作 , 以及参数的手工设置 
4. 自动检索结果集(自动把结果集转换成对象 甚至关联的对象)  

## MyBatis 框架的构成 
1. 实体bean , 封装数据信息 
2. SQL 定义文件 , 封装SQL语句的XML
3. 主配置文件 , 定义连接数据库的信息的 , 加载sql定义文件 等
4. 框架的API , 涉及到SqlSession对象的创建 , 还有SqlSession对应的API , 主要完成增删改查

## 编写Mybatis程序 
1. 建立一个项目 , 导入jar包(mybatis.jar ojdbc6.jar) 
2. 根据表建立对应的实体类  
3. 编写SQL 定义文件 , (拷贝sql定义的模板到一个包中)
4. 拷贝主配置文件模板到src下 , 修改对应的信息 
5. 使用Mybatis的API , 获取SqlSession对象 , 使用这个对象完成对应的sql操作

6. java文件编写

```java
1. 查询代码
SqlSession ss = SqlSessionUtil.getSqlSession();
Account account = ss.selectOne("findAccountById", 2);
System.out.println(account);
ss.close();
2. 增删改代码
使用SqlSession 对应的  insert delete update 
一做增删改不能忘记提交 
```

7. xml文件编写

```xml
1. mapper.*Mapper.xml文件
<!-- 根据账号查账户 -->    
<select id="findAccountById" parameterType="int" 
  resultType="xdl.bean.Account">
     select * from BANK_ACCOUNT where id = #{id}
</select>
2. 如果要传入的参数不止一个,要用对象或者map集合传入参数
<select id="findAcc_NotByAcc_noAndAcc_Password" parameterType="map" resultType="xdl.bean.Account">
    select * from BANK_ACCOUNT where ACC_NO = #{acc_no} AND ACC_PASSWORD = #{acc_password}
</select>
```

## Mapper映射器
1. 作用 : 根据规则设计DAO接口可以自动产生实现类 
2. DAO接口的方法名必须和**SQL定义文件**中**SQL语句**的id保持一致 
3. 接口方法的返回值类型 , 一般和`resultType`保持一致
    1. 查询语句如果返回单值 , 那使用`resultType` 
    2. 查询语句如果可能返回多个值 , 则使用`List<resultType对应的类型>`
    3. 对DML(insert、delete、update) , 可以是返回void,也可以返回int,推荐返回int
4. 接口方法的参数类型 和 parameterType 保持一致 , 如果没有parameterType , 则参数可以任意 
5. SQL定义文件中的namespace 必须是**包名.接口名**    

```java
SqlSession ss = SqlSessionUtil.getSqlSession();
AccountDAO accountDAO = ss.getMapper(AccountDAO.class);
System.out.println(accountDAO.findAccountById(2));
ss.close();
```



