---
layout: post
title:  "配置SSH"
date:   2019-08-19
categories: Git
tags: Git
---

* content
{:toc}

1. 设置ssh协议
2. 添加远程仓库








# Git操作
## 1.设置ssh协议

第一步：`ssh-keygen -t rsa -C "ttk1907@163.com"`获取ssh key，然后按三次enter

第二步：`cat ~/.ssh/id_rsa.pub`，打开这个文件，复制ssh key

第三步：克隆`git clone git@github.com:ttk1907/ttk1907.github.io.git`，用ssh协议重新克隆库。

## 2.添加远程仓库
`git remote add [自己起得名字] [原作者项目地址]`





