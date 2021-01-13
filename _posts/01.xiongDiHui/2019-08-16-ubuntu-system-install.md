---
layout: post
title:  "ubuntu系统的安装"
date:   2019-08-16 22:14:54
categories: System problem
tags:  ubuntu
---

* content
{:toc}

ubuntu系统安装。







# 安装开始

## 一.做启动盘

​ 去官网下载镜像，找一个空的u盘，用工具做成启动盘。

## 二.开机进入BIOS界面

​ 关闭安全模式，security boot 选dis，选择u盘启动。

## 三.安装时一直点继续，安装成功

### 问题1.卡在登陆界面动不了

​解决方法：这是由于忘记禁用独立显卡造成的，开机时按esc进入选择界面，在*install ubuntu 或者*ubuntu 按e进入编辑模式，在`quiet slash --` 后面添加以下内容，`acpi_osi=linux nomodeset `然后按ctrl+x或者f10保存。修改上述选项时可以在开机的时候，禁用nouveau显卡。保存后进入桌面，这时由于没有安装显卡驱动，桌面分辨率较低，所以重点是，马上安装显卡驱动。因为如果不安装显卡驱动，在你重启之后，你会发现你将会遇到第二个问题。

### 问题2.在登陆界面无限循环，只有nvidia显卡可用解决方法

​解决方法：这就是由于没有及时安装显卡驱动造成的后果，下面我们来安装nvidia显卡驱动，共有三个方法。

1. 首先查看硬件型号，在终端输入：`ubuntu-drivers devices `可以看到自己显卡的型号，然后安装推荐版本的驱动。在终端输入：`sudo ubuntu-drivers autoinstall `这样就可以自动安装了，如果显示软件包没有依赖的话，在终端输入：
```
sudo dpkg --add-architecture i386
​sudo apt update
​sudo apt install build-essential libc6:i386
```
这是一些nvidia的依赖软件，然后重复第一步自动安装就可以了

2. 添加PPA第三方软件仓库安装最新版本，首先添加PPA软件仓库:`sudo add-apt-repository ppa:graphics-drivers/ppa`,需要输入用户密码，按提示按下Enter健。更新软件索引：`sudo apt update`,接下来的步骤同方法1

3. 第三种方法是从nvidia官网下载最新版驱动手动安装，但是我并不会。
