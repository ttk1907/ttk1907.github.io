---
layout: post
title:  "HTML/CSS学习笔记"
date:   2019-08-30
categories: HTML
tags: note HTML
---

* content
{:toc}

HTML/CSS学习笔记









# HTML/CSS学习笔记
## HTML
1. div标签：分节，使html页面更有可读性
2. a标签：添加跳转链接，锚
3. form标签：向数据库中传输数据
4. ul里li标签：定义无序列表，多用于导航栏
5. p标签：定义一个段落
6. select标签：定义一个下拉列表

## CSS标签
### 引入CSS
1. 引入css,行间样式：直接在`div`标签中的`style`里写
2. 引入css,页面标签：在`head`中直接写`style`标签，在里面修改css
3. 引入css,外部css文件：在`head`中添加`link`标签，在`link`标签里写`css`文件地址

### CSS选择器
1. id选择：`id='abc'`，css中应该写`#abc{}`，这样就选择上了,`id`只能一对一
2. class选择：`class=demo`，css中应该写`.demo{}`，这样就选择上了，`class`可以多对多
3. 标签选择器：想选什么直接写上标签就行，对所有这个标签都进行修改，比如`div{}`
4. 统配符选择器：一个`*`号就完事，但凡是标签就被选中，例如`*{}`
5. css权重问题：`!important`>`行间样式`>`id`>`class`>`标签选择器`>`统配符选择器`
6. 复杂选择器：父子选择器、伪类选择器：例如`hover`:鼠标移上之后添加css样式

### 元素
1. 行级元素
feature：内容决定元素所占位置，不可以通过css改变宽高  
例如： `span标签`和`strong标签`以及`a标签`等等

2. 块级元素
feature：独占一行，可以通过css改变宽高
例如： `div标签`和`p标签`以及`ul标签`和`form标签`

3. 行级块元素
feature：内容决定大小，可以改宽高
例如：`img标签`

## 盒子模型
1. 外边距 margin
2. 盒子壁 border
3. 内边距 padding
4. 盒子内容 width+height
![盒子模型](/assets/hezi.png)







