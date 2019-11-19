---
layout: post
title:  "兄弟会个人分享第一次"
date:   2019-08-19
categories: share
tags: share
---

* content
{:toc}

兄弟会个人分享第一次








<!-- ![燕十八](http://7q5cdt.com1.z0.glb.clouddn.com/teach-girlfriend-html-18swallows.png) -->
# 兄弟会个人分享第一次
## 1.回退版本
问题：上传更改结果博客没有更改
1. 时刻保持数据完整性,所有保存在 Git 数据库中的东西都是用哈希值来作索引的，而不是靠文件名。哈希值看起来就像是：
```
24b9da6552252987aa493b52f8696cd6d3b00373
```
执行，回退到某个版本的命令
```
git reset --hard 24b9da6552252987aa493b52f8696cd6d3b00373
```
强制提交到master分支（具体需要提交到哪个分支自行修改）
```
git push -f -u origin master
```
2. 进入github，提交，进入犯错之前的版本，浏览文件，直接下载。

## 跳过使用暂存区域
尽管使用暂存区域的方式可以精心准备要提交的细节，但有时候这么做略显繁琐。Git 提供了一个跳过使用暂存区域的方式，只要在提交的时候，给 git commit 加上 -a 选项，Git 就会自动把所有已经跟踪过的文件暂存起来一并提交，从而跳过 git add 步骤：

## 2.添加特效
1. 鼠标吸附线条效果：
    * 去百度查找吸附效果的代码，加入到footer文件夹中
2. 网易云音乐：
    * 去网易云音乐网站找代码，在指定的地方插入

## 3.小技巧
一些边边角角的小技巧，[小明博客](https://victorfengming.github.io/)
























