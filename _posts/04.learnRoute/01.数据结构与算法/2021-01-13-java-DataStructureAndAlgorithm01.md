---
layout: post
title:  "数据结构与算法01-基础数据结构"
date:   2021-01-13
categories: study
tags: DataStructureAndAlgorithm
---

* content
{:toc}

1. 线性结构与非线性结构
2. 稀疏数组
3. 队列和数组模拟环形队列
4. 链表
5. 栈




# 一、线性结构和非线性结构

1. 线性结构
    1. 线性结构作为最常用的数据结构，其特点是数据元素之间存在一对一的线性关系
    2. 线性结构有两种不同的存储结构，即顺序存储结构(数组)和链式存储结构(链表)。顺序存储的线性表称为顺序表，顺序表中的存储元素是连续的
    3. 链式存储的线性表称为链表，链表中的存储元素不一定是连续的，元素节点中存放数据元素以及相邻元素的地址信息
    4. 线性结构常见的有：数组、队列、链表和栈，后面我们会详细讲解.
2. 非线性结构
    1. 非线性结构包括：二维数组，多维数组，广义表，树结构，图结构

# 二、稀疏数组

1. 使用场景:
编写的五子棋程序中,有存盘退出和续上盘的功能。
![五子棋图片](/assets/01.java提升计划/01.数据结构与算法/01/五子棋.jpg)

2. 分析问题:
因为该二维数组的很多值是默认值 0, 因此记录了很多没有意义的数据-->稀疏数组。

3. 基本介绍:
当一个数组中大部分元素为０，或者为同一个值的数组时，可以使用稀疏数组来保存该数组。稀疏数组的处理方法是:
    1. 记录数组一共有几行几列，有多少个不同的值
    2. 把具有不同值的元素的行列及值记录在一个小规模的数组中，从而缩小程序的规模
    ![稀疏数组](/assets/01.java提升计划/01.数据结构与算法/01/稀疏数组.jpg)

4. 应用实例
    1. 使用稀疏数组，来保留类似前面的二维数组(棋盘、地图等等)
    2. 把稀疏数组存盘，并且可以从新恢复原来的二维数组数
    3. 整体思路分析
    ![稀疏数组思路](/assets/01.java提升计划/01.数据结构与算法/01/稀疏数组思路.jpg)

# 三、队列

1. 使用场景:
银行排队叫号场景

2. 队列介绍
    1. 队列是一个有序列表，可以用数组或是链表来实现。
    2. 遵循先入先出的原则。即：先存入队列的数据，要先取出。后存入的要后取出

3. 数组模拟环形队列:
对前面的数组模拟队列的优化，充分利用数组. 因此将数组看做是一个环形的。(通过取模的方式来实现即可)
    1. front(首指针)变量的含义：front就指向队列的第一个元素，也就是说arr[front]就是队列的第一个元素，front的初始值是0
    2. rear(尾指针)：变量的含义：rear指向队列的最后一个元素的后一个位置，因为希望空出一个空间作为约定，rear的初始值=0
    3. 当队列满时，判断条件时(rear+1) % maxSize = front(实际上当队列最大长度为maxSize，其中放满元素时的容量为maxSize-1)
    4. 当队列为空的条件：rear==front
    5. 当我们这样分析，队列中有效的数据的个数(rear+maxSize-front)%maxSize

# 四、链表

## 1.单链表
1. 链表(Linked List)介绍:
链表是有序的列表，但是它在内存中是存储如下
    1. 链表是以节点的方式来存储,是链式存储
    2. 每个节点包含 data  域， next 域：指向下一个节点.
    3. 链表的各个节点不一定是连续存储.
    4. 链表分带头节点的链表和没有头节点的链表，根据实际的需求来确定
    ![链表介绍](/assets/01.java提升计划/01.数据结构与算法/01/链表介绍.jpg)

2. 单链表的应用实例
    1. 添加：
        1. 先创建一个head节点，作用就是表示单链表的头
        2. 后面我们每添加一个节点，就直接加入到链表的最后
    2. 修改：
        1. 先找到这个节点，修改其对应的属性
    3. 删除：
        1. 我们先找到需要删除的这个节点的前一个key
        2. temp.next = temp.next.next
        3. 被删除的节点，将不会有其他引用指向，会被垃圾回收机制回收

3. 单链表面试题
    1. 查找单链表的倒数第k个节点，思路：
        1. 将k和链表的头节点作为参数
        2. 先找出有多少个有效节点，比如有n个节点
        3. 找出第(n-k+1)个元素就是目标元素
    2. 单链表的反转,思路:
        1. 创建一个新的节点
        2. 依次将原链表的节点从头插入这个新节点的后面
        3. 然后将原链表的head节点的next指向新建节点的next
    3. 从尾到头打印单链表，思路：
        1. 先依次压栈，后依次出栈

## 2.双向链表
1. 管理单向链表的缺点分析:
    1. 单向链表,查找的方向只能是一个方向,而双向链表可以向前或者向后查找。
    2. 单向链表不能自我删除,需要靠辅助节点,而双向链表则可以自我删除,所以前面我们单链表删除时节点,总是找到temp,temp是待删除节点的前一个节点(认真体会).
    3. 添加和删除和单向链表类似，只不过是多了一个指向前一个节点的per指针，考虑进去便是

