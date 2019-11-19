---
layout: post
title:  "JS学习笔记4"
date:   2019-09-06
categories: JS
tags: JS note
---

* content
{:toc}

JS学习笔记4






# JS实例：放大镜
## 1.参考淘宝京东商品页
## 2.css部分
1. 边框样式：
    * margin：外边框
    * border：边框
    * padding：内边框
    * content：内容
2. 定位样式：
    * position：relative相对定位
    * position：absolute绝对定位
3. 零碎样式：
    * cursor:move 鼠标样式
    * overflow: hidden 超出边框内容隐藏
    * .bimg>img：寻找.bimg下一级的img元素
    * list-style: none 将样式清空

## 3.JS部分
1. ready()定义和用法：
    * 语法：`$(document).ready(function)`
    * 当 DOM（文档对象模型） 已经加载，并且页面（包括图像）已经完全呈现时，会发生 ready 事件。

2. hover()定义和用法：
    * 语法：`$(selector).hover(inFunction,outFunction)`
    * hover()方法规定当鼠标指针悬停在被选元素上时要运行的两个函数。方法触发 `mouseenter` 和 `mouseleave` 事件。

3. mousemove()定义和用法：
    * 语法：` $(selector).mousemove(function)`
    * 当鼠标指针在指定的元素中移动时，就会发生 mousemove 事件.mousemove() 方法触发 mousemove 事件，或添加当发生 mousemove 事件时运行的函数。
    * 实例：获得鼠标指针在页面中的位置
    ```
    $(document).mousemove(function(event){
    $("span").text(event.pageX + ", " + event.pageY);
    });
    ```

4. offset()定义和用法：
    * offset() 方法:`$(selector).offset()` 设置或返回被选元素相对于文档的偏移坐标。
    * 当用于返回偏移时：`$(selector).offset({top:value,left:value})`该方法返回第一个匹配元素的偏移坐标。它返回一个带有两个属性（以像素为单位的 top 和 left 位置）的对象。
    






















