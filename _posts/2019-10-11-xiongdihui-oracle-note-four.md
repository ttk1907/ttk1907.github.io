---
layout: post
title:  "Oracle基础学习笔记4"
date:   2019-10-11
categories: Oracle
tags: Oracle note
---

* content
{:toc}

Oracle基础学习笔记4








# Oracle基础学习笔记4

## 第一节课:子查询
### 知识点
1. 子查询的各个使用形式
2. 分析子查询的主要意义

### 具体内容
实际上对于这个SQL语法而言,所有的组成就是几个固定的查询语句,而所谓的子查询指的就是在一个查询里面继续嵌套其他的查询语句,如果非要给个语法,在每一步都可添加子查询
1. where子句:子查询一般会返回单行单列.单行多列.多行单列数据
	1. where子句的作用是进行数据行的筛选操作的.
	2. 查询出低于公司平均工资的雇员信息
	3. any:与in的作用相同.>any就是比any的最小值大,`<any就是比any最大的值要小`
	4. all:>all就是比all的最大值要大,`<all就是比all最小值要小`

```
select * 
from emp 
where 
sal<(
	select avg(sal)
	from emp
 	);

```
	
2. having子句:子查询会返回单行单列,同时表示要使用统计函数
3. from子句:子查询返回多行多列数据(表结构)
	1. 查询每个部门名称、位置、部门人数 

```
统计出部门编号.名称.位置
select d.dname,d.deptno,d.loc
from dept d
统计出每个部门的编号.人数
select e.deptno,count(empno)
from emp e
group by deptno
以上的两个数据发现可以在部门编号上找到联系
select d.dname,d.loc,t.count
from dept d,(
	select e.deptno,count(empno) count
	from emp e
	group by deptno) t
where d.deptno=t.deptno(+)
```	

4. select子句:返回单行单列,一般不使用(强烈不建议)
5. 多表查询可以实现统计,子查询也能实现统计,那种方式好呢?为了更好的解释这个问题,假设将数据表中的数据扩大100倍,即:此时假设emp表有1400条记录,而dept表有400条记录
	1. 使用多表查询及分组统计:
		* emp表的1400条 x dept表的400条=560000条记录
	2. 使用子查询:
		* 子查询的数据量:只使用emp的1400条记录,最多返回400行
		* 子查询的返回数据量400条 x dept表的400条=160000条数据
		* 两个操作加在一起最多只操作160400条
	3. 在实际工作中,子查询的主要目的使解决多表查询所带来的性能问题

### 总结
1. 复杂查询=简单查询+限定查询+多表查询+分组统计查询+子查询
2. 如果是子查询,首先考虑的一定是where和from子句里面出现子查询的操作,而having只有在适用统计函数的时候才会使用
3. 在实际工作中,子查询的主要目的使解决多表查询所带来的性能问题

## 第二节课:复杂查询
### 练习题
1. 列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称、部门人数

```
部门30最高的薪金
select max(sal)
from emp
where deptno=30

部门人数和部门编号
select e.deptno,count(empno)
from emp e
group by deptno

最终
select e.ename,e.sal,d.dname,t.count
from emp e,dept d,(
	select e.deptno,count(empno) count
	from emp e
	group by deptno) t
where e.sal>(
	select max(sal)
	from emp
	where deptno=30) and e.deptno=d.deptno and e.deptno=t.deptno
```

2. 列出与"SCOTT"从事相同工作的所有员工及部门名称,部门人数,领导姓名

```
需要emp统计员工,需要dept统计部门名称,emp统计领导姓名,emp统计部门人数

1.找到scott这个人的工作
select job 
from emp
where ename='SCOTT'

2.统计与"SCOTT"从事相同工作的所有员工
select *
from emp
where job=(
	select job 
	from emp
	where ename='SCOTT')

3.将第二步的表与部门表结合,加上部门名称
select e.ename,d.dname
from emp e,dept d
where job=(
	select job 
	from emp
	where ename='SCOTT') and e.deptno=d.deptno

4.通过emp表统计部门人数
select deptno,count(empno)
from emp
group by deptno

5.将部门人数加到第三步的表
select e.ename,d.dname,t.count
from emp e,dept d,(
	select deptno,count(empno) count
	from emp
	group by deptno) t
where job=(
	select job 
	from emp
	where ename='SCOTT') and e.deptno=d.deptno and t.deptno=e.deptno

6.统计领导姓名	
select a.ename,e.ename 领导姓名
from emp e,(
	select e.ename,e.mgr
	from emp e) a
where a.mgr=e.empno

7.将领导姓名加入第五步
select e.ename,d.dname,t.count,m.ename
from emp e,dept d,(
	select deptno,count(empno) count
	from emp
	group by deptno) t,emp m
where e.job=(
	select job
	from emp
	where ename='SCOTT') 
	and e.deptno=d.deptno 
	and t.deptno=e.deptno 
	and e.mgr=m.empno 
	and e.ename!='SCOTT'
```

