---
layout: post
title:  "Java-Spring框架第二天"
date:   2019-11-26
categories: Frame
tags: Spring note
---

* content
{:toc}

1. Spring第2天:参数的注入、Spring DAO、Spring DAO完成增删改查、自定义模板










# Spring第2天
## 参数的注入
1. 简单值的注入 
    1. 简单值包括**八种基本类型**和**对应的封装类、String、枚举** 
2. 复杂值的注入
    1. 把set注入或者构造器注入中的`value`改成`ref`或者自动化注入 
3. 集合参数的注入 
    1. java中有**List、Map、Set、Properties**可以在Spring 配置文件中配置对应的标记让其创建出对应的对象

```xml
List 
   <list> 
       <value> 值 </value>
   </list>     
Set  
   <set>
         <value> 值 </value>
   </set>
Map 
   <map>
        <entry  key=""   value="" /> 
   </map> 
Properties 
   <props>
       <prop key="15966667777">小泽</prop> 
       <prop key="15966667778">伟杰</prop> 
       <prop key="15966667779">小马</prop> 
   </props>
```

4. 集合参数的单独定义

```xml
<util:list id=""></util:list>
<util:set id=""></util:set>
<util:map id=""></util:map>
<util:properties id=""></util:properties>
```

5. Properties单独定义时可以关联一个.properties文件

```xml
<util:properties id="ref_dbcp" location="classpath:dbcp.properties"></util:properties>
```

## Spring DAO
1. 简介
    1. Spring DAO封装了JDBC简化了DAO实现的类编写 
    2. Spring DAO提供了基于AOP的事务管理   
    3. Spring DAO对JDBC中的异常做了封装,把原来检查异常封装成了继承自RuntimeException的 一个DataAccessException

2. Spring DAO中的核心类 
    1. **JdbcTemplate**:jdbc模板类:可以自动加载驱动、获取连接、执行环境的获取、结果集遍历、以及资源的释放  
    2. **JdbcDaoSupport**:jdbc DAO的支持类:这个类可以提供JdbcTemplate 模板对象

3. 采用继承JdbcDaoSupport的方式完成对数据库的操作 
    1. 建立一张银行账户表,插入几条测试数据,提交
    2.  建立一个项目导入jar包(ioc aop dao 连接池 数据库驱动),拷贝配置文件到src 
    3.  编写DAO 接口:查询银行账户表中的账户的数量
    4.  编写DAO 的实现类:继承 JdbcDaoSupport 实现DAO接口,使用父类提供的模板,结合sql语句完成查询 
    5.  开启组件,在DAO实现类上打**持久层标注**,同时要 给JdbcDaoSupport注入一个dataSource 对象
    6. 创建Spring容器获取DAO并进行测试    

## Spring DAO完成增删改(DML)
### 查询银行账户 
1. 根据id查询银行账户:结果集到对象的转换,需要自己完成---实现RowMapper接口 
    1. 要接收对象,先创建一个实现RowMapper接口的类,重写方法

    ```java
    @Override
    public Account mapRow(ResultSet rs, int i) throws SQLException {
        return new Account(rs.getInt("id"),rs.getString("acc_no"),rs.getString("acc_password"),rs.getInt("acc_money"));
    }
    ```

    2. 重写DAO接口的方法时,第二个参数传入上一个类:`return super.getJdbcTemplate().queryForObject(sql,new AccountMapper(),id);`

### 增加银行账户 
1. 建表:如果有需要建立对应的序列 
2. 建立项目:导入jar包(ioc aop dao 数据库连接池和驱动),拷贝配置文件到src下 
3. 编写一个实体bean
4. 编写DAO接口 
5. 编写DAO的实现类,继承JdbcDaoSupport,实现DAO接口,使用父类模板,根据sql完成对应的操作 
6. 开启组件扫描,给DAO的父类注入dataSource 
7. 封装一个Service,注入DAO,封装业务方法 ----测试   

```java
@Override
public int insertAccount(Account account) {
    try{
        String sql = "insert into bank_account values(bank_account_id_seq.nextval,"+"?,?,?)";
        return super.getJdbcTemplate().update(sql,account.getAcc_no(),account.getAcc_password(),account.getAcc_money());
    }catch (Exception e){
        e.printStackTrace();
    }
    return 0;
}
```

### 删除银行账户
1. 步骤同上

```java
@Override
public int deleteAccount(String acc_no) {
    try{
        String sql = "delete from bank_account where acc_no = ?";
        return super.getJdbcTemplate().update(sql,acc_no);
    }catch (Exception e){
        e.printStackTrace();
    }
    return 0;
}
```

### 修改银行账户

```java
@Override
public int updateAccountByAccount(Account account,int money) {
    try{
        String sql = "update bank_account set acc_money= acc_money + ? where acc_no = ?";
        return jdbcTemplate.update(sql,money,account.getAcc_no());
    }catch (Exception e){
        e.printStackTrace();
    }
    return 0;
}
```

## 自定义模板
1. 不继承JdbcDaoSupport的方式完成 Spring 对数据库的操作 
2. 需要自己定义一个JdbcTemplate 类型的对象,然后注入给DAO的实现类 ,使用自定义的模板对象,完成对应的数据库操作。 
3. 当然自定义模板对象 需要注入dataSource 

```xml
<bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate">
    <constructor-arg index="0" ref="dataSource"/>
</bean>
```
