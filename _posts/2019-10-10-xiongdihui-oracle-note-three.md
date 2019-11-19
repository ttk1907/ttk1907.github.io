---
layout: post
title:  "Oracle基础学习笔记3"
date:   2019-10-10
categories: Oracle
tags: Oracle note
---

* content
{:toc}

Oracle基础学习笔记3








# Oracle基础学习笔记3

## 第一节课:统计函数
### 知识点
1. 基础统计函数的使用
2. 分组统计操作的实现,结合多表查询使用分组统计

### 具体内容
1. 统计个数:count(* 字段 [distinct])
2. 最大值:max(字段)
3. 最小值:min(字段)
4. 总和:sum(数字字段)
5. 平均:avg(数字字段)

## 第二节课:分组统计
1. group by 分组字段
    * 限制一:在没有编写group by子句的时候,相当于全表分组,那么select子句之中只允许出现统计函数,不允许出现任何的其他字段
    * 限制二:在使用group by子句分组时,select只允许出现分组字段和统计函数,不允许出现其他字段
    * 限制三:统计函数允许被嵌套使用,但是嵌套后的统计查询中,select子句里面不允许出现任何字段,包括分组字段,只允许出现统计函数
2. 总结
    1. 在整个分组里面一定要注意,只有在基数固定的时候才可能分组
    2. 不管是单表分组还是多表分组,重点先看重复的列,如果是一个重复列,就在group by写一个,如果是多个重复的列,就写多个
    3. 多表查询与分组统计的时候,查询结果相当于一张临时表,所有的分组是在临时表里完成的

### 小练习
1. 查询每个部门的名称.人数.平均工资
```
select dname,count(empno),avg(sal)
from emp e,dept d
where e.deptno(+)=d.deptno
group by dname;
```

2. 查询出每个部门编号.名称.位置.部门人数.平均服务年限
```
select e.deptno,dname,loc,count(empno),avg(months_between(sysdate,HIREDATE)/12) 平均年限
from emp e,dept d 
where e.deptno(+)=d.deptno
group by e.deptno,dname,loc
```

3. 要求查询出平均工资高于2000的职位名称以及平均工资
```
select job,avg(sal)
from emp
group by job
having avg(sal)>2000
```
having用于对分组后的数据进行筛选

## sql查询语句最终结构
5. 确定要使用的数据列:`SELECT [DISTINCT] 分组字段[别名] 统计函数`
1. 确定要查找的数据来源:`FROM`
2. 针对于数据行进行筛选:`WHERE 过滤条件(S)`
3. 针对于数据实现分组:`GROUP BY 分组字段` 
4. 针对于分组后的数据进行筛选:`HHAVING 分组后的过滤条件`
6. 针对于返回结果进行排序:`ORDER BY 字段[ASC/DESC]`

## where与having的区别
1. where发生在group操作之前,属于分组前数据筛选,即:从所有的数据中筛选出可以分组的数据,where子句不允许使用统计函数;
2. having发生在group by 操作之后,是针对于分组后的数据进行筛选,having子句可以使用统计函数;

## 综合练习
1. 显示非销售人员工作名称以及从事同一工作雇员的月工资总和,并且要满足从事同一工作的雇员的月工资合计大于5000,输出结果按月工资的合计升序排列
```
select job,sum(sal)
from emp
where job!='SALESMAN'
group by job
having sum(sal)>5000
order by sum(sal) 
```

2. 统计公司所有领取佣金与不领取佣金的雇员人数.平均工资
```
select '不领取佣金' title,count(empno),avg(sal)
from emp
where comm is null
union
select '领取佣金' title,count(empno),avg(sal)
from emp
where comm is not null
```








