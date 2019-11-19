---
layout: post
title:  "redis基础学习笔记2"
date:   2019-10-15
categories: Redis
tags: Redis note
---

* content
{:toc}

redis基础学习笔记2









# redis基础学习笔记2
## 常用命令
1. 返回键：`keys *` 
2. 存储键值对：`set name zhangsan`
3. 获取值：`get name`
4. 检测键是否存在，有返回1，没有返回0：`exists 键名`
5. 删除键值对：`del 键名 `
6. 设置键存在时常为十秒：`expire 键名 10`
7. 查看键的过期时间，若为-2表示已过期,-1表示永不过期：`ttl 键名`
8. 将键名age的转移到1数据库：`move age 1`
9. 切换数据库：`select 1`，默认有15个数据库，0-15
10. 移除键名过期时间：`persist age`
11. 删除所有数据：`flushdb`
12. 清空所有数据：`flushall `

# 直接看课件吧













