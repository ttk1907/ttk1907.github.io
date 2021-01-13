---
layout: post
title:  "Java核心类库第五天"
date:   2019-10-29
categories: Java
tags: Java note
---

* content
{:toc}

1. 核心类库第7天：线程









# Java核心类库第五天
## Java深入篇--核心类库--第7天
### 线程
1. 基本概念
    1. 程序 - 数据结构 + 算法，主要指存放在硬盘上的可执行文件。
    2. 进程 - 主要指运行在内存中的程序。
    3. 目前主流的操作系统都支持多进程，为了使得操作系统能够同时执行多个任务，但进程是重量级的，新建进程对系统的资源消耗比较大，因此进程的数量比较局限。线程是进程内部的程序流，也就是操作系统中支持多进程，而每个进程的内部又可以支持多线程，线程是轻量级的，新建线程会共享所在进程的系统资源，因此以后的开发中都采用多线程技术。多线程技术采用时间片轮转法实现并发执行，所谓并发就是指宏观并行微观串行。
2. 线程的创建(重中之重)
    1. 创建和启动的方式：java.lang.Thread类用于描述线程，Java 虚拟机允许应用程序并发地运行多个执行线程，而线程的创建和启动方式如下：
        1. 自定义类继承Thread类并重写run方法，创建该类的实例调用start方法。
        2. 自定义类实现Runnable接口并重写run方法，创建该类的实例作为实参来构造 
        3. 注意：线程创建和启动的方式一相对来说代码简单，但Java语言中只支持单继承，若该类继承Thread类后则无法继承其它类；而方式二相对来说代码复杂，但不影响该类继承其它类以及实现其它接口，因此以后开发中推荐方式二。
    2. 相关方法的解析
        1. Thread() - 使用无参方式构造对象。
        2. Thread(String name) - 根据参数指定的名称来构造对象。
        3. Thread(Runnable target) - 根据参数指定的接口引用来构造对象。
        4. Thread(Runnable target, String name) - 根据参数指定的引用和名称构造对象。
        5. void run() - 若使用Runnable类型的引用构造出来的对象调用该方法，则最终调用引用所指向对象的run方法，否则调用该方法啥也不做。
        6. void start() - 用于启动线程，Java虚拟机会自动调用该线程的run方法。
    3. 常用方法
        1. static void yield()：当前线程让出处理器(离开Running状态)，使当前线程进入Runnable状态等待
        2. static void sleep(times)：使当前线程从Running放弃处理器进入Block状态，休眠times毫秒，再返回到Runnable如果其他线程打断当前线程的Block(sleep)，就会发生InterruptedException
        3. int getPriority()：用于获取线程的优先级
        4. void setPriority(int)：更改线程的优先级
        5. void join()：等待该线程终止
        6. void join(long millis)：表示等待参数指定的毫秒数
        7. boolean isDaemon()：用于判断是否为守护线程
        8. void setDaemon(boolean on)：用于设置线程为守护线程
    4. 原理分析
        1. 执行main方法的线程叫做主线程，执行run方法的线程叫做子线程。
        2. main方法是程序的入口，最开始只有主线程来依次执行main方法中的代码，当start方法调用成功后，线程的个数瞬间由1个变成了2个，其中子线程去执行run方法，主线程继续执行main方法的代码，两个线程各自独立运行互不影响。
        3. 当run方法执行完毕后子线程结束，当main方法执行完毕后主线程结束，但两个线程谁先执行没有明确的规定，取决于操作系统的调度算法。
3. 线程的编号和名称
    1. 相关方法：
        1. long getId()：用于获取调用对象所表示线程的编号
        2. String getName()：用于获取调用对象所表示线程的名称
        3. void setName(String name)：用于设置线程的名称为参数制定的数值
        4. static Thread currentThread()：获取当前正在执行线程的引用

























