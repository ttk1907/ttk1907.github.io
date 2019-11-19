---
layout: post
title:  "JS小知识2"
date:   2019-09-12
categories: JS
tags: JS
---

* content
{:toc}

1. 更改选择框属性、时间、jquery方法










# JS小知识
## 更改选择框属性
```
for (var i = 0; i <=$('input').length-1 ; i++) {
            var b = $('input').eq(i).prop('checked',false);
            console.log(b);
        }
```
这是一个让所有框全不选的属性

## 时间
```
var mydate = new Date();

mydate.getYear(); //获取当前年份(2位)

mydate.getFullYear(); //获取完整的年份(4位,1970-????)

mydate.getMonth(); //获取当前月份(0-11,0代表1月)

mydate.getDate(); //获取当前日(1-31)

mydate.getDay(); //获取当前星期X(0-6,0代表星期天)

mydate.getTime(); //获取当前时间(从1970.1.1开始的毫秒数)

mydate.getHours(); //获取当前小时数(0-23)

mydate.getMinutes(); //获取当前分钟数(0-59)

mydate.getSeconds(); //获取当前秒数(0-59)

mydate.getMilliseconds(); //获取当前毫秒数(0-999)

mydate.toLocaleDateString(); //获取当前日期

var mytime=mydate.toLocaleTimeString(); //获取当前时间

mydate.toLocaleString( ); //获取日期与时间
```

## jquery方法
1. last()：选择最后一个元素
2. fadeTo(0,0)：使用淡出效果来隐藏一个元素，第一个数是速度，第二个数是透明度
3. hide()：隐藏元素
4. prependTo(父)：在每个父元素的子元素开头插入内容
5. slideDown(1000)：slideDown() 方法通过使用滑动效果，显示隐藏的被选元素。参数是速度










