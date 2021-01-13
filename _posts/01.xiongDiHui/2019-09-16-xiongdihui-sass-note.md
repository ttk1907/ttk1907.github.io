---
layout: post
title:  "Sass学习笔记"
date:   2019-09-16
categories: Sass
tags: Sass note
---

* content
{:toc}

Sass学习笔记









# Sass学习笔记
## sass
1. 文件分为：头部，内容，尾部，名字前要加`_`，style.sass
```
@import "header";
```

2. 定义一个变量，创建一个sass文件用来定义变量
```
_variable.sass
```

3. 嵌套
在一个css属性里可以继续嵌套选择他的子元素进行设置

4. 混入 
跟function类似，在sass中定义一个mixin
```
@mixin transform(参数$a){
    transform:$a;
}
```
调用的时候需要引入一下`@include transform(属性值);`

5. 继承
首先定义一个父类，然后在想要用的地方继承
```
定义父类：
%subtitle-font-size{
    font-size:16px;
    line-height:16px;
}
继承：
@extend %subtitle-font-size;
```

## 使用sass
1. 首先安装sass插件`Live Sass Compiler`
2. 在功能栏打开`live sass:watch sass`
3. 在配置中修改css生成的路径
4. 编辑scss

















