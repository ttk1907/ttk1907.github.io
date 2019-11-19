---
layout: post
title:  "Oracle基础学习笔记1"
date:   2019-10-08
categories: Oracle
tags: Oracle note
---

* content
{:toc}

Oracle基础学习笔记1








# Oracle基础学习笔记1

## 第一节课:常用指令
1. 设置每一行长度 set linesize 300;
2. 设置一页显示数据数量 set pagesize 30;
3. 启动记事本程序 ed(同linux下的vi) mldn(数据库全局名称);
4. 执行文件命令 @mldn(文件名称)
5. 在sqlplus下使用如下语法切换用户:
    * conn 用户名/密码
    * 登录sys必须要在后面加[AS SYSDBA]
6. 命令前加host可以调用本机命令
7. distinct 是去重的意思

## 第二节课
### 知识点:
1. 认识sql的介绍
2. 掌握scott用户的数据表结构

### sql简介
1. sql语法单词:select、from、where、group by、having、order by、insert、create、 drop、alter、grant、revoke

### scott用户表的结构
1. 查询一个用户下的所有表`select * from tab`
2. 查询一个表结构 `desc 表名称`
3. 部门信息表(dept)
    * deptno number(2) 表示部门编号,最多有两个字符组成
    * dname varchar2(14) 表示部门名称,最多由14个字符组成
    * loc varchar2(13) 部门位置
4. 雇员信息表(emp)
    * EMPNO   NOT NULL NUMBER(4)
    * ENAME    VARCHAR2(10)
    * JOB      VARCHAR2(9)
    * MGR      NUMBER(4)
    * HIREDATE DATE
    * SAL      NUMBER(7,2) [小数点最多只占2位,整数最多占5位]
    * COMM     NUMBER(7,2) [佣金]
    * DEPTNO   NUMBER(2)
5. 工资等级表(salgrade)
    * GRADE    NUMBER
    * LOSAL    NUMBER
    * HISAL    NUMBER
6. 对单个列进行设置 `col ename for a10;`    

## 第三节课:sql简单查询
### 知识点
1. 简单查询基本操作格式
2. 别名的设置
3. 在简单查询之中实现四则运算和字符串的连接显示

### 具体内容
1. select [distinct] * 列名称[别名],列名称[别名],... from 表名称[别名];
2. ||可以将两个列的内容合并为一个列

## 第四节 :限定查询
### 知识点
1. 掌握where子句的使用频率
2. 掌握各种限定查询符号的使用

### 具体步骤
1. 确定数据来源:from 表名称[别名]
2. 确定满足条件的数据行:where 过滤条件
3. 控制要显示的数据列:select[distinct] * |列名称[别名]

### 具体内容
1. 关系运算符:>,<,>=,<=;
2. 逻辑运算符:and,or,not;
3. 范围元素符:between,and;
4. 谓词范围:in,not in;
5. 空判断:is null,is not null;
6. 模糊查询:like;

## 第五节:排序查询
### 知识点
1. 排序的使用
2. 多个字句的关系

### 具体内容
1. 确定数据来源:from 表名称[别名]
2. 确定满足条件的数据行:where 过滤条件
3. 控制要显示的数据列:select[distinct] * |列名称[别名]
4. 针对查询结果进行排序[order by 字段 [asc(升序)|desc(降序)]]
5. order by可以调用别名

## 第六节:综合练习
### 目标
巩固学习过的四个子句:select,from,where,order by.

### 练习
1. 选择部门30中的所有员工:`select * from emp where deptno=30`
2. 列出所有办事员(CLERK)的姓名,编号和部门编号:`select ename,empno,deptno from emp where job='CLERK'`
3. 找出佣金高于薪金60%的员工:`select * from emp where COMM>SAL*0.6 ` 
4. 找出部门10中所有经理(MANAGER)和部门20中所有办事员(CLERK)的详细资料:`select * from emp where (deptno=10 and job='MANAGER') or (deptno=20 and job='CLERK')`
5. 找出部门10中所有经理(MANAGER),部门20中所有的办事员(CLERK),既不是经理又不是办事员但其薪金大于或等于2000的所有员工详细资料:`select * from emp where (deptno=10 and job='MANAGER') or (deptno=20 and job='CLERK') or (job not in ('MANAGER','CLERK') and sal>2000)`
6. 找出收取佣金的员工的不同工作:`select job from emp where comm is not null`
7. 找出不收取佣金或收取佣金低于100的员工:`select * from emp where comm is null or comm<100`
8. 显示不带R的员工的姓名:`select ename from emp where not ENAME like '%R%';`
9. 显示姓名字段的任何位置包含'A'的所有员工姓名,显示的结果按照基本工资由高到低排序,工资相同则按照雇佣年限由早到晚排序,如果雇佣日期相同则按照职位排序:`select * from empwhere ename like '%A%' order by sal desc ,HIREDATE,job desc`

### 总结
1. 清楚学习过每一个字句的作用:select.from.where.order by
2. 多个条件判断的时候一定要使用逻辑连接,尽量使用()做一个区分
3. 遇到问题慢慢分析,别着急









