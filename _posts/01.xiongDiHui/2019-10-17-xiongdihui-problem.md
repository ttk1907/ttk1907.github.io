---
layout: post
title:  "将记事本默认编码设为UTF-8的方法"
date:   2019-10-17
categories: problem
tags: txt
---

* content
{:toc}

将记事本默认编码设为UTF-8的方法









# 将记事本默认编码设为UTF-8的方法
### 问题
新建文本文件然后改成.java文件时，由于记事本的编码方式默认为ANSI，导致用sublime等编译器编写完成后，在终端运行java文件会出现乱码。

### 目标
将记事本默认编码改成utf8

### 解决方法
1. 打开记事本新建一个空白的文本文档，不输入任何文字，然后保存此文档，在“另存为”对话框中将编码由默认的 ANSI 修改为 Unicode 或 UTF-8，接着为文件取名，在此假设将新文档命名为`UTF8.txt`。
2. 将 UTF8.txt 复制至隐含的系统文件夹,没有的话就自己创建`C:\Windows\ShellNew`。
3. 打开注册表编辑器定位至：`HKEY_CLASSES_ROOT\.txt\ShellNew`，新建名为 FileName 的字符串值，将此字符串值设置为`UTF8.txt`。










