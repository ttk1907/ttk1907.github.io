---
layout: post
title:  "Java-Spring框架第一天"
date:   2019-11-25
categories: Spring
tags: Spring note
---

* content
{:toc}

1. Spring第1、2天：项目开发思路MVC、Spring










# Spring第1天
## 项目开发思路 MVC
1. 根据需求文档,建立对应的表 xdl_user
2. 根据表建立对应的实体类 XdlUser
3. 定义一个DAO接口
4. 利用jdbc的工具类结合JDBC访问数据库的五步完成功能
5. 加一个工厂类提供DAO的实现类,解除Service和DAO的耦合度
6. 编写一个业务类 XdlUserService 注册--测试 ----M
7. 经典方法:
    1. 编写控制器类,使用M层获取快件列表,放入request中,转发到快件列表对应的jsp----C
    2. 使用jstl + el在jsp中展示快件列表----V
8. Ajax方法:
    1. 编写一个控制器,使用M层获取快件列表,使用第三方jar包把列表转换成JSON字符串写给浏览器----C
    2. jsp中发送ajax请求把返回的数据使用jsp显示到页面中----V

## Spring
SSM-Spring-SpringMVC-MyBatis
### 1.Spring 框架的构成    
1. IOC:控制反转,它是Spring框架的核心 
2. DAO:数据访问对象模块,它是对JDBC的封装和简化
3. WebMVC:它是Spring 对 javaweb的支持以及MVC设计模式的支持
4. AOP:面向切面编程,它是对面向对象的扩展 
5. ORM:对象关系映射(是以面向对象的思想访问数据库),Mybatis

### 2.什么是IOC?
1. Inverstion Of Control   控制反转   
2. 程序中需要某个对象时由原来的new的方式改成了由容器来进行 创建和管理以及维护组件关系。这样做的好处是可以大大降低组件之间的耦合度。

### 3.Spring 容器
1. 任何的java类都可以在Spring容器中创建对象并由容器进行管理以及维护组件关系
2. Spring容器实现了 IOC 和 AOP 机制
3. Spring容器的类型BeanFactory或者是ApplicationContext类型

### 4.使用Spring容器完成IOC的步骤  
1. 建立一个项目导入jar包(ioc相关jar包)拷贝Spring配置文件到src下
2. 在SPring配置文件中 配置对象创建的说明`<bean id="对象的引用名" class="包名.类名"></bean>`
3. 创建Spring容器对象和从容器中获取对象  

```java
ApplicationContext app = new ClassPathXmlApplicationContext("配置文件名");
app.getBean("对象的引用名",类型.class);
```  

### 5.Spring容器创建对象的三种方式
1. **构造器方式实例化:** `<bean  id="标识符"  class="包名.类名"></bean>`,默认调用类型对应的无参构造方法
2. **静态工厂方法实例化:**本质上是类型调用对应的静态方法 来获取一个对象,`类型名.静态方法名()`,比如在java代码中创建一个Calendar类型的对象:`<bean id="标识符"  class="包名.工厂类名" factory-method="静态方法名"></bean>`
3. **实例工厂方法实例化:**本质上是利用一个已经存在的对象 来创建出另外一个类型的对象,`<bean id="标识符"    factory-method="实例方法名"  factory-bean="工厂对象的id"></bean>`

### 6.Spring中对象的作用域
1. Spring中对象默认的作用域是单例的,如果希望每次请求都获取不同的对象,则可以使用bean标记中的scope属性指定作用域。scope 默认的取值是`singleton`,设置成`prototype`则为非单例的。
2. 当然这里也有request、session等作用域这到web部分才会涉及。

### 7.Spring容器中的对象的初始化和销毁 
1. **初始化:**一个对象被容器创建之后,可以通过`beans`标记中的 `default-init-method`属性来指定初始化方法,由于这样影响的范围比较大(影响配置文件中所有的对象).所以对象对应的类型中如果没有对应的初始化方法程序也不会报错。也可以通过`bean`标记中的`init-method`属性来指定初始化方法,这种方式只会影响到一个对象所以对象对应的类型中如果没有对应的初始化方法程序就会报错。

