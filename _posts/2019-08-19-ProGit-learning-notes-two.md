---
layout: post
title:  "Pro Git 学习笔记2"
date:   2019-08-19
categories: Git
tags: Git note 
---

* content
{:toc}

第二章








<!-- ![燕十八](http://7q5cdt.com1.z0.glb.clouddn.com/teach-girlfriend-html-18swallows.png) -->
# Pro Git 学习笔记

## 二.Git基础

### 2.1 取得项目的Git仓库

#### 在工作目录中初始化新仓库
`git init`:初始化后，当前目录下会出现一个名为 .git 的目录，所有 Git 需要的数据和资源都存放在这个目录中。但我们还没有开始跟踪管理项目中的任何一个文件。  
如果当前目录下有几个文件想要纳入版本控制，需要先用`git add`命令告诉 Git 开始对这些文件进行跟踪,然后提交`git commit`

#### 从现有仓库克隆
克隆仓库的命令格式为`git clone [url]`。比如，要克隆Ruby 语言的Git代码仓库Grit，可以用下面的命令：
1. http协议方式
```
git clone https://github.com/用户名/用户名.github.io
```
2. ssh协议方式
```
git clone git://github.com/schacon/grit.git
```

### 2.2 记录每次更新到仓库

1. `git status`:检查文件当前状态
2. `git diff`:查看具体修改了什么地方
3. `git diff --staged`:看已经暂存起来的文件和上次提交时的快照之间的差异
4. `git add`:可以用它开始跟踪新文件，或者把已跟踪的文件放到暂存区，还能用于合并时把有冲突的文件标记为已解决状态等
5. `git commit -a`:Git会自动把所有已经跟踪过的文件暂存起来一起提交
6. `git rm`:要从Git中移除某个文件，就必须要从已跟踪文件清单中移除,可以用`git rm`命令完成此项工作，并连带从工作目录中删除指定的文件
* 我们想把文件从Git仓库中删除（亦即从暂存区域移除），但仍然希望保留在当前工作目录中。换句话说，仅是从跟踪清单中删除。比如一些大型日志文件或者一堆`.a`编译文件，不小心纳入仓库后，要移除跟踪但不删除文件，以便稍后在`.gitignore`文件中补上，用`--cached`选项即可：
```
git rm --cached readme.txt
```
* 后面可以列出文件或者目录的名字，也可以使用glob 模式。  
比方说：
```
git rm log/\*.log
```
此命令删除所有`log/`目录下扩展名为`.log`的文件
* 会递归删除当前目录及其子目录中所有`~`结尾的文件
```
git rm \*~
```
7. 一般我们总会有些文件无需纳入 Git 的管理，也不希望它们总出现在未跟踪文件列表。我们可以创建一个名为`.gitignore`的文件，列出要忽略的文件模式。
```
*.[oa]
*~
```
第一行告诉 Git 忽略所有以`.o`或`.a`结尾的文件。一般这类对象文件和存档文件都是编译过程中出现的，我们用不着跟踪它们的版本。第二行告诉 Git 忽略所有以波浪符（`~`）结尾的文件，许多文本编辑软件（比如 Emacs）都用这样的文件名保存副本。    
文件`.gitignore`的格式规范如下：
* 所有空行或者以注释符号`＃`开头的行都会被 Git 忽略。
* 可以使用标准的`glob`模式匹配。
* 匹配模式最后跟反斜杠（`/`）说明要忽略的是目录。
* 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号（`!`）取反。
8. `mv 旧文件名字 新文件名字`:修改文件名称

### 2.3 查看提交历史

1. `git log`:回顾提交历史  
2. `git log -p -2`:`-p`选项展开每次提交的内容差异，`-2`则仅显示最近两次更新，`-- pretty`可以指定使用完全不同于默认格式的方式展示提交历史，`oneline`将每个提交放在一行显示，另外还有`short`，`full`和`fuller`可以用，请自己手动实践以下
3. `format`:可以定制要显示的目录:
```
git log --pretty=format:"%h - %an, %ar : %s"
    ca82a6d - Scott Chacon, 11 months ago : changed the version number
    085bb3b - Scott Chacon, 11 months ago : removed unnecessary test code
    a11bef0 - Scott Chacon, 11 months ago : first commit
```
```
选项 说明
%H 提交对象（commit）的完整哈希字串
%T 树对象（tree）的完整哈希字串
%t 树对象的简短哈希字串
%P 父对象（parent）的完整哈希字串
%p 父对象的简短哈希字串
%an 作者（author）的名字
%ae 作者的电子邮件地址
%ad 作者修订日期（可以用 -date= 选项定制格式）
%ar 作者修订日期，按多久以前的方式显示
%cn 提交者(committer)的名字
%ce 提交者的电子邮件地址
%cd 提交日期
%cr 提交日期，按多久以前的方式显示
%s 提交说明
```
4. 另一个真正实用的`git log`选项是路径(path)，如果只关心某些文件或者目录的历史提交，可以在`git log`选项的最后指定它们的路径。因为是放在最后位置上的选项，所以用两个短划线（--）隔开之前的选项和后面限定的路径名。
```
选项 说明
    -p 按补丁格式显示每个更新之间的差异。
    --stat 显示每次更新的文件修改统计信息。
    --shortstat 只显示 --stat 中最后的行数修改添加移除统计。
    --name-only 仅在提交信息后显示已修改的文件清单。
    --name-status 显示新增、修改、删除的文件清单。
    --abbrev-commit 仅显示 SHA-1 的前几个字符，而非所有的 40 个字符。
    --relative-date 使用较短的相对时间显示（比如，“2 weeks ago”）。
    --graph 显示 ASCII 图形表示的分支合并历史。
    --pretty 使用其他格式显示历史提交信息。可用的选项包括 oneline，short，full，fuller 和 format（后跟指定格式）。
    -(n) 仅显示最近的 n 条提交
    --since, --after 仅显示指定时间之后的提交。
    --until, --before 仅显示指定时间之前的提交。
    --author 仅显示指定作者相关的提交。
    --committer 仅显示指定提交者相关的提交。
```
示例：如果要查看 Git 仓库中，2008 年 10 月期间，Junio Hamano 提交的但未合并的测试脚本（位于项目的 t/ 目录下的文件），可以用下面的查询命令  
`git log --pretty="%h - %s" --author=gitster --since="2008-10-01" \
    --before="2008-11-01" --no-merges -- t/`

5. 使用图形化工具查阅提交历史

### 2.4 撤销操作
1. `git commit --amend`:修改最后一次提交
2. 如果刚才提交时忘了暂存某些修改，可以先补上暂存操作，然后再运行`--amend`提交：
```
git commit -m 'initial commit'
    git add 忘记的文件
    git commit --amend
```
3. `git reset HEAD 文件名`:取消已经暂存的文件，不用死记硬背，输入`git status`的命令会提示。
4. `git checkout --文件名`:取消对文件的修改，不用死记硬背，输入`git status`的命令会提示。
5. 记住，任何已经提交到Git的都可以被恢复。即便在已经删除的分支中的提交，或者用`--amend`重新改写的提交，都可以被恢复。所以，你可能失去的数据，仅限于没有提交过的，对Git来说它们就像从未存在过一样。

### 2.5 远程仓库的使用
1. 查看当前的远程仓库：`git remote`，也可以加上-v，显示对应的克隆地址
2. 添加远程仓库：运行`git remote add [remote-name] url`
3. 从远程仓库抓取数据：`git fetch [remote-name]`
4. 推送数据到远程仓库：项目进行到一个阶段，要同别人分享目前的成果，可以将本地仓库中的数据推送到远程仓库。实现这个任务的命令很简单： `git push [remote-name] 分支名字`。只有在所克隆的服务器上有写权限，或者同一时刻没有其他人在推数据，这条命令才会如期完成任务。如果在你推数据前，已经有其他人推送了若干更新，那你的推送操作就会被驳回。你必须先把他们的更新抓取到本地，合并到自己的项目中，然后才可以再次推送。
5. 查看远程仓库信息：我们可以通过命令`git remote show [remote-name]`查看某个远程仓库的详细信息 
6. 远程仓库的删除和重命名：在新版Git中可以用`git remote rename`命令修改某个远程仓库在本地的简称，比如想把`pb`改成`paul`，可以这么运行：`git remote rename pb paul`，移除远端仓库，可以运行`git remote rm`命令：`git remote rm paul`

### 2.6 打标签
1. 列显已有的标签：`git tag`
2. 含附注的标签：创建一个含附注类型的标签非常简单，用`-a`。而`-m`选项则指定了对应的标签说明，Git会将此说明一同保存在标签对象中。如果没有给出该选项，Git会启动文本编辑软件供你输入标签说明。可以使用`git show`命令查看相应标签的版本信息，并连同显示打标签时的提交对象。`git tag -a v1.4 -m 'my version 1.4'`
3. 签署标签：如果你有自己的私钥，还可以用GPG来签署标签，只需要把之前的`-a`改为`-s`
4. 轻量级标签：实际上就是一个保存着对应提交对象的校验和信息的文件。要创建这样的标签,直接给出标签名字即可`git tag v1.4-lw`
5. 验证标签：可以使用`git tag -v [tag-name]`的方式验证已经签署的标签。此命令会调用GPG来验证签名，所以你需要有签署者的公钥，存放在keyring中，才能验证
6. 后期加注标签：我们忘了在提交 “updated rakefile” 后为此项目打上版本号v1.2，没关系，现在也能做。只要在打标签的时候跟上对应提交对象的校验和（或前几位字符）即可：`git tag -a v1.2 9fceb02`
7. 分享标签：默认情况下，`git push`并不会把标签传送到远端服务器上，只有通过显式命令才能分享标签到远端仓库。其命令格式如同推送分支，运行`git push origin [tagname]`。如果要一次推送所有本地新增的标签上去，可以使用`--tags`选项:`git push origin --tags`

### 2.7 技巧和窍门
1. 自动补全：下载 Git 的源代码，进入`contrib/completion`目录，会看到一个`git-completion.bash`文件。将此文件复制到你自己的用户主目录中（译注：按照下面的示例，还应改名加上点：`cp git-completion.bash ~/.git-completion.bash）`，并把下面一行内容添加到你的`.bashrc`文件中：`source ~/.git-completion.bash`。Linux 上则复制到`/etc/bash_completion.d/`目录中。
2. Git命令别名：Git并不会推断你输入的几个字符将会是哪条命令，不过如果想偷懒，少敲几个命令的字符，可以用`git config`为命令设置别名。来看看下面的例子：
```
$ git config --global alias.co checkout
    $ git config --global alias.br branch
    $ git config --global alias.ci commit
    $ git config --global alias.st status
```
现在，如果要输入`git commit`只需键入`git ci`即可。而随着Git使用的深入，会有很多经常要用到的命令，遇到这种情况，不妨建个别名提高效率。



### 2.8 小结
你已经学会了最基本的 Git 本地操作：创建和克隆仓库，做出修改，暂存并提交这些修改，以及查看所有历史修改记录。


























