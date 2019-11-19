---
layout: post
title:  "Java核心类库第四天"
date:   2019-10-28
categories: Java
tags: Java note
---

* content
{:toc}

1. 核心类库第5天：异常机制、File类、IO流、FileOutputStream类
2. 核心类库第6天：FileInputStream类、BufferedWriter类、BufferedReader类、PrintStream类、ObjectOutputStream类、ObjectInputStream类、经验分享、transient关键字










# Java核心类库第四天
## Java深入篇--核心类库--第5天
### 异常机制
1. 基本概念
    1. 异常就是"不正常"的含义，在Java语言中用于表示运行阶段发生的错误。
    2. java.lang.Throwable类是Java语言中所有错误(Error)和异常(Exception)的超类。
    3. 其中Error类主要用于描述比较严重无法编码解决的问题，如：JVM挂了。
    4. 其中Exception类主要用于描述比较轻微可以编码解决的问题，如：0作为除数。
2. 基本分类
    1. java.lang.Exception类是所有异常类的超类，主要分为以下两大类：
        1. RuntimeException - 运行时异常，也叫作非检测性异常
        2. IOException和其它异常 - 其它异常，也叫作检测性异常--所谓检测性异常就是在编译阶段能够被编译器检测出来的异常
   2. 其中RuntimeException类的主要子类：
        1. ArithmeticException - 算术异常
        2. ArrayIndexOutOfBoundsException - 数组下标越界异常
        3. NullPointerException - 空指针异常
        4. ClassCastException - 类型转换异常
        5. NumberFormatException - 数字格式异常
    3. 注意：当程序执行过程中发生异常但没有手动处理时，由Java虚拟机采用默认方式处理，而默认处理方式就是：打印异常名称、异常原因、异常发生的位置等并终止程序。
3. 异常的避免
    1. 在以后的开发中尽量使用if条件判断来避免异常的发生。
4. 异常的捕获
    1. 语法格式
    ```java
     try {
        编写可能发生异常的语句;
     } 
     catch(异常类型 变量名) {
        编写针对该类异常的处理语句；
     } 
     ...
     finally {
        编写无论是否发生异常都应该执行的语句；
     } 
    ```

    2. 注意实现
        1. 当需要编写多个catch分支时，切记小类型的异常应该放在大类型异常的上面。
        2. 懒人的写法：catch(Exception e){ ... }    
        3. finally主要用于编写善后处理的语句，如：关闭已经打开的文件等
    3. 执行流程
    ```java
try {
  a;
  b;  - 可能发生异常的语句
  c;
} catch(...) {
  d;
} finally {
  e;
}
当上述程序执行过程没有发生异常时的执行流程：a b c e;
当上述程序执行过程发生异常时的执行流程：a b d e;
    ```

5. 异常的抛出
    1. 基本概念：在某些特殊情况下产生的异常无法处理或者不便于处理时，就可以将该异常转移给该方法的调用者，这种方式就叫做异常的抛出。
    2. 语法格式
    ```java
    访问权限 返回值类型 方法名称(形参列表) throws 异常类型1, 异常类型2, ...{}
如：
    public void show() throws IOException {}
    ```

    3. 方法重写的原则
        1. 要求方法名相同、参数列表相同、返回值类型相同，从jdk1.5开始允许返回子类类型
        2. 要求方法的访问权限不能变小，可以相同或者变大
        3. 要求不能抛出更大的异常
6. 自定义异常
    1. 基本概念：虽然Java官方提供了大量的异常类，但一定不会包含所有开发中可能出现的异常，在Java程序中若需要表达特定问题的特定异常时，就需要程序员自定义异常来描述。
    2. 实现流程
        1. 自定义xxxxException继承自Exception类或者其子类；
        2. 提供两个版本的构造方法：无参构造方法 和 字符串作为参数的构造方法；
    3. 例子
    ```java
1.自定义年龄异常
public class AgeException extends Exception {
    private static final long serialVersionUID = 1L;
    public AgeException() {
    }
    public AgeException(String msg) {
        super(msg); // 调用父类的有参构造方法
    }
2.自定义异常成员方法
public void setAge(int age) throws AgeException {
        if(age > 0 && age < 150) {
            this.age = age;
        } else {
            //System.out.println("年龄不合理！！！");
            // 产生异常来表达年龄不合理的抗议
            //throw new NullPointerException();
            throw new AgeException("年龄不合理！！！");
        }
    }
    ```

