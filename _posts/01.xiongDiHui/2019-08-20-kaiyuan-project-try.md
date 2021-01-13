---
layout: post
title:  "开源项目参加流程"
date:   2019-08-20
categories: Git
tags: Git
---

* content
{:toc}

合作完成开源项目









<!-- ![燕十八](http://7q5cdt.com1.z0.glb.clouddn.com/teach-girlfriend-html-18swallows.png) -->

## 一.首先需要在github上注册账号并登陆

## 二.安装git，到github官网下载安装包。
ubuntu系统直接在终端中输入`sudo git-apt install git`安装git

## 三.为github账号添加ssh key
clone项目到本地不需要身份认证，但要push修改到github上需要身份验证。push修改时走ssh协议，所以这里需要将我们的公钥添加到github账号中。这里就是ssh实现无密码登陆，或者所谓的公钥登陆，就是采用了私钥确定唯一身份的原理。

1. 生成密钥对。运行终端执行以下命令：
```
ssh-keygen -t rsa -C "邮箱"
```
一直按enter，直至显示这个画面
![最终画面](/assets/ssh密钥.png)

2. `cat ~/.ssh/id_rsa.pub`查看密钥
3. 在github上添加密钥，这里添加的是`id_rsa.pub`里面的公钥
4. 添加私密钥到ssh：`ssh-add ~/.ssh/id_rsa`，用于验证唯一身份

## 四.fork你想参加的项目
1. 浏览git上的开源项目，然后点击fork，这时就跳到你的账号下，此项目就是你账号下的项目了。
2. fork就相当于把别人的项目克隆到自己的账号下一份，以后你的修改都应该是提交到你自己的github账号的这个项目中，你是没有权限直接push到原作者账号下的项目中的。

## 五.clone项目到本地
1. 复制项目clone地址
注意是clone自己账号下的项目地址，不是原作者的，原作者的你虽然也可以clone到本地，但是你是没push权限的。还要注意这里咱们使用ssh协议，所以要选择ssh类型的地址
2. clone到本地，在命令行输入`git clone 复制的地址`，然后执行，然后就可以进入项目目录了。

## 六.将项目原地址添加为远程仓库
复制原作者的项目地址，添加为自己的一个远程仓库，用来实时将原项目的修改更新到咱们本地并合并。注意也是复制ssh协议类型的地址哦
1. 添加远程仓库：`git remote add upstream 原作者项目地址`
2. 使用`git remote -v`可以看到我们有两个仓库一个origin，咱们自己的github仓库；一个upstream，原作者的远程仓库。当然也可以不用upstream这个名字

## 七.创建branch，用于添加自己的修改
这只是一个约定成俗的方式，当然你也可以在master上添加修改，创建新的branch添加自己的修改的好处是，你可以同时添加多个修改，在一个修改还没有被原作者merge时，你可以用master创建新的branch继续你的其它修改。
1. 在这里我们在新添加的分支上修改：执行如下命令
```
git branch test  //创建你test分支
git checkout test//切换到test分支
或者这样：
git checkout -b test
```
然后就可以添加我们的修改了

## 八.同步远程仓库
因为是合作开发项目，这时远程仓库中的内容有可能已经发生了变化，所以我们需要将远程仓库中的内容和本地分支中的内容进行合并  
方法1. pull方式是直接把远程仓库的主干和分支全合在一起拉过来，相当于fetch+merge
```
git pull [远程仓库名称] [分支名称]
```
方法2. git fetch 相当于是从远程获取最新到本地，不会自动merge，如下指令：
```
git fetch [远程仓库名称] [想要弄来的分支]:tmp //将远程仓库master分支获取最新，在本地建立tmp分支，将最新的远程仓库存入tmp分支
git diff tmp //将当前分支和tmp进行对比，可以看出修改了什么
如果你新建分支用来修改，那就切到用来修改的分支，合并tmp，然后修改提交，如果你用master直接修改，直接用master合并tmp再修改，
git merge origin/tmp //合并tmp分支到当前分支
```

## 九.将修改push到我们的github上
由于我们的github上还没有test分支，所以我们得把命令写全了：`git push origin test:test`

## 十.pull request
1. 你的修改已经push到了你的github下了，但是你要向原作者请求合并到原项目中，如果原作者合并了，也就意味着你是此项目的贡献者了。
2. 到你的github上点击如下按钮
![pull request](/assets/拉取请求.png)
3. 当然你也可以选择test分支，，然后点击项目右边的创建一个pull request。提交完pull request，原作者就会看到你的合并请求，采不采纳就是他的事了






