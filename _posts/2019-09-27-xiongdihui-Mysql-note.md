---
layout: post
title:  "MySQL学习资料"
date:   2019-09-27
categories: MySQL
tags: MySQL note
---

* content
{:toc}

MySQL学习笔记








### MySQL基础操作命令
##### 一、库和表的基础操作
1.如何使用cmd链接mysql服务,进入mysql数据库
```
1.win+R输入cmd打开DOS窗口
2.输入mysql -u root -p回车
3.如果有密码就输入，如果没有回车直接跳到第4步
4.执行完以上3步，界面会出现Welcome to the MySQL monitor.的字样，代表链接成功
```
2.查看mysql所有的库
```
命令:show databases;
注释:展示 数据库
结果:返回当前mysql中所有的库的列表
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
```
3.如何使用mysql中的库
```
命令:use mysql
注释:使用 库名
结果:Database changed
```
4.如何创建库
```
命令:create database itxdl default charset=utf8;
注释:创建   数据库      库名  默认    字符集为utf8（作用：让数据库中的表可以存储中文信息）
结果:Query OK, 1 row affected, 1 warning (0.13 sec)
```
5.如何创建表
```
命令:
create table user(
    id int,
    name varchar(30),
    age int,
    sex char(1)
);
注释:
创建 表  表名(
    字段名 字段类型,
    字段名 字段类型,
    字段名 字段类型,
    字段名 字段类型,
);
结果:Query OK, 0 rows affected (0.34 sec)
```
6.如何查看库中所有的表
```
命令:show tables;
注释:展示 表
结果:{
    1.如果没有表，则返回Empty set (0.00 sec)
    2.如果有表，则返回该库中所有的表
    例:+-----------------+
       | Tables_in_itxdl |
       +-----------------+
       | user            |
       +-----------------+
}
```
7.查看当前表的结构
```
命令:desc user;
注释:结构 表明
结果:+-------+-------------+------+-----+---------+-------+
     | Field | Type        | Null | Key | Default | Extra |
     +-------+-------------+------+-----+---------+-------+
     | id    | int(11)     | YES  |     | NULL    |       |
     | name  | varchar(30) | YES  |     | NULL    |       |
     | age   | int(11)     | YES  |     | NULL    |       |
     | sex   | char(1)     | YES  |     | NULL    |       |
     +-------+-------------+------+-----+---------+-------+
    1.Field代表的是字段
    2.Type代表的是字段类型
    3.NULL代表的是该字段的值是否可以为空（YES是可以为空，NO是不可以为空）
    4.Key代表的是该字段的键
    5.Extra代表的是该字段的其他属性
```
8.查看建表语句
```
命令:show create table user;
注释:展示 创建     表    表名
结果:| user  | CREATE TABLE `user` (
      `id` int(11) DEFAULT NULL,
      `name` varchar(30) DEFAULT NULL,
      `age` int(11) DEFAULT NULL,
      `sex` char(1) DEFAULT NULL
     ) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
```
##### 二、对数据的基础操作（添加，删除，修改，查看）
1.添加语句
```
命令:{
        1.insert into user(id,name,age,sex) values(1001,'张三',18,'男');
        注释:添加语句关键字 表名(字段名,多个字段以','间隔) 值(与字段名对应的字段值,多个值以','间隔)
        2.insert into user values(1002,'李四',20,'女');
        注释:添加语句关键字 表明 值(与字段名按顺序对应的字段值,多个值以','间隔)
    }
结果:Query OK, 1 row affected (0.05 sec)
```
2.查看语句
```
命令:select * from user;
注释:查看   所有数据 从 表名
结果:+------+--------+------+------+
     | id   | name   | age  | sex  |
     +------+--------+------+------+
     | 1001 | 张三   |   18 | 男   |
     | 1002 | 李四   |   20 | 女   |
     +------+--------+------+------+
```
3.修改语句
```
命令:update user set age=38 where id = 1001;
注释:更新   表名 设置 要修改的字段 条件
结果:Query OK, 1 row affected (0.04 sec)
     Rows matched: 1  Changed: 1  Warnings: 0
```
4.删除语句
```
命令:delete from user where id = 1002;
注释:删除   从   表名 条件
结果:Query OK, 1 row affected (0.07 sec)
```
##### 三、MySQL中的存储引擎
1.mysql中的存储引擎分类
```
1.InnoDB{
    1.支持事务
    2.存储结构是由两个文件组成{
        1.数据表结构(.frm)，写入速度没有Myisam快
        2.数据和索引(.ibd)
    }
}
2.Myisam{
    1.不支持事务
    2.存储结构是由三个文件组成{
        1.表结构(.frm)
        2.数据(.MYD)
        3.索引(.MYI)
    }
}
```
2.学术用语
```
1.DBMS:数据库管理软件
2.DBA:数据库管理工程师
```
3.设置表引擎
```
1.在my.ini中设置
2.建表的时候设置{
    关键词:在表后加engine=myisam
    命令:create table myuser(
        id int,
        name varchar(30),
        sex char(6),
        age int
    )engine=myisam;
}
```
4.修改表引擎
```
命令:alter table user engine=InnoDB
注释:修改表结构关键字 表 表明 引擎 要修改的引擎名称
结果:Query OK, 0 rows affected (0.45 sec)
     Records: 0  Duplicates: 0  Warnings: 0
```
##### 四、数据类型
1.数据类型的分类
```
1.字符串类型{
    1.char():定长字符串，存储长度0-255个字符
    2.varchar():不定长字符串，存储长度0-65535个字符
    3.text:文本类型,存储长度0-65535个字符，索引必须限制长度255
    4.enum:枚举类型，例enum('男','女','未知')
}
2.数字类型{
    1.int:数字类型，无符号（存储长度0-42亿），有符号（存储长度-21亿-21亿）
    2.tinyint:小的数字类型，1字节（8位）,无符号（存储长度0-255），有符号（存储长度-128-127）
    3.float:浮点类型
    4.decimal:小数类型，例:decimal(5,2)表示数值总共5位，小数占2位
}
3.时间日期{
    1.date:年月日
    2.time:时分秒
    3.datetime:年月日时分秒
}
4.注意{
    二进制（一般不再数据库中存储多媒体文件等二进制数据）
}
```
##### 五、MySQL类型约束
1.类型约束种类
```
1.unsigned:无符号
2.字段类型后边加括号限制长度(30)
3.not null:不能为空，在操作数据库时如果输入该字段的数据为NULL,语句就会报错
4.default:设置默认值
5.primary key:主键(不能为空且唯一)
6.auto_increment:定义字段列为自增属性，一般用于主键，数值会自动加1
7.unique:唯一索引(数据不能重复，一般用在用户名和电话字段)，可以增加查询(select)速度，但是会降低添加(insert)和更新(update)速度
```
2.用类型约束建表实例:
```
命令:create table ayi(
    id int unsigned auto_increment primary key,
    name varchar(30) not null,
    age tinyint not null default 20
);
结果:+-------+------------------+------+-----+---------+----------------+
     | Field | Type             | Null | Key | Default | Extra          |
     +-------+------------------+------+-----+---------+----------------+
     | id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
     | name  | varchar(30)      | NO   |     | NULL    |                |
     | age   | tinyint(4)       | NO   |     | 20      |                |
     +-------+------------------+------+-----+---------+----------------+
```
##### 六、修改表结构
1.添加字段
```
命令:alter table ayi add sex char(1) not null;
注释:修改表结构的关键字  表  表名 添加字段 约束类型
结果:Query OK, 0 rows affected (0.22 sec)
     Records: 0  Duplicates: 0  Warnings: 0
```
2.修改字段类型（modify）
```
命令:alter table ayi modify sex tinyint(1) not null default 1;
注释:修改表结构的关键字  表 表名 修改类型关键字 字段名 约束类型
结果:Query OK, 0 rows affected (0.64 sec)
     Records: 0  Duplicates: 0  Warnings: 0
```
3.修改字段名称（change）
```
命令:alter table ayi change sex SEX tinyint(4) not null default 20;
注释:修改表结构的关键字 表  表名 修改的字段原名字 要修改成的名字 原字段有的约束类型
结果:Query OK, 0 rows affected (0.14 sec)
     Records: 0  Duplicates: 0  Warnings: 0
```
4.修改自增(auto_increment)的初始值
```
命令:alter table ayi AUTO_INCREMENT=1000
注释:修改表结构的关键字 表 表名 AUTO_INCREMENT 从几开始
结果:Query OK, 0 rows affected (0.07 sec)
     Records: 0  Duplicates: 0  Warnings: 0
```
5.删除表
```
命令:drop table myuser;
注释:删除表的关键字 表 表名
结果:Query OK, 0 rows affected (0.24 sec)
```
##### 七、MySQL中表的索引
1.什么是索引，索引的作用是什么
```
作用:提高（select）查询速度
概念:索引就像是一本书中的目录
```
2.索引的类型
```
1.主键索引:不能为空且唯一，每个表中只能有一个
2.唯一索引:必须是唯一的
3.普通索引:就是很普通的索引
4.全文索引:全文索引在MySQL8.0之前的版本只适用于英文文本
```
3.给ayi表中的name字段添加唯一索引，索引名为ayi_name
```
命令:alter table ayi add unique ayi_name(name);
注释:修改表结构的关键字 表 表名 添加 唯一索引 索引名 需要添加的字段
结果:Query OK, 0 rows affected (0.29 sec)
     Records: 0  Duplicates: 0  Warnings: 0
```
4.给ayi表中的age字段添加普通索引，索引名为index_age
```
命令:alter table ayi add index index_age(age);
注释:修改表结构的关键字 表 表名 添加 普通索引 索引名 需要添加的字段
结果:Query OK, 0 rows affected (0.21 sec)
     Records: 0  Duplicates: 0  Warnings: 0
```
5.将ayi表中的age字段的index_age索引删除
```
命令:alter table ayi drop index index_age;
注释:修改表结构的关键字 表 表名 删除 普通索引 索引名
结果:Query OK, 0 rows affected (0.11 sec)
     Records: 0  Duplicates: 0  Warnings: 0
```
6.将ayi表中的id字段的主键删除
```
1.先取消当前主键的自增属性{
    命令:alter table ayi modify id int;
    注释:修改表结构的关键字 表 表名 修改字段关键字 字段 约束类型
    结果:Query OK, 2 rows affected (0.53 sec)
         Records: 2  Duplicates: 0  Warnings: 0
}
2.删除主键索引{
    命令:alter table ayi drop primary key;
    注释:修改表结构的关键字 表 表名 删除 主键
    结果:Query OK, 2 rows affected (0.51 sec)
         Records: 2  Duplicates: 0  Warnings: 0
}
```