### File类(查手册会用即可)
1. 基本概念：java.io.File类主要用于描述文件和目录的路径信息，可以获取名称、大小等属性信息
2. 常用方法
    1. File(String Pathname)：根据参数指定的路径来构造对象
    2. boolean exists()：测试此抽象路径名表示的文件或目录是否存在
    3. String getName()：返回由此抽象路径名表示的文件或目录的名称
    4. long length()：返回由此抽象路径名表示的文件的长度
    5. long lastModified()：返回此抽象路径名表示文件最后一次修改时间
    6. String getAbsolutePath()：返回此抽象路径名表示文件的绝对路径信息
    7. boolean delete()：用于删除文件，当删除目录时要求是空目录
    8. boolean createNewFile()：用于创建新的空文件
    9. boolean mkdir()：用于创建目录
    10. boolean mkdirs()：用于创建多级目录
    11. boolean isFile()：用于判断该对象是否为标准文件
    12. boolean isDirectory()：用于判断该对象是否为目录文件
    13. File[] listFiles()：用于获取一个目录中的所有内容

### IO流
1. 基本概念
    1. I/O就是Input/Output的简写，也就是输入输出的含义。
    2. I/O流就是像流水一样不间断地进行输入输出的状态。
2. 基本分类
    1. 按照数据读写的基本单位不同分为: 字节流 和 字符流。
        1. 其中字节流主要指以字节为单位进行读写的流，可以处理任意类型的文件；
        2. 其中字符流主要指以字符(2个字节)为单位进行读写的流，只能处理文本文件；
    2. 按照数据流动的方向不同分为：输入流 和 输出流(站在程序的角度)。
        1. 其中输入流主要指从文件中读取数据内容输入到程序中，也就是读文件；
        2. 其中输出流主要指将程序中的数据内容输出到文件中，也就是写文件；
    3. 节点流和包装流
        1. 节点流：直接跟文件关联
        2. 包装流：间接跟文件关联
3. IO流框架结构
![IO流结构](/assets/IO流结构.png)

### FileOutputStream类(字节类、重中之重)
1. 基本概念：java.io.FileOutputStream类主要用于将图像数据之类的原始字节流写入输出流中。
2. 常用方法
    1. void write(int b)：将指定字节写入此文件输出流
    2. void write(byte[] b,int off,int len)：将指定字节数组中从偏移量off开始的len个字节写入此文件输出流
    3. void write(byte[] b)：将b.length个字节从指定字节数组写入此文件输出流中
    4. void close()：用于关闭文件输出流并释放有关的资源
3. 构造方法
    1. 无参构造：FileOutputStream(String name)--根据参数指定的文件名来构造对象
    2. 有参构造：FileOutputStream(String name,boolean append)--表示以追加的方式根据参数指定的文件来构造对象

## Java深入篇--核心类库--第6天
### FileInputStream类(字节类、重中之重)
1. 基本概念
    1. java.io.FileInputStream类主要用于从输入流中读取图像数据之类的原始字节流。
2. 常用方法
    1. FileInputStream(String name)--根据参数指定的文件路径名来构造对象
    2. int read()：如果没到达末尾，返回实际读取到的数值。如果已到达文件末尾，则返回-1
    3. int read(byte[] b)：从此输入流中将最多b.length个字节的数据读入一个字节数组中，返回读取的字节的个数，到达文件末尾就返回-1
    4. int read(byte[] b,int off,int len)：从此输入流中将最多len个字节的数据读入一个字节数组中
    5. void close()：用于关闭文件输出流并释放有关的资源

