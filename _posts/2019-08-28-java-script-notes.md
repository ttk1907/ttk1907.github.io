---
layout: post
title:  "JS学习笔记1"
date:   2019-08-28
categories: JS
tags: JS note
---

* content
{:toc}

JS学习笔记
1. 这几天的任务是学习js和node.js





# JavaScript
## 1.JS历史
在上个世纪的1995年，当时的网景公司正凭借其Navigator浏览器成为Web时代开启时最著名的第一代互联网公司。  
由于网景公司希望能在静态HTML页面上添加一些动态效果，于是叫Brendan Eich这哥们在两周之内设计出了JavaScript语言。你没看错，这哥们只用了10天时间。

## 2.JS快速入门
1. JavaScript代码可以直接嵌在网页的任何地方，不过通常我们都把JavaScript代码放到`<head>`中:  
由`<script>...</script>`包含的代码就是JavaScript代码，它将直接被浏览器执行

2. 第二种方法是把JavaScript代码放到一个单独的.js文件，然后在HTML中通过`<script src="..."></script>`引入这个文件：  
这样，`/static/js/abc.js`就会被浏览器执行。  
把JavaScript代码放入一个单独的.js文件中更利于维护代码，并且多个页面可以各自引用同一份.js文件。  
可以在同一个页面中引入多个.js文件，还可以在页面中多次编写`<script> js代码... </script>`，浏览器按照顺序依次执行。

3. 可以在控制台(console)调试JS代码

## 3.语法
JavaScript的语法和Java语言类似，每个语句以`;`结束，语句块用`{...}`,以`//`开头直到行末的字符被视为行注释,另一种块注释是用`/*...*/`把多行字符包裹起来，把一大“块”视为一个注释

## 4.数据类型和变量
1. JS里比较相等多用`===`,`&&`是与运算,`||`是或运算,`!`是非运算
2. null和undefined:JavaScript的设计者希望用`null`表示一个空的值，而`undefined`表示值未定义。事实证明，这并没有什么卵用，区分两者的意义不大。大多数情况下，我们都应该用`null`。`undefined`仅仅在判断函数参数是否传递的情况下有用。
3. 对象:JavaScript的对象是一组由键-值组成的无序集合:
```
var person = {
    name: 'Bob',
    age: 20,
    tags: ['js', 'web', 'mobile'],
    city: 'Beijing',
    hasCar: true,
    zipcode: null
};
```
JavaScript对象的键都是字符串类型，值可以是任意数据类型。上述`person`对象一共定义了6个键值对，其中每个键又称为对象的属性，例如，`person的name`属性为`'Bob'`，`zipcode`属性为`null`。  
要获取一个对象的属性，我们用`对象变量.属性名`的方式：
```
person.name; // 'Bob'
person.zipcode; // null
```
4. 变量:和python变量命名差不多，只多了一个`$`符号：
```
var a; // 申明了变量a，此时a的值为undefined
var $b = 1; // 申明了变量$b，同时给$b赋值，此时$b的值为1
var s_007 = '007'; // s_007是一个字符串
var Answer = true; // Answer是一个布尔值true
var t = null; // t的值是null
```
要显示变量的内容，可以用`console.log(x)`
5. strict模式：在同一个页面的不同的JavaScript文件中，如果都不用var申明，恰好都使用了变量`i`，将造成变量`i`互相影响，产生难以调试的错误结果。在strict模式下运行的JavaScript代码，强制通过var申明变量，未使用var申明变量就使用的，将导致运行错误。  
启用strict模式的方法是在JavaScript代码的第一行写上：`'use strict';`

## 5.字符串
1. 多行字符串：由于多行字符串用\n写起来比较费事，所以最新的ES6标准新增了一种多行字符串的表示方法，用反引号`*... *`表示
```
`这是一个
多行
字符串`;
```
2. 模板字符串:如果有很多变量需要连接，用+号就比较麻烦。ES6新增了一种模板字符串，表示方法和上面的多行字符串一样，但是它会自动替换字符串中的变量
```
var name = '小明';
var age = 20;
var message = `你好, ${name}, 你今年${age}岁了!`;
alert(message);
```
3. 操作字符串
```
var s = 'Hello, world!';
s.length; // 13
```
需要特别注意的是，字符串是不可变的，如果对字符串的某个索引赋值，不会有任何错误，但是，也没有任何效果  
JavaScript为字符串提供了一些常用方法，注意，调用这些方法本身不会改变原有字符串的内容，而是返回一个新字符串  
* toUpperCase():把一个字符串全部变为大写
* toLowerCase():把一个字符串全部变为小写
* indexOf():会搜索指定字符串出现的位置
* substring():返回指定索引区间的子串

## 6.数组
* slice():它截取`Array`的部分元素，然后返回一个新的`Array`
* push和pop:`push()`向`Array`的末尾添加若干元素，`pop()`则把`Array`的最后一个元素删除掉
* unshift和shift:如果要往`Array`的头部添加若干元素，使用`unshift()`方法，`shift()`方法则把`Array`的第一个元素删掉
* sort():可以对当前`Array`进行排序，它会直接修改当前`Array`的元素位置，直接调用时，按照默认顺序排序
* reverse():把整个`Array`的元素给掉个个，也就是反转
* splice():方法是修改`Array`的“万能方法”，它可以从指定的索引开始删除若干元素，然后再从该位置添加若干元素
* concat():把当前的`Array`和另一个`Array`连接起来，并返回一个新的`Array`
* join():一个非常实用的方法，它把当前`Array`的每个元素都用指定的字符串连接起来，然后返回连接后的字符串

## 7. 对象
JavaScript的对象是一种无序的集合数据类型，它由若干键值对组成。  
JavaScript的对象用于描述现实世界中的某个对象。例如，为了描述“小明”这个淘气的小朋友，我们可以用若干键值对来描述他：
```
var xiaoming = {
    name: '小明',
    birth: 1990,
    school: 'No.1 Middle School',
    height: 1.70,
    weight: 65,
    score: null
};
```
上述对象申明了一个`name`属性，值是`'小明'`，`birth`属性，值是`1990`，以及其他一些属性。最后，把这个对象赋值给变量`xiaoming`后，就可以通过变量`xiaoming`来获取小明的属性了
```
xiaoming.name; // '小明'
xiaoming.birth; // 1990
```
访问属性是通过`.`操作符完成的，但这要求属性名必须是一个有效的变量名。如果属性名包含特殊字符，就必须用`''`括起来  
由于JavaScript的对象是动态类型，你可以自由地给一个对象添加或删除属性
```
var xiaoming = {
    name: '小明'
};
xiaoming.age; // undefined
xiaoming.age = 18; // 新增一个age属性
xiaoming.age; // 18
delete xiaoming.age; // 删除age属性
xiaoming.age; // undefined
delete xiaoming['name']; // 删除name属性
xiaoming.name; // undefined
delete xiaoming.school; // 删除一个不存在的school属性也不会报错
```















































