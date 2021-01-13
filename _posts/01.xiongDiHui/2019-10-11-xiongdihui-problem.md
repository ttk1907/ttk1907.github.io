---
layout: post
title:  "数据库使用过程中的小问题"
date:   2019-10-11
categories: problem
tags: oracle
---

* content
{:toc}

监听服务开启不了









# 监听服务开启不了
### 问题
本地计算机上的OracleOraDb11g_home1TNSListener服务启动后停止。某些服务在未由其他服务或程序使用时将自动停止

### 解决方法
1. 找到listener.ora文件(在app文件夹下搜索)
2. 在终端查看自己IP地址
	* window命令为:ipconfig
	* linux命令为:ifconfig
3. 将listener.ora中的IP地址换成正在使用的IP地址重启服务即可