### BufferedWriter类(重点、字符类)
1. 基本概念
    1. java.io.BufferedWriter类主要用于向输出流中写入单个字符、字符数组以及字符串
2. 构造方法
    1. BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(路径)))
3. 常用方法
    1. void write(int c)：用于写入单个字符到输出流中
    2. void write(char[] cbuf,int off,int len)：用于将字符数组cbuf中从下标off开始的len个字符写入到输出流中
    3. void write(char[] cbuf)：用于将字符数组cbuf中所有内容写入输出流
    4. void write(String str)：用于将参数指定的字符串内容写入输出流中
    5. void newLine()：用于写入行分隔符到输出流中
    6. void close()：用于关闭文件输出流并释放有关的资源

### BufferedReader类(重点、字符类)
1. 基本概念
    1. java.io.BufferedReader类主要用于从输入流中读取单个字符、字符数组以及一行字符串内容。
2. 构造方法
    1. BufferedReader bw = new BufferedReader(new InputStreamReader(new FileInputStream(路径)));
3. 常用方法
    1. int read()：用于读取单个字符并返回，若读取到文件末尾则返回-1，否则返回实际读取到字符的整数值
    2. int read(char[] cbuf,int off,int len)：用于从输入流中读取len个字符放入cbuf中下标从off开始的位置上，若读取到末尾则返回-1，否则返回实际读取到的字符个数
    3. int read(char[] cbuf)：用于从输入流中读满整个数组cbuf
    4. String readLine()：用于读取一行字符串并返回
    5. void close()：用于关闭文件输出流并释放有关的资源

### PrintStream类(重点、字节类)
1. 基本概念
    1. java.io.PrintStream类主要用于方便地打印各种数据内容并且自动刷新。 
2. 构造方法：
    1. PrintStream ps = new PrintStream(new FileOutputStream(路径));
3. 常用方法：
    1. void print(String s)：用于将参数指定的字符串内容打印出来
    2. void println(String x)：用于打印字符串后并终止该行
    3. void close()：用于关闭文件输出流并释放有关的资源

### ObjectOutputStream类(重点、字节类)
1. 基本概念
    1. java.io.ObjectOutputStream类主要用于将Java语言中的对象整体写入输出流中。
    2. 只能将支持 java.io.Serializable 接口的对象写入流中。
    3. 类通过实现 java.io.Serializable 接口以启用其序列化功能。
    4. 所谓序列化就是指将一个对象相关的所有信息有效组织成字节序列的转化过程。
2. 构造方法
    1. ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(路径));
3. 常用方法
    1. void writeObject(Object obj)：用于将参数指定的对象整体写入到输出流中
    2. void close()：用于关闭文件输出流并释放有关的资源

### ObjectInputStream类(重点、字节类)
1. 基本概念
    1. java.io.ObjectInputStream类主要用于从输入流中一次性将一个对象的内容读取出来。实现了从字节序列到对象的转化过程，叫做反序列化。
2. 构造方法
    1. ObjectInputStream ois = new ObjectInputStream(new FileInputStream(路径));
3. 常用方法
    1. Object readObject()：主要用于从输入流中读取一个对象并返回无法通过返回值来判断是否读取到文件的末尾
    2. void close()：用于关闭文件输出流并释放有关的资源

### 经验分享
当需要写入多个对象到文件中时，建议先将多个对象放入一个集合对象中，然后将集合对象看做一个整体只需要调用一次writeObject方法就可以写入所有内容，此时只需要调用一次readObject方法就可以将所有内容读取出来，这样就避免了通过返回值来判断是否读取到文件的末尾。

### transient关键字
transient是Java语言中的关键字，用来表示一个特征不是该对象序列化的一部分。当一个对象被序列化的时候，transient型变量的值不包括在序列化的表示中，然而非transient型的变量是被包括进去的






