---
layout: post
title:  "Java核心类库第二天"
date:   2019-10-24
categories: Java
tags: Java note
---

* content
{:toc}

1. 核心类库第2天：String类的常用方法、StringBuilder类和StringBuffer类、日期相关的类
2. 多态的三种使用场合










# Java核心类库第二天
## Java深入篇--核心类库--第2天
### String类的常用方法(重中之重、练熟、记住)
1. charAt(int i)：获取下标为i的字符，返回char字符
2. length()：获取字符串的长度
3. boolean contains(CharSequences)：用于判断当前字符串是否包含参数指定的内容
4. String toLowerCase()：返回字符串的小写形式
5. String toUpperCase()：返回字符串的大写形式
6. String trim()：返回去掉前导和后继空白的字符串
7. boolean startsWith(String prefix)：判断字符串是否以参数字符串开头
8. boolean endsWith(String suffix)：判断字符串是否以参数字符串结尾
9. str.indexOf():从指定字符串查找第一次遇到的字符串返回下标
10. str.substring(5,10):表示从下标5(包括)取到10(不包括)并返回

```java
面试题：使用两种方法实现将字符串"12345"转换为整数12345并打印

方式一:使用Interger类中的parseInt方法进行转换即可
String str2 = new String("12345");
int ia = Interger.parseInt(str2);

方式二:取出字符串中的每个字符并转换为整数数据再合并起来
'1'-48 => 1  '2'-48 =>2  
'1'-'0'=>1   '2'-'0' =>2  '3'-'0'=>3
int res = 0;
for (int i = 0; i<str2.length() ;i++){
    res = res*10 + (str2.charAt(i)-'0');
}
```

### StringBuilder类和StringBuffer类(重点)
1. 基本概念：由于String类型描述的字符串内容是个常量不可更改，当程序出现大量类似的字符串时需要单独存放从而浪费内存空间，若希望使用一块内存空间进行存储并且可以修改字符串内容，则应该使用StringBuilder类和StringBuffer类
2. 其中StringBuffer类从jdk1.0开始存在，该类支持线程安全，因此访问的效率比较低
3. 其中StringBuilder类从jdk1.5开始存在，该类不支持线程安全，访问的效率比较高
4. 常用方法

```java
1.public StringBuffer append(String s)
将指定的字符串追加到此字符序列。

2.public StringBuffer reverse()
将此字符序列用其反转形式取代。

3.public delete(int start, int end)
移除此序列的子字符串中的字符。

4.public insert(int offset, int i)
将 int 参数的字符串表示形式插入此序列中。

5.replace(int start, int end, String str)
使用给定 String 中的字符替换此序列的子字符串中的字符。
```

### 日期相关的类(查手册会用即可)
1. Date类：java.util.Date类用于描述特定的瞬间，可以精确到毫秒
    1. Date d1 = new Date();--使用无参的方式构造对象并打印
    2. Date d2 = new Date(1000);--使用参数指定的毫秒数来构造对象并打印
    3. long msc= d1.getTime();--调用成员方法，用于获取调用对象d1表示的时间距离标准时间的毫秒数
    4. d1.setTime(2000);--设置调用对象表示的时间为距离标准时间2秒的时间点
2. SimpleDateFormat类：java.text.SimpleDateFormat类主要用于实现日期和文本之间的相互转换
    1. format(Date类型)：实现Date类型向String类型的转换并打印
    2. parse(String类型)：实现String类型向Date类型的转换并打印
3. Calendar类：java.util.Calendar类用于取代Date类来描述年月日时分秒的特定瞬间
    1. 调用静态方法得到Calendar类型的引用：Calendar c1 = Calendar.getInstance();
    2. 调用set方法设置年月日时分秒：c1.set(2008,8-1,8,20,8,8);
    3. 调用getTime方法将Calendar类型转换为Date类型：Date d2 = c1.getTime();
    4. 调整格式并打印format(d2)

### 思考题
1. 既然Calendar是个抽象类，那么getInstance方法如何得到该类引用呢？
2. 答：返回Calendar类型子类的对象从而形成了多态，多态的第三种使用场合

### 多态的三种使用场合
1. 通过方法的传参形成多态
2. 直接在方法体里面直接用引用指向子类对象
3. 通过方法的返回值类型形成多态





