## 3. 约瑟夫环问题
1. Josephu(约瑟夫、 约瑟夫环)问题：Josephu 问题为： 设编号为 1,2,… n的 **n** 个人围坐一圈,约定编号为 **k（1<=k<=n）**的人从 1 开始报数,数到 **m** 的那个人出列,它的下一位又从 1 开始报数,数到 m 的那个人又出列,依次类推,直到所有人出列为止,由此产生一个出队编号的序列。

2. 思路： 用一个不带头结点的循环链表来处理 Josephu 问题： 先构成一个有 n 个结点的单循环链表,然后由 k 结点起从 1 开始计数,计到 m 时,对应结点从链表中删除,然后再从被删除结点的下一个结点又从 1 开始计数,直到最后一个结点从链表中删除算法结束

3. 单向环形链表介绍
就是最后一个节点的next指向第一个节点,整成一个圈

# 五、栈

1. 栈的一个实际需求
    1. 输入一个表达式,计算式:[7\*2\*2-5+1-5+3-3] 计算该式
    2. 请问: 计算机底层是如何运算得到结果的？注意不是简单的把算式列出运算,因为我们看到的这个是算式,但是计算机怎么理解这个算式的(对计算机而言,它接收到的就是一个字符串),我们讨论的是这个问题。

2. 栈的介绍
    1. 栈的英文为(stack)
    2. 栈是一个先入后出(FILO-First In Last Out)的有序列表。
    3. 栈(stack)是限制线性表中元素的插入和删除只能在线性表的同一端进行的一种特殊线性表。允许插入和删除的一端,为变化的一端,称为栈顶(Top),另一端为固定的一端,称为栈底(Bottom)。
    4. 根据栈的定义可知,最先放入栈中元素在栈底,最后放入的元素在栈顶,而删除元素刚好相反,最后放入的元素最先删除,最先放入的元素最后删除
    5. 图解方式说明出栈(pop)和入栈(push)的概念

3. 栈的应用场景
    1. 子程序的调用：在跳往子程序前，会先将下个指令的地址存到堆栈中，直到子程序执行完后再将地址取出，以回到原来的程序中。
    2. 处理递归调用：和子程序的调用类似，只是除了储存下一个指令的地址外，也将参数、区域变量等数据存入堆栈中。
    3. 表达式的转换[中缀表达式转后缀表达式]与求值(实际解决)。
    4. 二叉树的遍历。
    5. 图形的深度优先(depth 一 first)搜索法。

4. 栈实现计算器(中缀表达式)思路: **6+5-9x5**
    1. 通过一个index值(索引),来遍历我们的表达式
    2. 如果发现一个**数字**,就直接入数栈
    3. 如果发现**扫描到的是一个符号**,就分如下情况
        1. 如果发现符号栈为空,就直接入栈
        2. 如果发现符号栈有操作符,就进行比较,<font color=red><strong>如果当前的操作符的优先级小于或者等于栈中的操作符</strong></font>,就需要从数栈中pop出一个符号,进行运算,将得到的结果,入数栈,然后将当前的操作符入符号栈,<font color=red><strong>如果当前的操作符的优先级大于栈中的操作符,就直接入符号栈</strong></font>
    4. **当表达式扫描完毕,就顺序的从数栈和符号栈中pop出响应的数和符号,并运行**
    5. **最后在数栈中只有一个数字,就是表达式的结果**

5. 逆波兰计算器
**(3+4)× 5-6**对应的后缀表达式就是 **3 4 + 5 × 6 -**,针对后缀表达式求值步骤如下:
    1. 从左至右扫描,将 3 和 4 压入堆栈;
    2. 遇到+运算符,因此弹出 4 和 3（4 为栈顶元素,3 为次顶元素）,计算出 3+4 的值,得 7,再将 7 入栈;
    3. 将 5 入栈;
    4. 接下来是× 运算符,因此弹出 5 和 7,计算出 7× 5=35,将 35 入栈;
    5. 将 6 入栈;
    6. 最后是-运算符,计算出 35-6 的值,即 29,由此得出最终结果

6. 中缀表达式转换为后缀表达式
后缀表达式适合计算式进行运算,但是人却不太容易写出来,尤其是表达式很长的情况下,因此在开发中,我们需要将 中缀表达式转成后缀表达式。
具体步骤如下:
    1. 初始化两个栈：运算符栈 s1 和储存中间结果的栈 s2;
    2. 从左至右扫描中缀表达式;
    3. 遇到操作数时,将其压 s2;
    4. 遇到运算符时,比较其与 s1 栈顶运算符的优先级：
        1. 如果 s1 为空,或栈顶运算符为左括号"(",则直接将此运算符入栈;
        2. 否则,若优先级比栈顶运算符的高,也将运算符压入 s1;
        3. 否则,将 s1 栈顶的运算符弹出并压入到 s2 中,再次转到(4.1)与 s1 中新的栈顶运算符相比较;
    5. 遇到括号时：
        1. 如果是左括号"(",则直接压入 s1
        2. 如果是右括号")",则依次弹出 s1 栈顶的运算符,并压入 s2,直到遇到左括号为止,此时将这一对括号丢弃
    6. 重复步骤 2 至 5,直到表达式的最右边
    7. 将 s1 中剩余的运算符依次弹出并压入 s2
    8. 依次弹出 s2 中的元素并输出,结果的逆序即为中缀表达式对应的后缀表达式
