---
layout: post
title:  "Java核心类库第七天"
date:   2019-10-31
categories: Java
tags: Java note
---

* content
{:toc}

1. 核心类库第9天：常用的设计原则、常用的设计模式、常用的查找算法、冒泡排序算法









# Java核心类库第七天
## Java深入篇--核心类库--第9天
### 常用的设计原则(记住)
1. 软件开发的流程
    1. 需求分析文档 => 概要设计文档 => 详细设计文档 => 编码和测试 => 安装和调试=> 维护和升级
2. 常用的设计原则
    1. 开闭原则 
        1. 对扩展开放，对修改关闭。
        2. 提高了代码的扩展性和维护性。
    ```java
如：
   public class Person {
      private String name;
      private int age;
      ...
   }
   public class SubPerson extends Person {
      private boolean gender;
      ... 
   }
    ```

    2. 里氏代换原则
        1. 任何父类可以出现的地方，子类一定可以出现。
        2. 子类 is a 父类。
        3. 在以后的开发中多使用继承和多态的理念。
    ```java
如：
   public static void draw(Shape s){
       s.show();
   }
   ShapeTest.draw(new Rect(1, 2, 3, 4));
   ShapeTest.draw(new Circle(5, 6, 7));
    ```

    3. 依赖倒转原则
        1. 尽量多依赖于抽象类和接口，而不是具体实现类。
        2. 在以后的开发中多使用抽象类和接口，对子类具有强制性和规范性
    ```java
如：
public abstract class Account {
       public abstract double getLixi();
   } 
   public class FixedAccount extends Account {
       @Override
       public double getLixi(){}
   }
    ```

    4. 接口隔离原则 
        1. 尽量依赖于小接口而不是大接口，避免接口的污染。
        2. 可以降低耦合度。
        3. 耦合主要指一个模块与其它模块之间的关联度
    ```java
如：
   public interface RunAnimal {
       public abstract void run(); // 描述奔跑的行为
   }
   public interface FlyAnimal {
       public abstract void fly(); // 描述飞行的行为
   }
   public class Dog implements RunAnimal {
       public void run(){ ... }
   }
    ```

    5. 迪米特法则(最少知道原则)
        1. 一个实体应当尽量少于其它实体之间发生相互作用。
        2. 低耦合，高内聚
        3. 高内聚就是指将一个实体应当将该实体应该拥有的功能尽量聚集在该实体内部
    6. 合成复用原则
        1. 尽量多使用合成的方式，而不是继承的方式。
    ```java
如：
   public class A {
       public void show() { ... }
       ... ...
   }
   //public class B extends A{  不推荐
   public class B {
       private A a;
       public void test() {
           // 调用show方法
           a.show();
       }
   }
    ```

### 常用的设计模式
1. 基本概念
    1. 设计模式就是一种用于固定场合的固定套路，是多年编程经验的总结。
2. 常用的设计模式
    1. 单例设计模式
    2. 模板设计模式
    3. 工厂方法模式(在扩展的时候违背开闭原则)
        1. 创建接口
        2. 实现产品接口(每个产品实现一个Sender接口)
        3. 在SenderFactory(工厂类)中创建每个产品的静态方法
        4. 直接类名点方法-创建对象
    4. 抽象工厂模式(与工厂方法模式相比在扩展的时候不用违背开闭原则)
        1. 创建provider接口
        2. 创建两个工厂类实现接口
        3. 在每个工厂类中创建方法返回对象

### 常用的查找算法(重中之重)
1. 线性/顺序查找算法
    1. 使用目标元素与样本列中的第一个元素起依次比较
    2. 若找到与目标元素相等的元素，则表示查找成功
    3. 若目标元素与所有样本元素比较完毕也不相等，则表示查找失败
2. 二分/折半查找算法
    1. 假定样本数列中的元素是从小到大依次排序的;
    2. 使用目标元素与样本数列中的中间元素进行比较;
    3. 若目标元素与中间元素相等,则表示查找成功;
    4. 若目标元素小于中间元素，则去中间元素的左边进行查找;
    5. 若目标元素大于中间元素，则去中间元素的右边进行查找;
    6. 直到目标元素与所有该比较的元素比较完毕后也不相等，则表示查找失败

### 冒泡排序算法(重中之重)
1. 比较相邻位置的两个元素，若第一个元素比第二个元素大则交换
2. 从开始的第一对元素一直到结尾的最后一对元素，经过这一轮找到了最大值并放在了最后
3. 持续对越来越少的元素进行两两比较，直到所有元素不再发生交换位置














