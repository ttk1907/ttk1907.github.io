---
layout: post
title:  "Java核心类库第三天"
date:   2019-10-25
categories: Java
tags: Java note
---

* content
{:toc}

1. 核心类库第3天：集合结构、Collection集合、List集合、泛型机制
2. 核心类库第4天：Queue集合、Set集合、Map集合












# Java核心类库第三天
## Java深入篇--核心类库--第3天
### 集合(容器)结构
1. 集合的由来
    1. 当需要在程序中记录单个数据内容时，则声明一个变量即可;
    2. 当需要在程序中记录多个类型相同的数据内容时，则声明一个一维数组即可;
    3. 当需要在程序中记录多个类型不同的数据内容时，则构造一个对象即可;
    4. 当需要在程序中记录多个类型相同的对象时，则声明一个对象数组即可;
    5. 当需要在程序中记录多个类型不同的对象时，则声明一个集合即可;
2. 集合框架结构
    1. 基本概念:在Java语言中集合框架的顶层是：java.util.Collection集合 和 java.util.Map集合
        1. 其中Collection集合中操作元素的基本单位是：单个元素
        2. 其中Map集合中操作元素的基本单位是：单对元素
        3. 在以后的开发中很少直接使用Collection集合，而是使用该集合的子集合：list集合、Queue集合、Set集合等。

### Collection集合(重点)
1. 基本概念
    1. java.util.Collection集合是集合框架的根接口，其他接口是该接口的子接口
2. 常用的方法
    1. boolean add(元素 e)：向集合里添加数据，成功返回true，失败返回false
    2. bollean contains(Object obj)：查找集合中有没有参数传入的对象，有则返回true，没有则返回false
    3. bollean remove(Object obj):删除成功返回true，失败返回false
    4. void clear()：全删，清空
    5. int size():返回集合中元素的个数

### List集合(重中之重)
1. 基本概念
    1. java.util.List集合是Collection集合的子集合，该集合中的元素有先后次序且允许重复
    2. 该集合的主要实现类有：ArrayList类、LinkedList类、Stack类、Vector类等
        1. 其中ArrayList类的底层是采用动态数组进行数据管理，访问方便，增删不方便
        2. 其中LinkedList类的底层是采用链表进行数据管理，增删方便，访问不方便
        3. 其中Stack类主要用于描述具有后进先出特征的数据结构，叫做栈，last in first out。该类的底层是采用数组进行数据的管理。
        4. 其中Vector类的底层采用数组进行数据的管理，与ArrayList类相比属于线程安全的类，因此效率比较低，在以后的开发中推荐使用ArrayList类取代之。
2. 常用方法(练熟、记住)
    1. void add(int index,E element)：向集合中指定位置添加元素
    2. boolean addAll(int index,Collection<?extends E>c)：向集合中添加所有元素
    3. E get(int index)：从集合中获取指定位置元素
    4. E set(int index,E element)：修改指定位置的元素,返回被修改的元素
    5. E remove(int index)：删除指定位置的元素,返回被删除的元素
    6. subList(1,list):获取List子集合,子集和原List公用一个地址

### 泛型机制(重点)
1. 基本概念
   1. 通常情况下集合中可以存放不同类型的对象，本质上是将这些对象全部看做Object类型放入的，因此从集合中取出元素时也是Object类型，为了表达元素最真实的数据类型就需要强制类型转换，而强制类型转换可能发生类型转换异常。
   2. 为了避免上述错误的发生，从jdk1.5开始提出泛型机制，也就是在集合名称的右侧使用<数据类型>的方式明确要求该集合可以存放的元素类型，若放入其它类型则编译报错
   ```java
如：
List lt1 = new LinkedList();--可以放入任意类型对象，取出麻烦
List<String> lt1 = new LinkedList<String>();--只能放入String类型，取出方便,从jdk1.7开始，new后面的<String>可以不写，写成<>
   ```

2. 原理分析
   1. 泛型的本质就是参数化类型，也就是让数据类型作为参数传递，集合定义中的E相当于形式参数负责占位，而使用集合时<>中的数据类型相当于实际参数负责给形式参数初始化，当初始化完毕后所有E被替换为实际参数表示的类型进行使用。
   2. 由于E支持的数据类型非常广泛，因此得名为"泛型".

## Java深入篇--核心类库--第4天
### Queue集合(重点)
1. 基本概念
   1. java.util.Queue集合是Collection集合的子集合，与List集合是平级关系。
   2. 该集合的主要实现类是：LinkedList类，因为该类在增删方面有一定的优势。
   3. 该集合用于描述具有先进先出特征的数据结构，叫做队列(first in first out)。
