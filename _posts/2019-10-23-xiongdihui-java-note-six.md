---
layout: post
title:  "Java核心类库第一天"
date:   2019-10-23
categories: Java
tags: Java note
---

* content
{:toc}

1. 核心类库第1天：Object类、包装类和数学处理类










# Java核心类库第一天
## Java深入篇--核心类库--第1天
### Object类
1. 常用的包
    1. java.lang包：该包是Java语言中的核心包，该包中的内容由Java虚拟机自动导入，如：String类、System类等
    2. java.util包：该包是Java语言中的工具包，里面包含了大量的工具类和集合类等，如：Scanner、Random类等
    3. java.io包：该包是Java语言中的输入输出包，里面包含了大量的读写文件的类等，如：FileOutputStream、FileInputStream类等
    4. java.net包：该包是Java语言中的网络包，里面包含了大量网络编程的类等，如：ServerSocket类、Socket类等
2. Object类
    1. 基本概念：java.lang.Object类是所有类层次结构的根类，任何类都是该类的直接或间接子类。
    2. 常用方法
        1. Object() -- 使用无参方式构造对象。
        2. boolean equals(Object obj)
            1. 用于判断调用对象是否与参数对象相等。该方法默认比较两个对象的地址，与==运算符结果相同。
            2. 为了使得该方法比较两个对象的内容，则需要重写该方法。
            3. 若该方法重写后，则应该重写hashCode方法来维护hashCode方法的常规协定
        3. int hashcode() 
            1. 用于获取调用对象的哈希码值(内存地址的编号)
            2. 若调用equals方法的结果相等，则各自调用hashCode方法的结果相同
            3. 若调用equals方法的结果不相等，则各自调用hashCode方法的结果不相同
            4. 为了维护上述的常规协定与equals方法结果保持一致，就需要重写该方法
        4. String toString()
            1. 用于获取对象的字符串形式
            2. 该方法返回的字符串为：包名.类名@哈希码值的十六进制形式
            3. 为了返回更有意义的数据，需要重写该方法
            4. 当字符串与引用进行连接时，自动调用toString方法
            5. 当使用print或println方法打印引用时，自动调用toString方法

### 包装类和数学处理类(会用即可)
1. 包装类的概念：由于Java语言是一门纯粹的面向对象编程语言，而8种基本数据类型声明的变量并不是对象，为了满足Java语言的特性就需要对这些变量进行对象化处理，而实现该功能的相关类就叫做包装类
2. 包装类的分类
    1. int => java.lang.Integer
    2. char => java.lang.Character
    3. 其他基本类型就是将首字母大写
3. Integer类(包装类)
    1. 基本概念：java.lang.Integer类是int类型的包装类，里面包含了一个int类型的成员变量。该类由final关键字修饰表示不能被继承。
    2. 常用方法
        1. Integer(int value) -- 根据参数指定的整数构造对象
        2. Integer(String s) -- 根据参数指定的字符串构造对象
        3. 该类重写了equals()、hashCode()、toString()方法
        4. int intValue() -- 用于获取调用对象中的整数数据并返回
        5. static Integer valueOf(int i) -- 根据参数指定的整数返回对应的Integer对象
        6. static int parseInt(String s) -- 用于将String类型转换成int类型并返回
        7. 从jdk1.5开始可以自动装箱，自动拆箱
        ```java
Integer it = 100;
res = it;
        ```

4. BigDecimal类(数学处理类)
    1. 基本概念：由于float类型和double类型的运算可能会有误差，为了实现精确运算则需要借助java.math.BigDecimal类型加以描述
    2. 常用的方法
        1. BigDecimal(String val) -- 根据参数指定的字符串构造对象。
        2. BigDecimal add(BigDecimal augend) -- 用于计算调用对象和参数对象的差并返回
        3. BigDecimal multiply(BigDecimal multiplicand) -- 用于计算调用对象和参数对象的积并返回
        4. BigDecimal divide(BigDecimal divisor) -- 用于计算调用对象和参数对象的商并返回
5. String类(重中之重)
    1. 基本概念：java.lang.String类用于描述字符串，Java应用程序中所有字符串字面值都可以作为String类型的对象加以描述，如："abc"等。
    2. 该类描述的字符串内容是个常量，一旦创建完毕后则不能更改，因此可以被共享
    3. 常用方法
        1. String():无参构造
        2. String(Arr,1,3):表示使用Arr数组中下标从1开始的3个字节来构造字符串对象
        3. String("World"):表示使用字符串构造对象
6. 常量池(原理、尽量理解)
    1. 由于String类型描述的字符串内容是个常量不可改变，因此Java虚拟机提供一个常量池，当Java程序中出现字符串内容时就放入常量池中，若后续出现重复的字符串内容则直接使用池中已有的对象而不许再次创建，从而提高了性能













