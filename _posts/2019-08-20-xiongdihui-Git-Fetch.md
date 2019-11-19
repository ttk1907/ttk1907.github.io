---
layout: post
title:  "Fetch用法"
date:   2019-08-20
categories: Git
tags: Git
---

* content
{:toc}

1. 解决ssh密钥没了的问题
2. fetch用法








# Git
## 1.ssh密钥没了解决方法
直接重新生成一个

## 2.fetch用法
fetch方法同步：现在已经落后版本了，要同步远程仓库
先用fetch把远程仓库的更新都拿过来放到tmp分支中：git fetch [远程仓库] [想要弄来的分支]:tmp  
git diff tmp可以查看当前分支和tmp进行对比，可以看出修改了什么  
切换到tmp，然后推他：git push -u origin tmp:tmp  
切回去master分支：合并master和tmp：git merge origin/tmp  
这就同步完成，修改后推master:git push -u origin master


