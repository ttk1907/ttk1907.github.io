---
layout: post
title:  "Redis基础学习笔记1"
date:   2019-10-14
categories: Redis
tags: Redis note
---

* content
{:toc}

redis基础学习笔记1









# NOSQL
## NOSQL是什么
1. NOSQL:Not Only SQL 泛指非关系性数据库 

## 为什么需要NOSQL
1. High performance - 高并发读写
2. Huge Storage - 海量数据库的高效率存储和访问
3. High Scalability && High Availability - 高可扩展性和高可用新性

## NOSQL数据库的四大分类
1. 键值对(Key-Value)存储：Redis 内容缓存，主要用于处理大量数据的高访问负载
2. 列存储:HBase 分布式的文件系统
3. 文档数据库:MongoDB Web应用(与Key-Value类似，Value是结构化的)
4. 图形数据库:InFoGrid 社交网络，推荐系统等，专注于构建关系图谱

## NOSQL特点
1. 易扩展
2. 灵活的数据模型
3. 大数据量，高性能
4. 高可用

## Redis概述
1. 高性能键值对数据库，支持的键值数据类型
    * 字符串类型
    * 列表类型
    * 有序集合类型
    * 散列类型
    * 集合类型

2. Redis应用场景
    * 缓存
    * 任务队列
    * 网站访问统计
    * 数据过期统计
    * 应用排行榜
    * 分布式集群架构中的session分离




