2. **销毁:**当一个对象即将消亡时可以通过`beans`标记中的`default-destroy-method`属性来指定销毁方法,由于这样影响的范围比较大(影响配置文件中所有的对象).所以对象对应的类型中如果没有对应的销毁方法程序也不会报错。也可以通过`bean`标记中的`destroy-method`属性来指定销毁方法,这种方式只会影响到一个对象所以对象对应的类型中如果没有对应的销毁方法程序就会报错,但是销毁方法只针对单例模式的对象。

### 8.**bean对象的延迟实例化:**
1. 在Spring容器中对象默认的作用域是单例的,Spring容器对单例对象 默认是容器启动时创建,可以通过bean标记的`lazy-init="true"` 让其使用到的时候创建,容器启动时不创建。

### 9.什么是DI?
1. Dependence Injection : 依赖注入(依赖注射)
2. 把一个组件的值设置给另外一个组件的过程叫依赖注入,DI解决的问题就是组件的装配问题 

### 10.**DI的三种实现方式**
1. **setter注入:**
    1. 参考类型对应的set方法来进行值的设置,在bean标记中出现如下配置:`<property name="属性名" value="值"> </property>`
    2. `属性名`:这是设置值,所以参考的是set方法去掉set然后首字母小写.如果要赋值复杂的值,则需要使用`ref`,value能赋值的类型有**八种基本类型**和**封装类、String、枚举**

2. **构造器注入:**
    1. 参考的是构造方法的参数,只要构造方法的参数能匹配上,则直接调用对应的带参构造,在bean标记中出现如下配置:
    2. 把上面的 property 标记 换成 `constructor-arg`注意我们可以使用`index`替换name,index代表参数的编号,编号0开始 

3. **自动化注入:**
    1. 主要解决复杂值的注入问题,只要在bean标记中使用`autowire`属性,指定自动化注入的方式即可
    2. autowire的取值有:byName、byType、constructor
    3. byName : 参考的是属性名
    4. byType : 参考的是成员变量的类型 
    5. constructor : 参考的是构造方法

### 11.组件扫描
1. **什么是组件扫描:**
    1. Component Scan 组件扫描,替代的ioc的功能
    2. 它是Spring 提供的一套基于标注(注解)的技术
    3. 目的是简化XML的配置
2. 实现组件扫描的步骤
    1. 建立一个项目导入jar包(ioc aop),并拷贝配置文件到src下
    2. 在配置文件中开启组件扫描:`<context:component-scan base-package="包名"/>`
    3. 建立一个类,然后在类上打对应的标注
        1. @Repository:持久层标注,一般加在DAO上
        2. @Service:服务层标注
        3. @Controller:控制层标注
        4. @Component:通用层标注
    4. 创建Spring容器,从容器中获取对象进行测试
3. 标注的三种写法
    1. @Component():调用时写类名的小写
    2. @Component(value = "ee"):调用时写ee
    3. @Component("ee"):调用时写ee
4. 和组件相关的其他标注
    1. @Scope("singleton" or "prototype"):和对象作用域相关的标注
    2. @PostContruct:加在初始化方法上
    3. @PreDestroy:即将销毁对象时调用的方法
5. 和DI相关的标注
    1. @Value:
        1. 它可以用在成员变量上或者set方法上
        2. 如果是简单值(8种基本类型和封装类String 枚举)可以直接使用@Value("值"),但是如果是复杂对象的赋值,则需要使用Spring的EL表达式赋值(从Spring容器中进行取值,取值的语法是把之前的$换成#即可)
    2. @Autowired:
        1. 它可以用在成员变量、set方法、构造方法上
        2. 它是用来解决复杂值的装配问题的
        3. 它优先适用类型进行匹配,如果类型有冲突,则会启用名字匹配进行装配
        4. 它可以和@Qualifier配合使用,@Qualifier可以指定查找的组件名,如果找不到程序报错,注意,@Qualifier不能用在构造方法上
        5. 当使用@Qualifier指定名字查找时对组件的依赖属于强依赖(找不到程序就报错),可以使用@Autowired的属性requried=false来解除这种强依赖,就是让程序尽量的去查找组件,找不到也不报错
    3. @Resource
        1. 它可以用在成员变量、set方法上
        2. 它也是用来解决复杂值的装配问题
        3. 它优先按照名字(参考的是set方法名而不是参数的名字)进行匹配,如果名字不匹配会启用类型进行匹配
        4. 它是JDK提供的标注
        5. 可以通过@Resource的那么属性指定查找的组件,如果找不到就报错,但是无法解除强依赖





























