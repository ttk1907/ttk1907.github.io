---
layout: post
title:  "Java-Spring框架第三天"
date:   2019-11-27
categories: Spring
tags: Spring note
---

* content
{:toc}

1. Spring第3天:Spring的声明式事务、Spring Web MVC、Spring MVC 的编程步骤、Spring MVC接受请求的参数










# Spring第3天
## Spring 的声明式事务 
1. 在Spring的配置文件中开启声明式事务

```xml
  <tx:annotation-driven    transaction-manager="事务管理器id"  
      proxy-target-class="false" />
```

2. proxy-target-class 默认使用SUN公司的代理机制,如果产生不了,则启用CGLIB,如果proxy-target-class="true"  则直接使用CGLIB的代理机制 
3. 创建事务管理器组件  -----  注意这个组件需要依赖于dataSource 

```xml
<bean  id="transactionManager"  
  class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
  <property name="dataSource"  ref="dataSource"></property>
</bean>    
```

4. 在类上或者在业务方法加事务控制标注**@Transactional**  
    1. 在类上加控制标注之后:整个类的所有方法一起成功,一起失败
    2. 在业务方法上加控制标注后:这个方法里的每一步要么一起成功,要么一起失败  

5. @Transactional的属性
    1. **rollbackFor:**Spring 的声明式事物默认只针对运行时异常回滚,对检查异常不回滚,可以通过rollbackFor属性指定对应的检查异常进行回滚
    2. **noRollbackFor**:针对指定的运行时异常不回滚
    3. **readOnly**:只读事物,当事物中只有查询语句时可以把readOnly设置成true,代表只读事务,只要有DML操作,设置成true无效
    4. **isolation**:隔离,用来设置事务的隔离级别的
        1. **事务的隔离级别**:读未提交,读提交,可重复度,序列化
        2. 用来解决数据库中的三大问题:
        3. **脏读**:一个事务读取到另外一个事务没有提交的数据
        4. **不可重复读**:一个事务在开始时读取了一份数据,另外一个事物修改了这份数据并进行了提交,当第一个事务再次读取数据发现数据发生了改变,这叫做不可重复读
        5. **幻读**:一个事务统计了整张表的数据,另外一个事务对表增加了数据,并进行了提交,当第一个事务再次统计数据时发现数据发生了改变
    5. **propagation** 事务传播特性
        1. 一个方法去调用一个事务方法时,事务应该如何表现
        2. propagation.REQUIRED,如果当前方法不存在事务,则会开启新事物,如果当前方法存在事务,则加入到当前事务之中]]

## Spring Web MVC
1. Spring MVC的五大核心组件 
    1. DispatcherServlet     控制器    请求的入口 
    2. HandlerMapping        控制器    派发请求  让请求和控制器建立一一对应的关联关系 
    3. Controller            控制器    真正的请求的处理者
    4. ModelAndView          模型和视图   封装了数据信息和视图信息
    5. ViewResolver          视图处理器  
  
## Spring MVC 的编程步骤1 
1. 建立一个项目,导入jar包(ioc mvc),拷贝Spring配置文件到src下,在WEB-INF下建立 hello.jsp 
2. 在web.xml 中配置DispatcherServlet 并通过初始化参数contextConfigLocation  来指定spring配置文件的位置
3. 在Spring 配置文件中配置HandlerMapping的实现类SimpleUrlHandlerMapping,并通过mappings 属性让请求和控制器建立一一对应的关联关系
4. 编写一个java类,实现Controller接口,覆盖接口方法返回ModelAndView,同时在Spring 容器中创建 Controller 的实现类的对象 
5. 在Spring 配置文件中配置ViewResolver的实现类InternalResourceViewResolver,需要配置前缀和后缀 

## Spring MVC 的编程步骤2
1. 建立一个项目,导入jar包(ioc aop mvc) 拷贝配置文件到src下,并在WEB-INF下建立一个login.jsp
2. 在web.xml 中配置DispatcherServlet 并通过初始化参数contextConfigLocation  来指定spring配置文件的位置   
```xml
<servlet>
    <servlet-name>Spring-MVC<servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>classpath:applicationContext.xml</param-value>
        </init-param>
</servlet>
<servlet-mapping>
    <servlet-name>Spring-MVC</servlet-name>
    <url-pattern>*.do</url-pattern>
</servlet-mapping>
``` 

3. 开启组件扫描和标注形式mvc:  
```xml
<context:component-scan base-package="包名"/>
<mvc:annotation-driven/>
(这句配置帮你在Spring容器中创建了一个ReqeuestMappingHandlerMapping对象)
```  

4. 编写一个控制器类,不用实现Controller接口,使用@Controller把普通java类转换成控制器,@RequestMapping("/请求路径"),返回值可以是String,也可以是ModelAndView 方法名自由(参数自由)   
```java  
@Controller
public class LoginController {
    @RequestMapping("/toLogin.do")
    public String toLogin(){
        return "login";
    }  
}
```

5. 配置视图处理器,配置前缀和后  
```xml  
<bean id="viewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
    <property name="prefix" value="/WEB-INF/"/>
    <property name="suffix" value=".jsp"/>
</bean>
```  

## Spring MVC接受请求的参数
1. 之前的方式依然可以使用:通过request来获取,`request.getParameter("name")`
2. 直接定义和页面参数同名的控制器参数
3. 页面参数和控制器参数不一致:`@RequestParam("页面参数名")控制器参数上`
4. 定义对象类型的控制器参数(要求属性和请求参数对应)