3. 列出薪金比'SMITH'或'ALLEN'多的所有的员工的编号、姓名、部门名称、其领导姓名,部门人数,平均工资,最高及最低工资

```
select e.empno,e.ename,d.dname,m.ename leader,a.count,a.avg,a.max,a.min
from emp e,dept d,emp m,(
	select deptno,count(empno) count,avg(sal) avg,max(sal) max,min(sal) min
	from emp
	group by deptno) a
where e.sal>any(
	select sal
	from emp
	where ename in ('SMITH','ALLEN'))
	and d.deptno=e.deptno
	and e.mgr=m.empno(+)
	and e.deptno=a.deptno
union
select avg(sal),max(sal),min(sal)
from emp
```

## 第三节课:增加数据
1. 数据增加:insert into 表名称[(列名称)] values(值1,值2)
但是在增加数据的时候,有如下声明:
	* 字符串:使用""声明,;例如:'mldn';
	* 数字:直接编写,例如:100;
	* 日期:当前日期(sysdate)、使用to_date()转换,按照日期格式编写字符串
2. 例1:进行数据的增加
	* insert into myemp(empno,sal,job,comm,ename,mgr,hirdate,deptno) values(8888,9000.0,'清洁工',10.0,'张三',7369,to_date('1979-10-10','yyyy-mm-dd'),40);

## 第四节课:修改数据
1. update 表名称 set 字段1=值1,字段2=值2,...[更新条件(s)];
2. 在使用更新的时候,where子句里可以使用in,between and
3. 例子:update myemp set sal=8000,comm=9000 where ename='smith'

## 第五节课:删除数据
1. delect from 表名称 [where 删除条件(s)]

## 第六节课:事务处理
### 具体内容
1. 如果假设要执行转账的业务操作,今天江同学要转账给付同学1000万:
	* 第一步:从江同学的账户减少1000万;
	* 第二步:在付同学的账户上增加1000万;
	* 第三步:随后江同学要支付50元的转账费用
2. 如果说现在执行到第二步的时候出现了错误,也就是说付同学没有收到1000万,第一步不应该执行,所有数据应该恢复到原始状态.这样的操作需要执行三条更新操作,并且属于同一个操作业务,为了保证这三个更新操作要么同时完成,要么同时失败,就可以使用事务这一概念进行处理.
3. 事务是针对与数据更新使用的,也就是说只有DML的更新操作才存在有事务的支持
4. session(会话,以后只要是此概念都表示唯一的一个登录用户),在oracle之中每一个登录到数据库中的用户,都会动态非配一个session,即:每一个session都表示不同地用户,而每一个session上都拥有独立的事务的操作,而每一个session上的事务处理都可以使用两个命令:
	* commit:提交,即,如果已经执行了多条更新操作,那么只有执行了commit之后更新才会真正发出,没执行commit之前,所有的更新操作,都会保存在缓冲区之中
	* rollback:事务回滚操作,即:如果发现更新的操作有问题,则恢复所有的更新操作,以保证原始的数据不被破坏

### 认识死锁
1. 每一个session都有自己独立的事务处理,那么现在sessionA与sessionB更新了同一个数据会如何?
2. 由于此时第一个session先发出的更新指令,并且没有进行任何的事务处理操作(commit,rollback),第二个session会一直等待一个个session更新后再发出我们的更新

### 总结
1. 只有更新操作才会存在事物处理,DDL不支持事务处理,而且在Oracle里面,如果发生了DDL操作,会产生严重的问题:所有未提交的更新事务会被自动提交;
2. 两个重要的事务操作命令:commit,rollback

## 数据伪列
1. rownum(行号)
2. 例子:查询emp表的第一行记录:select * from emp where rownum=1(只有第一行好使)
3. 取出前n行的记录:select * from emp where rownum<=5
4. 取出6到10行的记录:先取出10行,去掉前五行

```
select * 
from (
	select empno,ename,job,sal,hiredate,rownum rn
	from emp
	where rownum<=10) temp
where temp.rn>5
```
这种操作就是oracle中实现分页的核心操作

## 约束条件
1. 非空约束:not null
2. 唯一约束:不能有重复的数据添加,不包括null,一般起名时为`UK_列名`,代码是`constraint UK_email unique(email)`
3. 主键约束:非空约束和主键约束的集合体,既不能为空,也不能重复,代码是`constraint pk_mid primarykey(mid)`
4. 外键约束(fk):就是控制子表中某一个列的内容与父表中的数据范围相配匹,使用foreign key来表示,代码是`constraint fk_mid foreign key(mid) references 父表(mid)`
	* 限制一:如果表中存在有外键关系,再删除父表前一定要先删除子表
	* 限制二:父表中作为子表关联的外键字段,必须设置为主键约束或者唯一约束
	* 限制三:默认情况下,如果父表记录中有对应的子表记录,那么父表记录无法被删除