2. 常用方法
    1. boolean offer(E e)：将一个对象添加至队尾，若添加成功则返回true
    2. E poll()：从队首删除并返回一个元素
    3. E peek()：返回队首的元素(但并不删除)

### Set集合(重点)
1. 基本概念
    1. java.util.Set集合是Collection集合的子集合，与List集合以及Queue集合平级关系
    2. 该集合与List集合的主要区别在于：元素没有先后次序并且不允许重复的元素。
    3. 该集合的主要实现类有：HashSet类 和 TreeSet类。
    4. 其中HashSet类的底层采用哈希表进行数据管理的。
    5. 其中TreeSet类的底层采用二叉树进行数据管理的(选修)。
2. 常用的方法
    1. 参考Collection集合的方法即可
    2. Set集合的遍历
        1. 所有Collection的实现类都实现了其iterator方法，该方法返回一个Iterator接口类型的对象，用于实现对集合元素的迭代遍历
        2. 主要方法有
            1. booleanhasNext():判断集合中是否有可以迭代/访问的元素
            2. E next():用于取出一个元素并指向下一个元素
            3. void remove():用于删除访问到的最后一个元素
            4. 注意：当使用迭代器迭代集合中的所有元素时，若使用集合中的remove方法来删除元素，则会出现ConcurrentModificationException并发修改异常，以后的开发中应该使用迭代器的remove方法来删除元素。
    3. 使用迭代器来访问集合中的所有元素

    ```java
3.使用迭代器来访问集合中的所有元素[one, two]
    3.1 调用成员方法获取迭代器对象
    Iterator<String> it = s1.iterator();
    3.2 使用迭代器对象获取每个元素并打印
    判断该迭代器指向的集合中是否拥有可以迭代/遍历的元素
    System.out.println(it.hasNext()); // true
    获取一个元素并指向下一个位置
    与toString方法相比取出的是单个元素，更加灵活
    System.out.println("获取到的元素是：" + it.next()); //one 
while(it.hasNext()) {
    System.out.println("获取到的元素是：" + it.next());
        }
    ```


3. 增强版的for循环(for each结构)
    1. 语法格式
    ```java
for(元素类型 变量名 : 数组名/集合名) {
    循环体;
}
   ```

    2. 执行流程:不断地从数组或集合中取出一个元素并赋值给变量并执行循环体，直到处理完毕所有元素为止。
    3. 总结：
        1. 遍历Set集合的方式有三种：toString()、for each结构、迭代器方式
        2. 遍历List集合的方式有四种：除了上述3种方式外，还有get方法。

### Map集合(重点)
1. 基本概念:java.util.Map<K,V>集合中操作元素的基本单位是：单对元素，其中类型参数如下：  
    1. K - 此映射所维护的键(key)的类型
    2. V - 映射值(value)的类型
    3. 该集合中不允许出现重复的键，每个键最多只能映射到一个值。 
    4. 该集合的主要实现类有：HashMap类 和 TreeMap类。
    5. 其中HashMap类的底层是采用哈希表进行数据管理的。
    6. 其中TreeMap类的底层是采用二叉树进行数据管理的。
2. 常用方法
    1. V put(K key,V value);将key-value对存入Map,若集合中已经包含该key,则替换该Key所对应的Value,返回值为该Key原来所对应的Value,若没有则返回null
    2. V get(Object key);返回与参数Key所对应的Value对象,如果不存在则返回null
    3. boolean containsKey(K Key);查找键是否存在，存在即返回true,不存在即返回false
    4. boolean containsValue(V Value);查找数据是否存在，存在即返回true,不存在即返回false
    5. V remove(K Key);删除元素，不存在该元素则返回null,存在该元素则返回该元素本身
3. 遍历Map集合
    1. 方式1：toString方法
    2. 方式2：enTrySet方法，以键值对为基本单位进行转换
    ```java
Set<Map.Entry<Integer,String>> s1 = m1.entrySet();
for(Map.Entry<Integer,String> me : s1) {
    System.out.println(me);
    me.getKey();
    me.getValue();
}
    ```

    3. 方式3：keySet方法，以键为基本单位进行转换
    ```java
Set<Integer> s2 = m1.keySet();
for(Integer in : s2){
    System.out.println(in+"="+m1.get(in));
}
    ```

4. Map集合的实际应用
    1. Map集合是面向对象查询优化的数据结构，在大数据量情况下有着优良的查询性能，经常用于根据key检索value的业务场景
    2. 用户登陆数据缓冲：用户名是key，用户对象是value，在登录验证的时候根据用户名快速查询用户信息
    3. 登录会话保持状态：在网站编程中，用户会话状态保持经常采用Map存储，可以快速在数以万计的信息中快速确定用户是否已经登录






































