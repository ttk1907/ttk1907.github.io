---
layout: post
title:  "关于SublimeText3输入法候选窗口不能跟随光标位置的解决方案"
date:   2019-10-16
categories: problem
tags: sublime
---

* content
{:toc}

sublime小瑕疵




## sublime小瑕疵
今天使用sublime时，遇到SublimeText3默认不支持输入法跟随光标，特别不方便。

进入`SublimeText3`在上面菜单栏里`Perferences`点击`PackageControl`，这样就会自动安装一个可支持插件的终端窗口。

安装完毕之后，按快捷键`ctrl+shift+p`会弹出终端窗口，输入`install package`（下方会有提示）。

然后输入`imesupport`安装这个插件，安装完毕后，重启`Sublime`就可以了。

<div class="htmledit_views" id="content_views">
                                            <p>我们使用Sublime时有个Bug就是输入文字时，输入法的框不会跟随光标。</p>

<p><img alt="" class="has" height="55" src="https://img-blog.csdnimg.cn/20190220142828949.png" width="633"></p>

<p>我们需要手动添加一个包 就能解决这个问题</p>

第一步: 下载`IMESupport`插件

<p><strong>Github传送门</strong>：<a href="https://github.com/zcodes/IMESupport" rel="nofollow" data-token="0dce66f1378bbdf8a96f5c646cf34dce">https://github.com/zcodes/IMESupport</a>&nbsp;</p>

<p>如果你是用下载，下载后解压，注意双层文件夹的问题（两个同名文件夹，去掉外面的一个）。</p>

第二步: 放到package包下，这里必须手动添加依赖，不然不会生效

<p><img alt="" class="has" height="99" src="https://img-blog.csdnimg.cn/20190220143321812.png" width="765"></p>

<p><img alt="" class="has" height="228" src="https://img-blog.csdnimg.cn/20190220143347979.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0MTMxMzk5,size_16,color_FFFFFF,t_70" width="739"></p>

<p>图中第一个是用package control安装的 没用。</p>                                    </div>