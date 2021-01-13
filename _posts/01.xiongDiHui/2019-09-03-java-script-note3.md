---
layout: post
title:  "JS学习笔记3"
date:   2019-09-03
categories: JS
tags: JS note
---

* content
{:toc}

JS学习笔记3






# JavaScript
## 1. JS对象
1. 在 JavaScript 中，对象是王。如果您理解了对象，就理解了 JavaScript。  
在 JavaScript 中，几乎“所有事物”都是对象：
    * 布尔是对象（如果用 new 关键词定义）
    * 数字是对象（如果用 new 关键词定义）
    * 字符串是对象（如果用 new 关键词定义）
    * 日期永远都是对象
    * 算术永远都是对象
    * 正则表达式永远都是对象
    * 数组永远都是对象
    * 函数永远都是对象
    * 对象永远都是对象

2. 创建 JavaScript 对象
通过 JavaScript，您能够定义和创建自己的对象，有不同的方法来创建对象：
    * 定义和创建单个对象，使用对象文字。
    * 定义和创建单个对象，通过关键词 new。
    * 定义对象构造器，然后创建构造类型的对象。

3. 对象的增删改查
新建一个对象：
```
var person = {
    age:60,
    firstName:'Bill',
    lastName:'Gates',
    eyeColor:'blue'
};
```
    * 增：person.nationality = "English";
    * 删：delete person.lastName;
    * 改：person.age = 50 //直接改就行
    * 查：person.age

## 2. JS事件
1. HTML事件
    * HTML 网页完成加载
    * HTML 输入字段被修改
    * HTML 按钮被点击
改变id为demo的元素的值
```
<button onclick='document.getElementById("demo").innerHTML=Date()'>现在的时间是？</button>
```
改变自身的值
```
<button onclick="this.innerHTML=Date()">现在的时间是？</button>
```
2. 常见的事件
    * onchange：   HTML 元素已被改变
    * onclick： 用户点击了 HTML 元素
    * onmouseover： 用户把鼠标移动到 HTML 元素上
    * onmouseout： 用户把鼠标移开 HTML 元素
    * onkeydown：  用户按下键盘按键
    * onload： 浏览器已经完成页面加载

## 3.字符串
* length： 属性返回字符串的长度
* indexOf()： 方法返回字符串中指定文本首次出现的索引（位置）
* lastIndexOf()： 方法返回指定文本在字符串中最后一次出现的索引
* search()： 方法搜索特定值的字符串，并返回匹配的位置
    + 这两种方法是不相等的。区别在于：
    + `search()` 方法无法设置第二个开始位置参数。
    + `indexOf()` 方法无法设置更强大的搜索值（正则表达式）。
* slice()：方法 提取字符串的某个部分并在新字符串中返回被提取的部分，该方法设置两个参数：起始索引（开始位置），终止索引（结束位置）。
* substring()：方法`substring()` 类似于 `slice()`，不同之处在于 `substring()` 无法接受负的索引。
* replace()：方法用另一个值替换在字符串中指定的值
* toUpperCase()：把字符串转换为大写
* toLowerCase()：把字符串转换为小写
* concat()：连接两个或多个字符串
* trim()：方法删除字符串两端的空白符

## 4.this 是什么？
avaScript this 关键词指的是它所属的对象。

它拥有不同的值，具体取决于它的使用位置：

* 在方法中，`this` 指的是所有者对象。
* 单独的情况下，`this` 指的是全局对象。
* 在函数中，`this` 指的是全局对象。
* 在函数中，严格模式下，`this` 是 undefined。
* 在事件中，`this` 指的是接收事件的元素。

## 5.JavaScript HTML DOM
1. 什么是 HTML DOM？
HTML DOM 是 HTML 的标准对象模型和编程接口。它定义了：
    * 作为对象的 HTML 元素
    * 所有 HTML 元素的属性
    * 访问所有 HTML 元素的方法
    * 所有 HTML 元素的事件
换言之：HTML DOM 是关于如何获取、更改、添加或删除 HTML 元素的标准。

2. HTML DOM（文档对象模型）  
当网页被加载时，浏览器会创建页面的文档对象模型（Document Object Model）。

HTML DOM 模型被结构化为对象树：

对象的 HTML DOM 树
![对象的 HTML DOM 树](https://www.w3school.com.cn/i/ct_htmltree.gif)

3. 通过这个对象模型，JavaScript 获得创建动态 HTML 的所有力量：
    * JavaScript 能改变页面中的所有 HTML 元素
    * JavaScript 能改变页面中的所有 HTML 属性
    * JavaScript 能改变页面中的所有 CSS 样式
    * JavaScript 能删除已有的 HTML 元素和属性
    * JavaScript 能添加新的 HTML 元素和属性
    * JavaScript 能对页面中所有已有的 HTML 事件作出反应
    * JavaScript 能在页面中创建新的 HTML 事件

## 6.JavaScript - HTML DOM 方法
1. HTML DOM 方法是您能够（在 HTML 元素上）执行的动作。
2. HTML DOM 属性是您能够设置或改变的 HTML 元素的值。
3. getElementById 方法:通过id来查找元素
4. innerHTML 属性：
    * 获取元素内容最简单的方法是使用 innerHTML 属性。  
    * innerHTML 属性可用于获取或替换 HTML 元素的内容。
    * innerHTML 属性可用于获取或改变任何 HTML 元素，包括 `<html>` 和 `<body>`

## 7.JavaScript HTML DOM 元素
1. 查找 HTML 元素
    * 通过 id 查找 HTML 元素
    * 通过标签名查找 HTML 元素
    * 通过类名查找 HTML 元素
    * 通过 CSS 选择器查找 HTML 元素
    * 通过 HTML 对象集合查找 HTML 元素
2. 通过 CSS 选择器查找 HTML 元素
如果您需要查找匹配指定 CSS 选择器（id、类名、类型、属性、属性值等等）的所有 HTML 元素，请使用 `querySelectorAll()` 方法。

本例返回 class="intro" 的所有 `<p>` 元素列表：
```
var x = document.querySelectorAll("p.intro");
```
## 8.JavaScript HTML DOM - 改变 CSS
```
document.getElementById(id).style.property = new style
```




































